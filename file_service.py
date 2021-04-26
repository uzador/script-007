import os
import logging
import utils
from datetime import datetime

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CreateFileException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class ReadFileException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class RemoveFileException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class GetMetaDataException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)


class FileService:

    def __init__(self):
        pass

    @staticmethod
    def create(file_path, content):
        """ Function to create file:
        file_name: name of created file
        content: content of created file
        """
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'w') as f:
                    if content:
                        for line in content:
                            f.write(line)
                    else:
                        f.write('empty file')
                logger.info('file {} created'.format(file_path))
            except OSError as ose:
                raise CreateFileException('Can not create {} cause {}'
                                          .format(file_path, ose.strerror))
        else:
            raise CreateFileException('Can not create {} cause it exists'
                                      .format(file_path))

    @staticmethod
    def remove(file_path):
        """ Function to remove file:
        file_name: name of removed file
        """
        try:
            os.remove(file_path)
            logger.info('file {} removed'.format(file_path))
        except OSError as e:
            raise RemoveFileException('Can not remove {} cause {}'
                                      .format(file_path, e.strerror))

    @staticmethod
    def read(file_path):
        """ Function to read file
        Takes file and returns its content
        """
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except IOError as ioe:
            raise ReadFileException('Can not read {} cause {}'
                                    .format(file_path, ioe.strerror))
        except OSError as ose:
            raise ReadFileException('Can not read {} cause {}'
                                    .format(file_path, ose.strerror))

    @staticmethod
    def get_meta(file_path):
        """ Function to get file's meta date:
        file_name: name of the file
        """
        try:
            size = os.path.getsize(file_path)
            atime = datetime.fromtimestamp(os.path.getatime(file_path))
            ctime = datetime.fromtimestamp(os.path.getctime(file_path))
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

            return 'size: {} bytes atime: {} ctime: {} mtime: {}' \
                .format(size, atime, ctime, mtime)
        except IOError as ioe:
            raise GetMetaDataException('Can not get metadata {} cause {}'
                                       .format(file_path, ioe.strerror))
        except OSError as ose:
            raise GetMetaDataException('Can not get metadata {} cause {}'
                                       .format(file_path, ose.strerror))

    COMMANDS = {
        'create': create,
        'read': read,
        'remove': remove,
        'get_meta': get_meta,
    }

    @staticmethod
    def default_cmd(cmd):
        """ Function to be called when incoming command is unknown """
        logger.warn('Unknown command received')

    @staticmethod
    def process(cmd, file_name, content):
        """ Handler to process incoming commands
        cmd: command name
        file_name: file name to be processed by command
        content: content of the file in case of create command
        """
        logger.info('command: {}, file_name: {}, content: {}'
                    .format(cmd, file_name, content))
        try:
            utils.check_working_dir()
            cmd_to_execute = FileService.COMMANDS.get(cmd, FileService.default_cmd)
            file_path = utils.build_path(file_name)
            if content:
                result = cmd_to_execute(file_path, content)
            else:
                result = cmd_to_execute(file_path)

            if result:
                logger.info('result = {}'.format(result))
        except CreateFileException as e:
            logger.error('CreateFileException: {}'.format(e.message))
        except ReadFileException as e:
            logger.error('ReadFileException: {}'.format(e.message))
        except RemoveFileException as e:
            logger.error('RemoveFileException: {}'.format(e.message))
        except GetMetaDataException as e:
            logger.error('GetMetaDataException: {}'.format(e.message))
