from key import Key


class Wildcard:
    """
        Represents a string to be replaced upon program execution.
    """

    key: Key

    word: str

    def __init__(self, key: Key, word: str):
        self.key = key
        self.word = word

    def get_wildcard(self) -> str:
        return self.key.get_code() + self.word

