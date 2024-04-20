from key import Key
from wordmap import *
from template import *
from replacer import *
from loader import *

if __name__ == '__main__':
    templates = load_templates()
    wm = load_word_map_json()
    for template in templates:
        replace(template, wm, './output/')