import utils


def process(cmd, file_name, extra):
    utils.check_work_dir()

    if cmd == 'create':
        utils.create(file_name, extra)
    elif cmd == 'remove':
        utils.remove(file_name)
    elif cmd == 'read':
        utils.read(file_name)
    elif cmd == 'get_meta':
        utils.get_meta(file_name)
    else:
        print('Unknown command: {}'.format(cmd))
