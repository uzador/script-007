from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import logging
from .file_service import FileService
from .utils import get_file_key_path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseCipher:

    def __init__(self, fs: FileService):
        self.fs = fs

    def create(self, file_path: str, content: bytes):
        self.fs.create(file_path, content)

    def read(self, file_path: str) -> bytes:
        return self.fs.read(file_path)

    def remove(self, file_path: str) -> None:
        self.fs.remove(file_path)

    def get_meta(self, file_path: str) -> str:
        return self.fs.get_meta(file_path)

    def encrypt(self, content):
        pass

    def decrypt(self, key: bytes, nonce: bytes,
                tag: bytes, ciphertext: bytes) -> bytes:
        pass


class AESCipher(BaseCipher):

    def __init__(self, fs: FileService):
        super().__init__(fs)

    def encrypt(self, content: bytes):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(content)
        return ciphertext, tag, cipher.nonce, key

    def create(self, file_path: str, content: bytes) -> None:
        ciphertext, tag, nonce, key = self.encrypt(content)
        file_key_path = get_file_key_path(file_path)
        super().create(file_key_path, key)
        super().create(file_path, b''.join([nonce, tag, ciphertext]))

    def decrypt(self, key: bytes, nonce: bytes,
                tag: bytes, ciphertext: bytes) -> bytes:
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(ciphertext, tag)

    def read(self, file_path: str) -> bytes:
        file_key_path = get_file_key_path(file_path)
        key = super().read(file_key_path)

        f = open(file_path, "rb")
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

        return self.decrypt(key, nonce, tag, ciphertext)

    def remove(self, file_path):
        super().remove(file_path)
        super().remove(get_file_key_path(file_path))
