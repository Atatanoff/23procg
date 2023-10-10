
import customtkinter
import sqlite3
from PIL import Image, ImageTk
from customtkinter.windows.widgets.font import CTkFont
from loguru import logger

import utils.Utils as ut
import res



class ProgramWin(customtkinter.CTkToplevel):
    def __init__(self, id, value):
        super().__init__()
        self.id = id
        self.value = value
        self.put_widget()
    
    def put_widget(self):
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            title, color = cur.execute(
                "SELECT name, color FROM programs WHERE id=?",
                (self.id,)).fetchone()
                
            self.title(title)
        self.configure(bg='#1C1D21')
        self.geometry("400x300")
        self.configure(fg_color='#444444')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        Scroll(self, self.id, self.value, color).grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

class Scroll(customtkinter.CTkScrollableFrame):
    def __init__(self, master: any, id, value, color):
        super().__init__(master)
        self.id = id
        self.master = master
        self.color = color
        self.macros = None
        from utils.value import Value
        self.value: Value = value
        self.put_widget()

    def put_widget(self):
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            macros_list = cur.execute(
                "SELECT name, icon_id, macros FROM macros WHERE program_id=?",
                (self.id,)).fetchall()
            r = 0
            for name, icon_id, macros in macros_list:
                #заполняем параметры нажатой кнопки в валуе
                self.value.color_button = self.id
                self.value.name_button = name
                self.value.image_button = icon_id

                self.macros = "+" + macros
                image = None
                if isinstance(icon_id, int):
                    icon = cur.execute(
                        "SELECT icons, mode, width, hight FROM icons WHERE id=?",
                        (icon_id,)).fetchone()
                    image = customtkinter.CTkImage(
                        Image.frombytes(icon[1], (icon[2], icon[3]), icon[0]))
                button = customtkinter.CTkButton(
                    self,image = image, text=name, width=40,height=50,
                                    compound='left', fg_color = "transparent",
                                      command=self.send_macros)
                button.grid(row=r, column=0)
                customtkinter.CTkLabel(self, text=macros).grid(row=r,column=1)
                r+=1

    def send_macros(self, *arg):
        #доделать посмотреть при обычном сохранении обновляется окно или нет, сейчас уже это не нужно
        ut.savemacro(self.value, self.macros)
        self.master.destroy()