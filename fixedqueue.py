from typing import Any


class FixedQueue:

    length: int
    q: list[Any]

    def __init__(self, length: int):
        self.length = length
        q = []

    def add(self, value: Any) -> list[Any]:
        self.q = [value] + self.q[:self.length-1]
        return self.q

    def get(self, index: int) -> Any:
        return self.q[index]