import os
import logging
import argparse
from config import WORKING_DIR


logging.basicConfig(level=logging.DEBUG, filename='server.log',
                    format='%(asctime)s %(levelname)s:%(message)s')


def parse_args():
    """ Parse incoming arguments:

    -c/--command -- executed command (create, delete, read, get_meta)
    -f/--file_name -- file to be processed by above command
    -c/--content -- content for command create
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


def check_working_dir():
    """ Checks if working dir exists and creates one otherwise """
    if os.path.exists(WORKING_DIR):
        logging.debug("working dir exists")
        return True
    else:
        os.mkdir(WORKING_DIR)
        logging.info("working dir created")
        return False


def build_path(file_name):
    """ Generic function to build file path """
    return os.path.join('.', WORKING_DIR, file_name)
