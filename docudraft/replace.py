from docudraft.template.template import Template
from docudraft.user.data.key import Key
from docudraft.user.data.wordmap import WordMap
from docudraft.exceptions.FinishedSearching import FinishedSearching


# inspired by https://stackoverflow.com/a/24813382, adapted to work on text split over multiple runs
def search_and_replace(template: Template, word_map: WordMap, key: Key, output_dir: str) -> bool:
    """
    Replaces the words in a .docx document template as specified in the word map.
    :param template: Template object containing a loaded docx file, a key, and a name.
    :param word_map: An object containing a dictionary with keys to be replaced by values in the template.
    :param key: the key indicating wildcards in the templates
    :param output_dir: The directory in which the output doc should be saved.
    :return: True if the operation is successful.
    """
    doc = template.document

    # I am assuming a search term can't be divided into 2 paragraphs. If it is then may God have mercy on my code
    for paragraph in doc.paragraphs:
        for wildcard in word_map.get_data().keys():
            search_term = key.get_code() + wildcard
            if search_term in paragraph.text:
                n = 0  # keeps track of what character in the search term we are looking at
                start_run = -1
                start_index = -1

                try:
                    # runs through every character in every run
                    for i in range(len(paragraph.runs)):
                        for s in range(len(paragraph.runs[i].text)):
                            # if the character at i[s] is the #n^th character of the search term...
                            if paragraph.runs[i].text[s] == search_term[n]:
                                if n == 0:  # if it's the first character remember index
                                    start_run = i
                                    start_index = s
                                n += 1
                            else:
                                n = 0

                            if n == len(search_term):  # if we've reached this point the search term is found
                                if start_run == i:  # if it is located within one run
                                    paragraph.runs[i].text = paragraph.runs[i].text.replace(search_term,
                                                                                            word_map.get_data()[
                                                                                                wildcard])
                                # if it isn't :(
                                elif start_run < i:
                                    # 1: remove any bits of the search term from the first run
                                    paragraph.runs[start_run].text = paragraph.runs[start_run].text[:start_index]
                                    # 2: remove any bits of the search term from the last run
                                    paragraph.runs[i].text = paragraph.runs[i].text[s + 1:]
                                    # 3: remove search term segments from runs in-between
                                    for j in range(start_run + 1, i):
                                        paragraph.runs[j].text = ''
                                    # 4: insert word which replaces search term
                                    paragraph.runs[start_run].text += word_map.get_data()[wildcard]

                                n = 0
                                if search_term in paragraph.text:
                                    continue
                                else:
                                    raise FinishedSearching()
                except FinishedSearching:
                    continue

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for wildcard in word_map.get_data().keys():
                        paragraph_text = paragraph.text.replace(key.get_code() + wildcard,
                                                                word_map.get_data()[wildcard])
                        paragraph.text = paragraph_text

    doc.save(output_dir + template.name)

    return True
