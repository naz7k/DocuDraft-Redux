from docx import Document

from docudraft.exceptions import FileTypeError
from docudraft.user.data.key import Key


class Template:
    document: Document
    name: str

    def __init__(self, file: str, name: str):
        if file[len(file) - 5:] != '.docx':
            raise FileTypeError("File must be of format .docx (Word 2007 onwards)")

        self.document = Document(file)

        self.name = name
        if self.name[len(name) - 5:] != '.docx':
            self.name += '.docx'
