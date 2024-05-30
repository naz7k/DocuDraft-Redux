from abc import abstractmethod
from typing import Union

import customtkinter as ctk
from customtkinter import filedialog
from docudraft.__version__ import __version__
from docudraft.instance import Instance
from docudraft.template.template import Template
from docudraft.template.template_package import TemplatePackage
from docudraft.user.data.wordmap import WordMap
from docudraft.user.interfaces.interface import UserInterface

default_font = ('Segoe UI', 15)
default_font_popup = ('Segoe UI', 10)
default_bold_font = ('Segoe UI Semibold', 15)
title_font = ('Segoe UI Semibold', 35)


class App(ctk.CTk, UserInterface):

    def __init__(self, instance: Instance):
        super().__init__()
        UserInterface.__init__(self, instance)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.title('DocuDraft v.%s GUI' % __version__)
        self.geometry('420x920')
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(index=0, weight=0)

        self.grid_rowconfigure(index=0, weight=0)

        self.editor = Editor(self, fg_color=("white", "white"), width=self.winfo_width(), height=self.winfo_height())
        self.editor.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')


class Editor(ctk.CTkScrollableFrame):
    master: App

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.grid_columnconfigure(index=0, weight=1, minsize=0)
        self.grid_columnconfigure(index=1, weight=1, minsize=0)

        self.grid_rowconfigure(index=0, weight=1, minsize=0)
        self.grid_rowconfigure(index=1, weight=3, minsize=0)
        self.grid_rowconfigure(index=2, weight=4, minsize=0)
        self.grid_rowconfigure(index=3, weight=4, minsize=0)
        self.grid_rowconfigure(index=4, weight=10, minsize=0)
        self.grid_rowconfigure(index=5, weight=3, minsize=0)

        self.title = ctk.CTkLabel(self, text='DocuDraft v.%s' % __version__, font=title_font)
        self.title.grid(row=0, column=0, sticky='nsew', padx=10, pady=10, columnspan=2)

        self.load_button = ctk.CTkButton(self, text="Load Template", command=self._load, font=default_font, height=40)
        self.load_button.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        self.settings_button = self.run_button = ctk.CTkButton(self, text="Settings", command=self._run, font=default_font)
        self.settings_button.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

        self.run_button = ctk.CTkButton(self, text="Run", command=self._run, font=default_font, height=40)
        self.run_button.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.info_frame = InfoBox(self,
                                  "Name: %s" % master.instance.loaded_template_package.name,
                                  'Description: %s' % master.instance.loaded_template_package.description,
                                  'Key: %s' % master.instance.loaded_template_package.key.key, height=100, width=100)
        self.info_frame.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=20, pady=10)

        self.doc_list = InfoBox(self, *(x.name for x in master.instance.loaded_template_package.template_package))
        self.doc_list.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=20, pady=10)

        self.input_frame = InputFrame(self, master.instance.loaded_template_package,
                                      height=50,
                                      width=200)
        self.input_frame.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=20, pady=10)

    def _load(self):
        file_path = filedialog.askopenfilename()
        self.master.instance.load_template_package(file_path)

        # debug
        print(file_path)
        print(self.master.instance.loaded_template_package.name)

        self.info_frame.reload("Name: %s" % self.master.instance.loaded_template_package.name,
                               'Description: %s' % self.master.instance.loaded_template_package.description,
                               'Key: %s' % self.master.instance.loaded_template_package.key.key)
        self.doc_list.reload(*(x.name for x in self.master.instance.loaded_template_package.template_package))
        self.input_frame.reload(self.master.instance.loaded_template_package)

    def _run(self):
        if self.master.instance.run():  # if program runs without errors, show a success popup
            self.after(100, self._success_popup)

    def _success_popup(self):
        success_popup = ctk.CTkToplevel(self.master)
        success_popup.geometry('360x160')
        success_popup.title('Status')
        success_popup.rowconfigure(index=0)
        success_popup.columnconfigure(index=0)
        message = ctk.CTkLabel(success_popup,
                               text='Documents drafted Successfully in:\n' + self.master.instance.output_dir,
                               font=default_font)
        message.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        success_popup.attributes('-topmost', 1)


