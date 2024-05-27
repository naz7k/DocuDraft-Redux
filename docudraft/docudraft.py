import docudraft.user.interfaces.cli as cli
import docudraft.user.interfaces.ddgui as gui
from docudraft.instance import Instance
from docudraft.__version__ import __version__

import argparse as ap


if __name__ == '__main__':
    parser = ap.ArgumentParser(description="Simple document drafting program.")
    parser.add_argument('-c', '--cli', help='Launch with the command-line interface', action='store_true')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    args = parser.parse_args()

    match args.cli:
        case True:
            cli.DocuDraftCLI(Instance()).cmdloop()
        case False:
            gui.App(Instance()).mainloop()


