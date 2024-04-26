from os import listdir
import json

from user.data.wordmap import WordMap
from user.data.key import Key
from template import Template
from exceptions import FileTypeError


def load_templates(template_dir: str = './Templates/', template_data: str = './Templates/TemplateData.json') -> list[Template]:
    """
    Loads the templates in the provided directory. Requires a TemplateData.json file indicating the key.
    :param template_dir: The directory in which all templates reside.
    :param template_data: The directory of the template data file within the template_dir.
    :return: A list of template objects.
    """
    td = open(template_data)
    template_data = json.load(td)

    files = listdir(template_dir)
    templates = []

    for i in files:
        try:
            templates.append(Template(template_dir + i, i, Key(template_data["key"])))
        except FileTypeError:
            continue

    return templates


def load_word_map_json(word_map_file: str = 'WordMap.json') -> WordMap:
    """
    Loads the word map mapping wildcards to words to be filled.
    :param word_map_file: Location of Word Map file.
    :return: Word Map object containing mappings.
    """
    wmf = open(word_map_file)
    word_map_dict = json.load(wmf)
    word_map = WordMap(word_map_dict)
    return word_map
