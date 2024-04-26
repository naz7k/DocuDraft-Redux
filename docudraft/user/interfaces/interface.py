from abc import abstractmethod

from docudraft.__version__ import __version__

class UserInterface:

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def get_input(self):
        raise NotImplementedError

    @abstractmethod
    def send_command(self, command: str):
        raise NotImplementedError