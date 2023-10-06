from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3
import re

from PIL import Image, ImageTk
import customtkinter

from loguru import logger

import os

import res


if not os.path.isfile(res.data):
    import data.create_db

def dismiss(window, *arg):    
    main_win = window.main_win
    window.grab_release
    window.destroy()
    if main_win: main_win.refresh(*arg)

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Программы")
        self.put_frames()

    def put_frames(self, select_prog = None):
        data_prog = self.get_bd()
        if data_prog and not select_prog:
            select_prog = data_prog[0][1]
        if select_prog:
            select_id = tuple(filter(lambda x: x[1]==select_prog, data_prog))[0][0]
            
        else: 
            select_prog = "Добавьте программу"
            select_id = None
        programs = [v[1] for v in data_prog]
        FrameH(self, select_prog, programs, select_id).grid(column=0, row=0, sticky='we', pady=20)
        FrameM(self, (select_id, select_prog)).grid(column=0, row=2, sticky='we', pady=20)
        FrameB(self, select_id, select_prog).grid(column=0, row=4, sticky='nswe', pady=20)

    def refresh(self, select_prog):
        for el in [el for el in self.children]:
            self.nametowidget(el).destroy()
        self.put_frames(select_prog)

    @staticmethod
    def get_bd():
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            cur.execute("SELECT id, name FROM programs")
            return cur.fetchall()

class FrameH(ttk.Frame):
    def __init__(self, master, select_prog, programs, select_id, *arg) -> None:
        super().__init__(master)
        self.select_prog = select_prog
        self.select_id = select_id
        self.programs = programs
        self.put_widget()
    
    def put_widget(self):
        self.combobox = ttk.Combobox(self, values=self.programs, state="readonly")
        self.combobox.grid(row=0, column=0)
        self.combobox.set(self.select_prog)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.master.refresh(self.combobox.get()))
        ttk.Button(self, text="Добавить программу...", command=self.add).grid(row=0, column=1)
        ttk.Button(self, text="Изменить программу...", command=self.change).grid(row=0, column=2)
        ttk.Button(self, text="Удалить программу", command=self.del_pro).grid(row=0, column=3)

    def add(self):
        Windows(FrameWinPro, "Добавление программы", self.master)
    
    def change(self):
        Windows(FrameWinPro, "Изменение программы", self.master, self.select_id)    
    
    
    def del_pro(self):
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM programs WHERE id = ?", (self.select_id,))
            cur.execute("DELETE FROM macros WHERE program_id = ?", (self.select_id,))
        self.master.refresh(None)
                
                
class FrameWinPro(ttk.Frame):
    def __init__(self, master, id=None, *arg):
        super().__init__(master)
        self.id = id
        self.put_widget()


    def put_widget(self):
        ttk.Label(self, text="Название программы").grid(column=0, row=0)
        ttk.Label(self, text="Цвет").grid(column=1, row=0)

        self.errormsg = StringVar()
        self.errorLab = ttk.Label(self, wraplength=250, textvariable=self.errormsg)
        self.errorLab.grid(column=0, row=2)

        self.entry_prog = ttk.Entry(self)
        self.entry_prog.grid(column=0, row=1)
        check = (self.register(self.is_valid), "%P")
        self.entry_color = ttk.Entry(self, validate="key", validatecommand=check)
        self.entry_color.grid(column=1, row=1)
        self.entry_color.insert(0, "#")
        add_button = ttk.Button(self, text="Изменить" if self.id else "Добавить",
                                command=self.add_pro)
        add_button.grid(column=0, row=3, columnspan=2, sticky='nesw')
        
        if self.id:            
            _, prg, clr = self.get_data()
            self.entry_prog.insert(0, prg)
            self.entry_color.insert(0, clr)
        

    def is_valid(self, newval):
        result=  re.match("^\#[0-9a-f]{0,6}$", newval) is not None
        
        if result and len(newval) in (4, 7):
            self.errormsg.set('')            
        else:
            self.errormsg.set('Формат цвета #xxx или #xxxxxx')
        return result


    def get_data(self):
        
        with sqlite3.connect(res.data) as con:
                    cur = con.cursor()
                    return cur.execute("SELECT * FROM programs WHERE id = ?", self.id).fetchone()
        

    
    def add_pro(self):
        add_prog = self.entry_prog.get()
        color = self.entry_color.get()
        if add_prog and color:
            if not self.id:
                with sqlite3.connect(res.data) as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO programs VALUES(NULL,?,?)", (add_prog,
                                                                        color))
            else:
                with sqlite3.connect(res.data) as con:
                    cur = con.cursor()
                    cur.execute("UPDATE programs SET VALUES(NULL,?,?)", (add_prog,
                                                                        color))
            dismiss(self.master, add_prog)   
          

