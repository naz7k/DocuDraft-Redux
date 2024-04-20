from fixedqueue import FixedQueue
from wordmap import WordMap
from template import Template


#based on https://stackoverflow.com/a/24813382
def replace(template: Template, word_map: WordMap, output_dir: str):
    doc = template.get_document()

    for paragraph in doc.paragraphs:
        for wildcard in word_map.get_data().keys():
            search_term = template.get_key().get_code() + wildcard
            if search_term in paragraph.text:
                index_st = 0
                start_run = -1

                try:
                    for i in range(len(paragraph.runs)):
                        for s in range(len(paragraph.runs[i].text)):
                            if paragraph.runs[i].text[s] == search_term[index_st]:
                                if index_st == 0:
                                    start_run = i
                                    start_index = s
                                index_st += 1
                            else:
                                index_st = 0

                            if index_st + 1 == len(search_term):
                                if start_run == i:
                                    paragraph.runs[i].text = paragraph.runs[i].text.replace(search_term, word_map.get_data()[wildcard])
                                elif start_run < i:
                                    paragraph.runs[start_run].text = paragraph.runs[start_run].text[:start_index] + word_map.get_data()[wildcard]

                                    for j in range(start_index+1, i):
                                        paragraph.runs[j].text = ''

                                    paragraph.runs[i].text = paragraph.runs[i].text[s:]

                                index_st = 0
                                if search_term in paragraph.text:
                                    continue
                                else:
                                    raise Exception("Done")
                except Exception:
                    continue




    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for wildcard in word_map.get_data().keys():
                        paragraph_text = paragraph.text.replace(template.get_key().get_code() + wildcard,
                                                                word_map.get_data()[wildcard])
                        paragraph.text = paragraph_text

    doc.save(output_dir + template.name)
