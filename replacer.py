from replacedata import ReplaceData
from template import Template


#based on https://stackoverflow.com/a/24813382
def replace(template: Template, replace_data: ReplaceData, output_dir: str):
    doc = template.get_document()
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            for wildcard in replace_data.get_data().keys():
                run_text = run.text.replace(replace_data.get_key().get_code() + wildcard, replace_data.get_data()[wildcard])
                run.text = run_text

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for run in cell.runs:
                    for wildcard in replace_data.get_data().keys():
                        run_text = cell.text.replace(replace_data.get_key().get_code() + wildcard, replace_data.get_data()[wildcard])
                        run.text = run_text