class FrameB(ttk.Frame):
    def __init__(self, master, select_id, select_prog, *arg) -> None:
        super().__init__(master)
        self.columns = ("name", "macros", "del")
        self.select_id = select_id
        self.select_prog = select_prog
        self.put_widget()

    def put_widget(self):
        Button(self, text="Удалить выбранное", command=self.del_macros).grid(column=0, row=0, sticky="we")
        Button(self, text="Удалить всё", command=self.del_all).grid(column=1, row=0, sticky="we")
        self.tree = ttk.Treeview(self, columns=self.columns)
        self.tree.grid(column=0,row=1, columnspan=2)

        self.tree.heading("#0", text="Иконка")
        self.tree.heading("name", text="Имя", anchor=W)
        self.tree.heading("macros", text="Макрос", anchor=W)
        self.tree.heading("del", text="")
        self.tree.column('del', stretch=NO, width=30)       

        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky="ns")
        #
        if self.select_id:
            with sqlite3.connect(res.data) as con:
                cur = con.cursor()
                macros = cur.execute("SELECT icon_id, name, macros FROM macros WHERE program_id=?", (self.select_id,)).fetchall()
                for el in macros:
                    if el[0] != "NULL":
                        icon = cur.execute("SELECT mode, width, hight, icons FROM icons WHERE id=?",(el[0],)).fetchone()
                        
                        image = ImageTk.PhotoImage(Image.frombytes(icon[0], (icon[1], icon[2]), icon[3]).resize((10,10)))
                        name = ""
                        self.tree.insert("", END, image=image, values=(name, el[2]))
                        self.tree.__dict__[f"image{el[0]}"] = image
                                            
                    else: 
                        name = el[1]
                        self.tree.insert("", END, values=(name, el[2]))

    def del_all(self, *arg):
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM macros WHERE program_id = ?",
                            (self.select_id,))
        self.put_refresh() 

    def del_macros(self, *arg):
        for el in self.tree.selection():
            with sqlite3.connect(res.data) as con:
                cur = con.cursor()
                cur.execute("DELETE FROM macros WHERE macros = ? AND program_id = ?",
                             (self.tree.item(el)['values'][-1], self.select_id))
        
        self.put_refresh()    
    
    def put_refresh(self, *arg):
        for el in [el for el in self.children]:
            self.nametowidget(el).destroy()
        self.put_widget()
        
class Windows(Toplevel):
    def __init__(self, frame, name, main_win, *arg) -> None:
        super().__init__()
        self.main_win = main_win        
        self.title(name)
        self.protocol("WM_DELETE_WINDOW", lambda: dismiss(self, None))
        self.frame = frame(self, arg)
        self.frame.grid()
        self.wait_visibility()
        self.grab_set()       # захватываем пользовательский ввод
#доделать если нет программ и будет попытка записать макрос
class FrameM(ttk.Frame):
    def __init__(self, master, prog, *arg) -> None:
        super().__init__(master)
        self.id_icon = None
        self.id_prog = prog[0]
        self.prog = prog[1]
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
            with sqlite3.connect(res.data) as con:
                cur = con.cursor()
                data = cur.execute("SELECT * FROM icons WHERE id = ?", arg).fetchall()[0]
        
            self.id_icon = data[0]
            image = customtkinter.CTkImage(Image.frombytes(data[2], (data[3], data[4]), data[1]))
            self.button_add_icon.destroy()
            self.button_add_icon = customtkinter.CTkButton(self, text="добавить иконку",image=image, command=self.add_icon,
                                                            compound='left', fg_color = "transparent" )
            self.button_add_icon.grid(column=1, row=2)
            self.entry_name.delete(0,END)
   
    
    def add_in_bd(self):
        macros = self.entry_macros.get()
        name = self.entry_name.get()
        if macros and (name or self.id_icon):
            name = self.entry_name.get()
            if not name:
                name = None
            
            with sqlite3.connect(res.data) as con:
                cur = con.cursor()
                cur.execute('INSERT INTO macros VALUES(NULL,?,?,?,?)', (macros, name, self.id_icon, self.id_prog))
            self.master.refresh(self.prog)

        else: self.error_label.configure(text="Что-то забыл ввести", foreground="red")
        

    def clear_icon(self):
       
        self.id_icon = 'NULL'
        self.button_add_icon.destroy()
        self.button_add_icon = customtkinter.CTkButton(self, text="добавить иконку", command=self.add_icon,
                                                        compound='left', fg_color = "transparent" )
        self.button_add_icon.grid(column=1, row=2)

class IconFrame(ttk.Frame):
    def __init__(self, master: Windows, *arg):
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
    def __init__(self, master, *arg) -> None:
        super().__init__(master)
        Button(self, text="загрузить иконку в бд...", command=self.add_icon_in_bd).grid()
    
    def add_icon_in_bd(self):
        #доделать загрузку нескольких иконок
        file_path = filedialog.askopenfilename()
        icon_img = convert_to_binary_data(file_path)
        with sqlite3.connect(res.data) as con:
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
    def __init__(self, master: IconFrame, *arg) -> None:
        super().__init__(master)       

        Label(self, text="Список загруженных иконок, чтоб добавить к макросу, нажать на иконку").grid(column=0,row=0, columnspan=2)
        self.put_widget()


    def put_widget(self):
        with sqlite3.connect(res.data) as con:
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
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM icons WHERE id = ?", (id,))
        bt.destroy()
        delbt.destroy()
        self.master.refresh()
        
app = App()
app.mainloop()
