from .file_service import FileService
from .file_service_hash_signed import FileServiceSigned
from .file_service_hybrid_signed import AESCipher
from .config import CRYPTO

if CRYPTO:
    if "HASH" == CRYPTO:
        fs = FileServiceSigned()
    elif "SYMMETRIC" == CRYPTO:
        fs = AESCipher(FileService())
    else:
        fs = FileService()
else:
    fs = FileService()
