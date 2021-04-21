import os
import utils
from datetime import datetime


def create(file_name, extra):
    file_to_create = utils.build_path(file_name)
    if os.path.exists(file_to_create):
        print('Can not create {} cause file existed'.format(file_name))

    try:
        with open(file_to_create, 'w') as f:
            if extra:
                for line in extra:
                    f.write(line + '\n')
            else:
                f.write('empty file')
    except OSError as ose:
        print('Can not create {} cause {}'.format(file_name, ose.strerror))


def remove(file_name):
    try:
        file_to_remove = utils.build_path(file_name)
        os.remove(file_to_remove)
    except OSError as e:
        print('Can not remove {} cause {}'.format(file_name, e.strerror))


def read(file_name):
    try:
        file_to_read = utils.build_path(file_name)

        with open(file_to_read, 'r') as f:
            for line in f:
                print(line)
    except IOError as ioe:
        print('Can not read {} cause {}'.format(file_name, ioe.strerror))
    except OSError as ose:
        print('Can not read {} cause {}'.format(file_name, ose.strerror))


def get_meta(file_name):
    try:
        file_to_get_meta = utils.build_path(file_name)

        size = os.path.getsize(file_to_get_meta)
        atime = datetime.fromtimestamp(os.path.getatime(file_to_get_meta))
        ctime = datetime.fromtimestamp(os.path.getctime(file_to_get_meta))
        mtime = datetime.fromtimestamp(os.path.getmtime(file_to_get_meta))

        print('size: {} bytes\natime: {}\nctime: {}\nmtime: {}'
              .format(size, atime, ctime, mtime))
    except IOError as ioe:
        print('Can not get metadata {} cause {}'
              .format(file_name, ioe.strerror))
    except OSError as ose:
        print('Can not get metadata {} cause {}'
              .format(file_name, ose.strerror))


COMMANDS = {
    'create': create,
    'read': read,
    'remove': remove,
    'get_meta': get_meta,
}


def default_cmd(name):
    print('Unknown command: {}'.format(name))


def process(cmd, file_name, extra):
    utils.check_working_dir()
    cmd_to_execute = COMMANDS.get(cmd, default_cmd)
    if extra:
        cmd_to_execute(file_name, extra)
    else:
        cmd_to_execute(file_name)
