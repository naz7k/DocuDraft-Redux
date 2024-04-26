class FileTypeError(Exception):

    def __init__(self, message='Incorrect File Type'):
        super().__init__(message)