import docudraft.loader as loader
import docudraft.replace as replace
import docudraft.defaults as defaults


class Instance:
    template_dir: str
    template_data: str
    word_map_file: str
    output_dir: str

    def __init__(self):
        self.template_dir = defaults.TEMPLATE_DIR
        self.template_data = defaults.TEMPLATE_DATA
        self.word_map_file = defaults.WORD_MAP
        self.output_dir = defaults.OUTPUT_DIR

    def set_settings(self, setting, path):
        match setting:
            case 'templateDir':
                self.template_dir = path
            case 'templateData':
                self.template_data = path
            case 'wordMapFile':
                self.word_map_file = path
            case 'outputDir':
                self.output_dir = path

    def get_settings(self, setting) -> str:
        match setting:
            case 'templateDir':
                return self.template_dir
            case 'templateData':
                return self.template_data
            case 'wordMapFile':
                return self.word_map_file
            case 'outputDir':
                return self.output_dir

    def run(self) -> int:
        """
        Runs the program, outputs drafted docs.
        :return: Number of successfully drafted documents.
        """
        templates = loader.load_templates(template_dir=self.template_dir, template_data=self.template_data)
        wm = loader.load_word_map_json(word_map_file=self.word_map_file)

        draft_num = 0
        for template in templates:
            if replace.replace(template, wm, self.output_dir):
                draft_num += 1
        return draft_num
