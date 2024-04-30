from docudraft.template.template import Template
from docudraft.user.data.key import Key
from docudraft.user.data.wordmap import WordMap


class TemplatePackage:
    template_package: list[Template]
    key: Key
    word_map: WordMap

    def __init__(self, template_package: list[Template], key: Key, word_map: WordMap):
        self.template_package = template_package
        self.key = key
        self.word_map = word_map
