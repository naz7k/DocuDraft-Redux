import docudraft.user.interfaces.cli
from docudraft.instance import Instance

if __name__ == '__main__':
    docudraft.user.interfaces.cli.DocuDraftCLI(Instance()).cmdloop()
