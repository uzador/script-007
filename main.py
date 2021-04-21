import utils
import file_service

if __name__ == '__main__':
    args = utils.parse_args()
    file_service.process(args.command, args.file_name, args.extra)
