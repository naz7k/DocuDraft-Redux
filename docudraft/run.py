import loader
import replace
import defaults

class Run:

    template_dir: str
    template_data: str
    word_map_file: str

    def __init__(self):
        self.template_dir = defaults.TEMPLATE_DIR
        self.template_data = defaults.TEMPLATE_DATA
        self.word_map_file = defaults.WORD_MAP

    def run(self) -> None:
        templates = loader.load_templates(template_dir=self.template_dir, template_data=self.template_data)
        wm = loader.load_word_map_json(word_map_file=self.word_map_file)
        for template in templates:
            replace.replace(template, wm, '../output/')