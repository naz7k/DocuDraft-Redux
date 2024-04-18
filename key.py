class Key:
    """
        Stores a key indicating a wildcard
    """

    key: str

    def __init__(self, key: str):
        self.key = key

    def get_code(self) -> str:
        return self.key
