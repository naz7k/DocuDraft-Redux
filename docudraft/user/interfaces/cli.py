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
        print("%s document(s) drafted successfully." % self.instance.run())

    def do_set(self, setting, path):
        """Change the location of templateDir, templateData, wordMapFile
            usage: set setting path"""
        self.instance.set_settings(setting, path)

    def do_see(self, setting):
        """See the current  of templateDir, templateData, wordMapFile
            usage: see setting"""
        print(self.instance.get_settings(setting))
