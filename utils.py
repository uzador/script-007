import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Process commands: create, delete, read, get_meta')

    parser.add_argument('-c', '--command', required=True, help='command to be executed')
    parser.add_argument('-n', '--file_name', required=True, help='file name')
    parser.add_argument('-e', '--extra', required=False, nargs='+', help='extra argument')

    return parser.parse_args()
