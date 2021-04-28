import os
import logging
import argparse
from server.config import WORKING_DIR

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_args() -> argparse.Namespace:
    """ Parse incoming arguments:

    -c/--command -- executed command (create, delete, read, get_meta)
    -n/--file_name -- file to be processed by above command
    -e/--content -- content for command create
    """
    parser = argparse.ArgumentParser(
        description='Process commands: create, delete, read, get_meta')

    parser.add_argument('-c', '--command', required=True,
                        help='command to be executed')
    parser.add_argument('-n', '--file_name', required=True,
                        help='file name')
    parser.add_argument('-e', '--content', required=False, nargs='+',
                        help='file content')

    return parser.parse_args()


def check_working_dir() -> bool:
    """ Checks if working dir exists and creates one otherwise """
    if os.path.isdir(WORKING_DIR):
        return True
    else:
        os.mkdir(WORKING_DIR)
        logging.info("working dir created")
        return False


def build_path(file_name: str) -> str:
    """ Build file path from config.WORKING_DIR """
    return os.path.join(WORKING_DIR, file_name)


def encode_content(content: list) -> bytes:
    """ Encode content to bytes """
    return b''.join([part.encode() for part in content])


def get_file_signed_path(file_path: str) -> str:
    """ Change file extension to .sig """
    file, ext = os.path.splitext(file_path)
    return file + '.sig'


def get_file_key_path(file_path):
    """ Change file extension to .bin """
    file, ext = os.path.splitext(file_path)
    return file + '.bin'
