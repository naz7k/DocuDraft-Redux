from docx import Document


class Template:
    document: Document
    name: str

    def __init__(self, document: Document, name: str):
        self.document = document

        self.name = name
        if self.name[-5:] != '.docx':
            self.name += '.docx'

    @classmethod
    def from_path(cls, file_path: str, name: str):
        return cls(Document(file_path), name)
