class CreateFileException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class ReadFileException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class RemoveFileException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class GetMetaDataException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class UnknownCommand(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
