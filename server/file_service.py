import os
import logging
from datetime import datetime
import server.exception as exception

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FileService:

    def create(self, file_path: str, content: bytes) -> None:
        """ Function to create file:
        file_name: name of created file
        content: content of created file
        """
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'wb') as f:
                    if content:
                        f.write(content)
                    else:
                        f.write(b'empty file')
                logger.info(f'file {file_path} created')
            except OSError as ose:
                raise exception.CreateFileException(
                    f'Can not create {file_path} cause {ose.strerror}')
        else:
            raise exception.CreateFileException(
                f'Can not create {file_path} cause it exists')

    def remove(self, file_path: str) -> None:
        """ Function to remove file:
        file_name: name of removed file
        """
        try:
            os.remove(file_path)
            logger.info(f'file {file_path} removed')
        except OSError as e:
            raise exception.RemoveFileException(
                f'Can not remove {file_path} cause {e.strerror}')

    def read(self, file_path: str) -> bytes:
        """ Function to read file
        Takes file and returns its content
        """
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except OSError as ose:
            raise exception.ReadFileException(
                f'Can not read {file_path} cause {ose.strerror}')

    def get_meta(self, file_path: str) -> str:
        """ Function to get file's meta date:
        file_name: name of the file
        """
        try:
            size = os.path.getsize(file_path)
            access_time = datetime.fromtimestamp(os.path.getatime(file_path))
            create_time = datetime.fromtimestamp(os.path.getctime(file_path))
            modify_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            return f'size: {size} bytes access_time: {access_time}' \
                   f' create_time: {create_time} modify_time: {modify_time}'
        except OSError as ose:
            raise exception.GetMetaDataException(
                f'Can not get metadata {file_path} cause {ose.strerror}')
