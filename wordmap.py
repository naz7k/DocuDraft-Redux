from key import Key


class WordMap:

    word_map: dict[str, str]
    key: Key

    def __init__(self, key: Key):
        self.word_map = {}
        self.key = key

    def add_pair(self, wildcard: str, word: str) -> None:
        self.word_map[wildcard] = word

    def get_data(self):
        return self.word_map.copy()

    def get_key(self) -> Key:
        return self.key
