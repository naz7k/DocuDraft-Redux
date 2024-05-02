class FinishedSearching(Exception):

    def __init__(self, message='Document Search Complete'):
        super().__init__(message)