class InfoBox(ctk.CTkFrame):
    info_text: list[ctk.CTkLabel]

    def __init__(self, master, *args: Union[str, tuple[str, str]], heading_font: ctk.CTkFont = default_bold_font,
                 font: ctk.CTkFont = default_font, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_propagate(True)

        self.font = font
        self.heading_text = []
        self.info_text = []

        self.grid_columnconfigure(index=0, weight=1, minsize=0)
        for i in range(0, len(args), 2):
            self.grid_rowconfigure(index=i, weight=0, minsize=0)
            self.grid_rowconfigure(index=i + 1, weight=0, minsize=0)
            if type(i) is tuple:
                info_title = ctk.CTkLabel(self, text=args[i][0], font=heading_font, height=0)
                info_text = ctk.CTkLabel(self, text=args[i][1], font=font, height=0)
                info_title.grid(column=0, row=i, sticky='sw', padx=5, pady=3)
                info_text.grid(column=0, row=i + 1, sticky='nw', padx=5, pady=3)  # TODO: Finish this!!!
                self.heading_text.append(info_title)
                self.info_text.append(info_text)
            else:
                info_text = ctk.CTkLabel(self, text=args[i], font=font, height=0)
                info_text.grid(column=0, row=i + 1, sticky='w', padx=5, pady=6)
                self.heading_text.append("")
                self.info_text.append(info_text)
            info_text.bind("<Configure>", self.wrap)
            # self.bind("<Configure>", self.__on_configure)

    def reload(self, *args: str):
        _reload_row_labels_frame(self, self.heading_text, self.info_text, args)
        self.wrap()

    def wrap(self, *args):
        for i in range(len(self.info_text)):
            self.info_text[i].configure(wraplength=self.winfo_width())


class InputFrame(ctk.CTkFrame):
    input_labels: list[ctk.CTkLabel]
    input_boxes: list[ctk.CTkTextbox]

    def __init__(self, master, template_package: TemplatePackage, font: ctk.CTkFont = default_font, **kwargs):
        super().__init__(master, **kwargs)

        self.font = font

        self.input_labels = []
        self.input_boxes = []

        self.grid_columnconfigure(index=0, weight=1, minsize=0)
        self.grid_columnconfigure(index=1, weight=3, minsize=0)

    def reload(self, template_package: TemplatePackage):
        index = 0
        long_names = []
        for i in template_package.word_map_names.word_map:
            self.grid_rowconfigure(index=index, weight=0, minsize=0)
            input_box = MappedTextbox(self, i, template_package.word_map.word_map, activate_scrollbars=False, width=0,
                                      height=0)
            input_box.grid(column=1, row=index, sticky='nsew', padx=2, pady=2)
            self.input_boxes.append(input_box)
            long_names.append(template_package.word_map_names.word_map[i])
            index += 1
        _reload_row_labels_frame(self, [], self.input_labels, long_names)

    def wrap(self, *args):
        for i in range(len(self.input_labels)):
            self.input_labels[i].configure(wraplength=self.input_labels[i].winfo_width())


class MappedTextbox(ctk.CTkTextbox):

    def __init__(self, master, name: str, mapped_dict: dict[str, str], **kwargs):
        super().__init__(master, **kwargs)
        self.mapped_dict = mapped_dict
        self.name = name
        self.bind("<KeyRelease>", self.update_word_map)

    def update_word_map(self, *args):
        self.mapped_dict[self.name] = self.get('1.0', "end").strip('\n')


class SettingsFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=1, weight=1)

        self.grid_columnconfigure(index=1, weight=1)

        self.output_label = ctk.CTkLabel(text="Output Folder", font=default_font)

def _reload_row_labels_frame(master: InfoBox, heading_list: list[ctk.CTkLabel], label_list: list[ctk.CTkLabel],
                             new_texts: Union[list[str], tuple[str, ...]]):  #TODO: finish!!!
    if len(new_texts) >= len(label_list):  # if new items are added to the infobox
        for i in range(len(new_texts)):
            if i < len(label_list):
                label_list[i].configure(text=new_texts[i])  # configure the existing labels to show new text
            else:
                master.grid_rowconfigure(index=i, weight=0, minsize=0)  # create new labels for new items
                info_text = ctk.CTkLabel(master, text=new_texts[i], font=master.font, height=0)
                info_text.grid(column=0, row=i, sticky='w', padx=5, pady=6)
                label_list.append(info_text)
                info_text.bind("<Configure>", master.wrap)

    else:  # if there are less items than existing labels
        for i in range(len(label_list)):
            if i < len(new_texts):  # while we are still in range of new items
                label_list[i].configure(text=new_texts[i])  # configure the existing labels to show new text
            else:
                label_list[i].configure(text="")  # once all new items added, clear existing text from extra labels

