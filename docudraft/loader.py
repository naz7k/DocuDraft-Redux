from os import listdir
import json

from docudraft.template.template_package import TemplatePackage
from docudraft.user.data.wordmap import WordMap
from docudraft.user.data.key import Key
from docudraft.template.template import Template
from docudraft.exceptions import FileTypeError


def create_template_package(template_dir: str, template_data: str) -> TemplatePackage:
    td = open(template_data)
    template_data = json.load(td)

    files = listdir(template_dir)
    templates = []

    for i in files:
        try:
            templates.append(Template(template_dir + i, i))
        except FileTypeError:
            continue

    tp = TemplatePackage(templates, Key(template_data["key"]), WordMap(template_data["word_map"]))

    return tp