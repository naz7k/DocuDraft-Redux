from abc import abstractmethod

from docudraft.instance import Instance


class UserInterface:

    instance: Instance

    @abstractmethod
    def __init__(self, instance: Instance):
        self.instance = instance
