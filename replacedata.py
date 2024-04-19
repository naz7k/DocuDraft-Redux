from key import Key


class ReplaceData:

    replace_data: dict[str, str]
    key: Key

    def __init__(self, key: Key):
        self.replace_data = {}
        self.key = key

    def add_pair(self, wildcard: str, word: str) -> None:
        self.replace_data[wildcard] = word

    def get_data(self):
        return self.replace_data.copy()

    def get_key(self) -> Key:
        return self.key
