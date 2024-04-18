from docx import Document


class Template:
    document: Document
    name: str

    def __init__(self, file: str, name : str):
        if file[len(file)-5:] != '.docx':
            raise Exception("File must be of format .docx (Word 2007 onwards)")

        self.document = Document(file)

        self.name = name
        if self.name[len(name)-5:] != '.docx':
            self.name += '.docx'

    def get_document(self) -> Document:
        return self.document

    def _save_template(self) -> None:
        self.document.save(self.name)