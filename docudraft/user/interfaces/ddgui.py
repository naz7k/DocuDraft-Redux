import customtkinter as ctk
from docudraft.__version__ import __version__


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button1 = ctk.CTkButton(self, text="Button 1", width=90)
        self.button1.grid(row=0, column=0, sticky='nsew')

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.title('DocuDraft v.%s GUI' % __version__)
        self.geometry('1280x720')
        self.resizable(width=True, height=True)

        self.grid_columnconfigure(index=0, weight=0, minsize=100)
        self.grid_columnconfigure(index=1, weight=1)

        self.grid_rowconfigure(index=0, weight=10)

        self.sidebar = Sidebar(self, fg_color=("#2CC985", "#2FA572"), width=90)
        self.sidebar.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')

        self.main_elements = ctk.CTkFrame(self)
        self.main_elements.grid(row=0, column=1, padx=0, pady=0, sticky='nswe')


app = App()
