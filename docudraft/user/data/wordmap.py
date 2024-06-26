class WordMap:
    word_map: dict[str, str]

    def __init__(self, word_map: dict[str, str] = None):
        if word_map is None:
            word_map = {}
        self.word_map = word_map

    def add_pair(self, wildcard: str, word: str) -> None:
        self.word_map[wildcard] = word

    def get_data(self):
        return self.word_map.copy()
