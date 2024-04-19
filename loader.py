from template import *
from os import listdir


def load_templates(self, template_dir='./Templates') -> list[Template]:
    files = listdir(template_dir)
    templates = []

    for i in files:
        try:
            templates.append(Template(i, i))
        except FileTypeError:
            continue

    return templates
