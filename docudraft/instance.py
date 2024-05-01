import docudraft.loader as loader
import docudraft.replace as replace
import docudraft.defaults as defaults


class Instance:
    template_dir: str
    template_data: str
    output_dir: str

    def __init__(self):
        self.template_dir = defaults.TEMPLATE_DIR
        self.template_data = defaults.TEMPLATE_DATA
        self.output_dir = defaults.OUTPUT_DIR

    def set_io_settings(self, setting, path):
        match setting:
            case 'templateDir':
                self.template_dir = path
            case 'templateData':
                self.template_data = path
            case 'outputDir':
                self.output_dir = path

    def get_io_settings(self, setting) -> str:
        match setting:
            case 'templateDir':
                return self.template_dir
            case 'templateData':
                return self.template_data
            case 'outputDir':
                return self.output_dir


    def run(self) -> int:
        """
        Runs the program, outputs drafted docs.
        :return: Number of successfully drafted documents.
        """

        # TODO: choose template pack functionality
        templates = loader.load_template_package_from_raw_data(template_dir=self.template_dir, template_data=self.template_data)

        draft_num = 0
        for template in templates.template_package:
            if replace.search_and_replace(template, templates.word_map, templates.key, self.output_dir):
                draft_num += 1
        return draft_num
