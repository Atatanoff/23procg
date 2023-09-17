from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3

from PIL import Image
import customtkinter

from loguru import logger

bd = "mb.db"

def dismiss(window, *arg):    
    main_win = window.main_win
    window.grab_release
    window.destroy()
    if main_win: main_win.refresh(*arg)

class App(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Программы")

        self.put_frames(None)

    def put_frames(self, arg):
        self.head = FrameH(self, arg).grid(column=0, row=0, sticky='nswe')
        self.bottom = FrameB(self, arg).grid(column=0, row=1, sticky='nswe')

    def refresh(self, *arg):
        for el in [el for el in self.children]:
            self.nametowidget(el).destroy()
        self.put_frames(arg)

class FrameH(ttk.Frame):
    def __init__(self, master, arg) -> None:
        super().__init__(master)
        self.put_widget(arg)
    
    def put_widget(self, selected_prog):
        programs = [ v[0] for v in self.get_bd()]
        if not selected_prog:
            prg_var = programs[0] if programs else "добавьте программу"
        else: prg_var = selected_prog[0]
        self.combobox = ttk.Combobox(self, values=programs, state="readonly")
        self.combobox.grid(row=0, column=0)
        self.combobox.set(prg_var)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.master.refresh(self.combobox.get()))
        ttk.Button(self, text="Добавить программу", command=self.click).grid(row=0, column=1)
        ttk.Button(self, text="Удалить программу", command=self.del_pro).grid(row=0, column=2)

    @staticmethod
    def get_bd():
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM programs")
            return cur.fetchall()

    def click(self):
        Windows(FrameWinPro, "Добавление программы", self.master)

    def del_pro(self):
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM programs WHERE name = ?", (self.combobox.get(),))
        self.master.refresh()
                
class FrameWinPro(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.put_widget()

    def put_widget(self):
        ttk.Label(self, text="Название программы").grid(column=0, row=0)
        ttk.Label(self, text="Цвет").grid(column=1, row=0)
        self.entry_prog = ttk.Entry(self)
        self.entry_prog.grid(column=0, row=1)
        self.entry_color = ttk.Entry(self)
        self.entry_color.grid(column=1, row=1)
        add_button = ttk.Button(self, text="Добавить",
                                command=self.add_pro)
        add_button.grid(column=0, row=3, columnspan=2, sticky='nesw')
    
    def add_pro(self):
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO programs VALUES(NULL,?,?)", (self.entry_prog.get(),
                                                                   self.entry_color.get()))
        dismiss(self.master)       

class FrameB(ttk.Frame):
    def __init__(self, master, arg) -> None:
        super().__init__(master)
        self.columns = ("name", "icon", "macros", "del")
        self.put_widget(arg)
    
    def put_widget(self, prog):
        ttk.Button(self, text="Добавить макрос", command=self.add_macros).grid(column=0, row=0,columnspan=2, sticky='we')
        tree = ttk.Treeview(self,columns=self.columns, show="headings")
        tree.grid(column=0,row=1)
        # определяем заголовки
        tree.heading("name", text="Имя", anchor=W)
        tree.heading("icon", text="Иконка", anchor=W)
        tree.heading("macros", text="Макрос", anchor=W)
        tree.heading("del", text="")
        tree.column('#4', stretch=NO, width=30)       

        # добавляем вертикальную прокрутку
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="ns")
        #доделать
        if prog:
            with sqlite3.connect(f"data/{bd}") as con:
                cur = con.cursor()
                id_prog = cur.execute("SELECT id FROM programs WHERE name=?", prog).fetchone()
                macros = cur.execute("SELECT name, icon_id, macros FROM macros WHERE program_id=?", id_prog).fetchall()
                
    def add_macros(self):
        Windows(FrameWinMac, "Добавление макроса", self.master)
        
class Windows(Toplevel):
    def __init__(self, frame, name, main_win) -> None:
        super().__init__()
        self.main_win = main_win        
        self.title(name)
        self.protocol("WM_DELETE_WINDOW", lambda: dismiss(self))
        self.frame = frame(self)
        self.frame.grid()
        self.wait_visibility()
        self.grab_set()       # захватываем пользовательский ввод

