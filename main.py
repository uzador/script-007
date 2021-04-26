import utils
from file_service import FileService

if __name__ == '__main__':
    args = utils.parse_args()
    FileService.process(args.command, args.file_name, args.content)
