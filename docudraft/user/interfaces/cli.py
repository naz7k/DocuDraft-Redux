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
        if self.instance.run():
            print("Document(s) drafted successfully.")
        else:
            print("No template package loaded. Please try again.")

    def do_loadtp(self, path: str):
        """Load a template package of type .dxtp
        usage: loadtp <path>"""
        self.instance.load_template_package(path)

    def do_info(self, arg):
        """Show the current settings configuration"""
        try:
            print("Loaded template package: %s" % self.instance.loaded_template_package.name)
        except AttributeError:
            print("No Loaded Template Package!")
        print("Output directory: %s" % self.instance.output_dir)

    def do_modwm(self, args: str):
        """Modify or display the word map of the loaded template.
        usage: <wildcard>:<value>,<wildcard2>:<value2>,..."""
        kwargs = dict(item.split(':') for item in args.split(','))
        print(self.instance.modify_word_map(**kwargs).word_map)
