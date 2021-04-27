import hashlib
from .file_service import FileService
import server.utils as utils
import server.exception as exception


class FileServiceSigned(FileService):

    def create(self, file_path, content):
        super().create(file_path, content)
        file_signed_path = utils.get_file_signed_path(file_path)
        signature = self.get_signature(
            [file_signed_path, super().get_meta(file_path)])
        super().create(file_signed_path, signature)

    def read(self, file_path):
        file_signed_path = utils.get_file_signed_path(file_path)
        signature = super().read(file_signed_path)
        calculated_signature = self.get_signature(
            [file_signed_path, super().get_meta(file_path)])

        if signature != calculated_signature:
            raise exception.SignatureException("Different signatures")

        return super().read(file_path)

    def remove(self, file_path):
        file_signed_path = utils.get_file_signed_path(file_path)
        super().remove(file_path)
        super().remove(file_signed_path)

    @staticmethod
    def get_signature(data):
        m = hashlib.sha512()
        for part in data:
            m.update(part.encode())
        return m.hexdigest()
