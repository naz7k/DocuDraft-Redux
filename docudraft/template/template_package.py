from copy import deepcopy

from docudraft.template.template import Template
from docudraft.user.data.key import Key
from docudraft.user.data.wordmap import WordMap


class TemplatePackage:
    name: str
    description: str
    template_package: list[Template]
    key: Key
    word_map: WordMap
    word_map_names: WordMap

    def __init__(self, name: str, description: str, template_package: list[Template], key: Key, word_map_names: WordMap):
        self.name = name
        self.description = description
        self.template_package = template_package
        self.key = key
        self.word_map_names = word_map_names

        self.word_map = deepcopy(word_map_names)
        self.word_map.clear()