class FrameWinMac(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.icon_img = None
        self.name = None
        self.put_widget()

    def put_widget(self):
        self.error_label = ttk.Label(self, text='У кнопки может быть или имя или иконка')
        self.error_label.grid(column=0, row=0, columnspan=3)
        ttk.Label(self, text="Имя кнопки").grid(column=0, row=1)
        ttk.Label(self, text="Иконка").grid(column=1, row=1)
        ttk.Label(self, text="Макрос").grid(column=2, row=1)
        chek = self.register(self.clear_icon,)
        self.entry_name = ttk.Entry(self, validate="focus", validatecommand=chek)
        self.entry_name.grid(column=0, row=2)
        self.button_add_icon = customtkinter.CTkButton(self, text="добавить иконку", command=self.add_icon,
                                                        compound='left', fg_color = "transparent" )
        self.button_add_icon.grid(column=1, row=2)
        self.entry_macros = ttk.Entry(self)
        self.entry_macros.grid(column=2, row=2)
        add_button = ttk.Button(self, text="Добавить в бд",
                                command=self.add_in_bd)
        add_button.grid(column=0, row=3, columnspan=3, sticky='nesw')       

    def add_icon(self):       
        Windows(IconFrame, "Выбор иконки", self)

    def refresh(self, *arg):
        if arg:
            with sqlite3.connect(f"data/{bd}") as con:
                cur = con.cursor()
                data = cur.execute("SELECT * FROM icons WHERE id = ?", arg).fetchall()[0]
        
            image = customtkinter.CTkImage(Image.frombytes(data[2], (data[3], data[4]), data[1]))
            self.button_add_icon.destroy()
            self.button_add_icon = customtkinter.CTkButton(self, text="добавить иконку",image=image, command=self.add_icon,
                                                            compound='left', fg_color = "transparent" )
            self.button_add_icon.grid(column=1, row=1)
            self.entry_name.delete(0,END)
        #доделать
    def add_in_bd(self):
        macros = self.entry_macros.get()
        name = self.entry_name.get()
        id_prog = None
        id_icon = None
        if macros and (name or id_icon):
            name = self.entry_name.get()
            if not name:
                name = None
        else: self.error_label.configure(text="Что-то забыл ввести", foreground="red")
               
        # with sqlite3.connect("data/miniboard.db") as con:
        #     cur = con.cursor()
            #cur.execute("INSERT INTO programs VALUES(NULL,?,?)",)

    def clear_icon(self):
        self.button_add_icon.destroy()
        self.button_add_icon = customtkinter.CTkButton(self, text="добавить иконку", command=self.add_icon,
                                                        compound='left', fg_color = "transparent" )
        self.button_add_icon.grid(column=1, row=1)

class IconFrame(ttk.Frame):
    def __init__(self, master: Windows):
        super().__init__(master)
        self.put_widget()

    def put_widget(self):
        FrameIconTop(self).grid(column=0, row=0, sticky='nswe')
        ttk.Separator(self).grid(column=0, row=1, sticky='nswe')
        self.but_icon = FrameIconBottom(self)
        self.but_icon.grid(column=0, row=2, sticky='nswe')

    def refresh(self, *arg):
        self.but_icon.destroy()
        self.but_icon = FrameIconBottom(self)
        self.but_icon.grid(column=0, row=2, sticky='nswe')

class FrameIconTop(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        Button(self, text="загрузить иконку в бд...", command=self.add_icon_in_bd).grid()
    
    def add_icon_in_bd(self):
        file_path = filedialog.askopenfilename()
        icon_img = convert_to_binary_data(file_path)
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO icons VALUES(NULL,?,?,?,?)", icon_img)
        self.master.refresh()

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат, возвращает blob, цыет.режим, высоту, ширину
    img = Image.open(filename)
    mode = img.mode
    size = img.size
    return (sqlite3.Binary(img.tobytes()), mode, size[0], size[1])

class FrameIconBottom(ttk.Frame):
    def __init__(self, master: IconFrame) -> None:
        super().__init__(master)       

        Label(self, text="Список загруженных иконок, чтоб добавить к макросу, нажать на иконку").grid(column=0,row=0, columnspan=2)
        self.put_widget()


    def put_widget(self):
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM icons").fetchall()
            for num, el in enumerate(data, 1):
                image = customtkinter.CTkImage(Image.frombytes(el[2], (el[3], el[4]), el[1]))

                bt = customtkinter.CTkButton(master=self, command=lambda id=el[0]: dismiss(self.master.master, id), image = image, text="Выбрать", width=40, height=50,
                                 compound='left', fg_color = "transparent" )
                bt.grid(column = 0, row = num)
                del_bt = Button(self, text="удалить", command=lambda bt=bt, id=el[0]: self.del_icon(bt, del_bt, id))
                del_bt.grid(column=1, row=num)
    
    def del_icon(self, bt: customtkinter.CTkButton, delbt: Button, id):
        with sqlite3.connect(f"data/{bd}") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM icons WHERE id = ?", (id,))
        bt.destroy()
        delbt.destroy()
        self.master.refresh()
        

app = App()
app.mainloop()
