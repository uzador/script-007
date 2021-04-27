from .file_service import FileService
from .file_service_signed import FileServiceSigned
from .config import CRYPTO

if "HASH" == CRYPTO:
    fs = FileServiceSigned()
else:
    fs = FileService()
