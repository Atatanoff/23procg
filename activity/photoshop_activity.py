from typing import Optional, Tuple, Union
import customtkinter

import utils.Utils as ut


class ProgramWin(customtkinter.CTkToplevel):
    def __init__(self, id):
        super().__init__()
        self.title('Photoshop')
        self.configure(bg='#1C1D21')
        self.geometry("400x300")
        self.configure(fg_color='#444444')
        print(id)