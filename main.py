import utils
import file_service as fs

if __name__ == '__main__':
    args = utils.parse_args()
    fs.process(args.command, args.file_name, args.extra)
