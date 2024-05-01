import tarfile
from os import listdir
import json
import docx

from docudraft.template.template_package import TemplatePackage
from docudraft.user.data.wordmap import WordMap
from docudraft.user.data.key import Key
from docudraft.template.template import Template
from docudraft.exceptions import FileTypeError


def create_template_package_file(template_dir: str, template_data: str, file_name: str = None) -> None:
    if file_name is None:
        file_name = json.load(open(template_data))['name']
    f = tarfile.open(file_name + '.dxtp', "w")
    f.add(template_data, arcname='tdata.json')

    # docx files
    files = listdir(template_dir)
    for i in files:
        if i[-5:] == '.docx':
            f.add(template_dir + i, arcname='template/' + i)

    f.close()


def load_template_package(template_package_tar: str) -> TemplatePackage:
    f = tarfile.open(template_package_tar)
    m = f.getmembers()

    tdata = json.load(f.extractfile(f.getmember('tdata.json')))
    templates = []

    for i in m:
        if i.path.split('/')[0] == 'template':
            templates.append(Template(document=docx.Document(f.extractfile(i)), name=i.path.split('/')[1]))

    tp = TemplatePackage(tdata['name'], tdata['description'], templates, Key(tdata['key']), WordMap(tdata['word_map']))

    return tp
