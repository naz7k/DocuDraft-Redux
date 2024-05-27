import docudraft.loader as loader
import docudraft.replace as replace
import docudraft.defaults as defaults
from docudraft.template.template_package import TemplatePackage
from docudraft.user.data.key import Key
from docudraft.user.data.wordmap import WordMap


class Instance:
    loaded_template_package: TemplatePackage
    template_package_dir: str  # where to look for dxtp files, used for gui
    output_dir: str

    def __init__(self):
        self.template_package_dir = defaults.TEMPLATE_PACK_DIR
        self.output_dir = defaults.OUTPUT_DIR
        self.loaded_template_package = TemplatePackage("No Template Package Loaded", "", [], Key(""), WordMap({}))

    def load_template_package(self, dxtp_path: str) -> None:
        self.loaded_template_package = loader.load_template_package(dxtp_path)

    def run(self) -> bool:
        """
        Runs the program, outputs drafted docs.
        :return: True if operation is successful. Otherwise, returns false.
        """
        try:
            for template in self.loaded_template_package.template_package:
                if replace.search_and_replace(template, self.loaded_template_package.word_map,
                                              self.loaded_template_package.key, self.output_dir):
                    return True

        except AttributeError:
            return False

    def modify_word_map(self, **kwargs: str) -> WordMap:
        try:
            for i in kwargs:
                if i in self.loaded_template_package.word_map.word_map:
                    self.loaded_template_package.word_map.word_map[i] = kwargs[i]
            return self.loaded_template_package.word_map
        except AttributeError:
            return None