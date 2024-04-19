from key import Key
from replacedata import *
from template import *
from replacer import *

if __name__ == '__main__':
    key = Key('<|')
    rd = ReplaceData(key)
    rd.add_pair('CORPORATION', 'TtestCorp123')
    rd.add_pair('OFFICE', 'address 2 2 2 3 L4W')
    rd.add_pair('PRESIDENT', 'naz')
    template = Template('./Templates/Corporate Summary.docx', 'Corporate Summary')
    replace(template, rd, './output/')