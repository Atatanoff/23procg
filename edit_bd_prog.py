from tkinter import *
from tkinter import ttk
import sqlite3


columns = ("name", "icon", "macros", "del")

def add_pro(win, frm, *arg):
    with sqlite3.connect("data/miniboard.db") as con:
        con.execute("INSERT INTO programs VALUES(NULL,?,?)", arg)
    frm.update()
    dismiss(win, frm)

def dismiss(window, com):
    window.grab_release()
    frm.update()
    window.destroy()
 
def click(frm):
    window = Toplevel()
    window.title("Добавление программы")
    window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window, frm)) # перехватываем нажатие на крестик
    frmw = ttk.Frame(window, padding=10)
    frmw.grid()
    ttk.Label(frmw, text="Название программы").grid(column=0, row=0)
    ttk.Label(frmw, text="Цвет").grid(column=1, row=0)
    entry_prog = ttk.Entry(frmw)
    entry_prog.grid(column=0, row=1)
    entry_color = ttk.Entry(frmw)
    entry_color.grid(column=1, row=1)
    add_button = ttk.Button(frmw, text="Добавить",
                             command=lambda: add_pro(window, frm, entry_prog.get(),
                             entry_color.get()))
    add_button.grid(column=0, row=3, columnspan=2, sticky='nesw')
    window.grab_set()       # захватываем пользовательский ввод

root = Tk()
root.title("Программы")

frm = ttk.Frame(root, padding=10)
frm.grid()

with sqlite3.connect("data/miniboard.db") as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS programs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color TEXT NOT NULL
    )''')
    cur.execute("SELECT name, color FROM programs")
    prg = cur.fetchall()

prg_var = StringVar(value=prg[0][0] if prg else "добавьте программу")

combobox = ttk.Combobox(frm,textvariable=prg_var, values=[v[0]for v in prg], state="readonly")
combobox.grid(column=0, row=0)

def del_prog(root, name):
    with sqlite3.connect("data/miniboard.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM programs WHERE name = ?", (name,))
    root.update()
    

ttk.Button(frm, text="Добавить программу", command=lambda:click(root)).grid(column=1, row=0)
ttk.Button(frm, text="Удалить программу", command=lambda: del_prog(root, combobox.get())).grid(column=2,row=0)

tree = ttk.Treeview(frm,columns=columns, show="headings")
tree.grid(column=0,row=1)
# определяем заголовки
tree.heading("name", text="Имя", anchor=W)
tree.heading("icon", text="Иконка", anchor=W)
tree.heading("macros", text="Макрос", anchor=W)
tree.heading("del", text="")

tree.column('#4', stretch=NO, width=30)

def add_macros():
    pass

ttk.Button(frm, text="Добавить макрос", command=add_macros).grid(column=1, row=1, columnspan=2, sticky='we')

# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
 
root.mainloop()