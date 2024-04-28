from cmd import Cmd
import sys

from docudraft.__version__ import __version__
from docudraft.instance import Instance
from .interface import UserInterface


class DocuDraftCLI(Cmd, UserInterface):
    prompt = '>> '
    intro = 'DocuDraft Version %s CLI.    Type help or ? to list commands.' % __version__

    def __init__(self, instance: Instance):
        super().__init__()
        super(Cmd, self).__init__(instance)

    def do_run(self, arg):
        """Run the program with the defined settings."""
        self.instance.run()
        return

    def do_set(self, setting, pointer):
        """Change the location of templateDir, templateData, wordMapFile"""
        match setting:
            case 'templateDir':
                self.instance.template_dir = pointer
            case 'templateData':
                self.instance.template_data = pointer
            case 'wordMapFile':
                self.instance.word_map_file = pointer

