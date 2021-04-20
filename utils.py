import argparse
import os
from datetime import datetime


working_dir = 'work'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Process commands: create, delete, read, get_meta')

    parser.add_argument('-c', '--command', required=True, help='command to be executed')
    parser.add_argument('-n', '--file_name', required=True, help='file name')
    parser.add_argument('-e', '--extra', required=False, nargs='+', help='extra argument')

    return parser.parse_args()


def check_work_dir():
    if os.path.exists(working_dir):
        print("working dir exists")
    else:
        os.mkdir(working_dir)
        print("working dir created")


def create(file_name, extra):
    file_to_create = os.path.join('.', working_dir, file_name)
    if os.path.exists(file_to_create):
        print('Can not create {} cause file existed'.format(file_name))

    with open(file_to_create, 'w') as f:
        if extra:
            for line in extra:
                f.write(line + '\n')
        else:
            f.write('bla-bla-bla')


def remove(file_name):
    try:
        file_to_remove = os.path.join('.', working_dir, file_name)
        os.remove(file_to_remove)
    except OSError as e:
        print('Can not remove {} cause {}'.format(file_name, e.strerror))


def read(file_name):
    try:
        file_to_read = os.path.join('.', working_dir, file_name)

        with open(file_to_read, 'r') as f:
            for line in f:
                print(line)
    except IOError as ioe:
        print('Can not read {} cause {}'.format(file_name, ioe.strerror))


def get_meta(file_name):
    try:
        file_to_get_meta = os.path.join('.', working_dir, file_name)

        size = os.path.getsize(file_to_get_meta)
        atime = datetime.fromtimestamp(os.path.getatime(file_to_get_meta))
        ctime = datetime.fromtimestamp(os.path.getctime(file_to_get_meta))
        mtime = datetime.fromtimestamp(os.path.getmtime(file_to_get_meta))

        print('size: {} bytes\natime: {}\nctime: {}\nmtime: {}'.format(size, atime, ctime, mtime))
    except IOError as ioe:
        print('Can not get metadata {} cause {}'.format(file_name, ioe.strerror))