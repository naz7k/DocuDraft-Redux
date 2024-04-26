import loader
import replace

def run(template_dir: str, template_data: str, word_map_file: str):
    templates = loader.load_templates(template_dir=template_dir, template_data=template_data)
    wm = loader.load_word_map_json(word_map_file=word_map_file)
    for template in templates:
        replace.replace(template, wm, '../output/')