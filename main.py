import logging
from server import utils
from server import fs
import server.exception as exception

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

COMMANDS = {
    'create': fs.create,
    'read': fs.read,
    'remove': fs.remove,
    'get_meta': fs.get_meta,
}


def default_cmd(cmd):
    """ Function to be called when incoming command is unknown """
    raise exception.UnknownCommand('Unknown command received')


def process(cmd, file_name, content):
    """ Handler to process incoming commands

    cmd: command name
    file_name: file name to be processed by command
    content: content of the file in case of create command
    """

    try:
        utils.check_working_dir()
        cmd_to_execute = COMMANDS.get(cmd, default_cmd)
        file_path = utils.build_path(file_name)
        if content:
            result = cmd_to_execute(file_path, content)
        else:
            result = cmd_to_execute(file_path)

        if result:
            logger.info(f'result = {result}')
    except exception.CreateFileException as ex:
        logger.error(f'CreateFileException: {ex.msg}')
    except exception.ReadFileException as ex:
        logger.error(f'ReadFileException: {ex.msg}')
    except exception.RemoveFileException as ex:
        logger.error(f'RemoveFileException: {ex.msg}')
    except exception.GetMetaDataException as ex:
        logger.error(f'GetMetaDataException: {ex.msg}')
    except exception.UnknownCommand as ex:
        logger.error(f'UnknownCommand: {ex.msg}')
    except Exception as ex:
        logger.error(f'Exception: {ex}')


if __name__ == '__main__':
    args = utils.parse_args()
    logger.info(f'command: {args.command}, file_name: {args.file_name}, content: {args.content}')

    process(args.command, args.file_name, args.content)
