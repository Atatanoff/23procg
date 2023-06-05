import tkinter
from tkinter import *
import tkinter.constants
from tkinter.messagebox import showinfo
import customtkinter
from tktooltip import ToolTip
import ctypes as ct
import time
import random
import os
import serial.tools.list_ports
from Utils import *


# def dark_title_bar(window):
#     window.update()
#     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
#     get_parent = ct.windll.user32.GetParent
#     hwnd = get_parent(window.winfo_id())
#     value = 2
#     value = ct.c_int(value)
#     set_window_attribute(hwnd, 20, ct.byref(value),4)

# велком текст
welcome_txt = {
    "morning": "Доброе утро",
    "afternoon": "Добрый день",
    "evening": "Добрый вечер",
    "night": "Доброй ночи",
    "awake": "Ты чё не спишь?"
}
t = time.localtime().tm_hour

time_of_day = "awake"
if 6 < t < 11:
    time_of_day = "morning"
elif 11 <= t < 16:
    time_of_day = "afternoon"
elif 16 <= t < 21:
    time_of_day = "evening"
elif 21 <= t < 24:
    time_of_day = "night"



#случайные высказывания
random_txt = (
    "work hard go pro",
    "Work is not a wolf, it will not run away into the forest",
    "Who does not work, he eats! Study student")


name_file = 'data.txt'
value = Value()
text_about = "Текст: 'О нас'"

# функция сохранения значния выбраной кнопки клавиатуры
 
def button_function(arg: str, bt, button):
    print(bt.winfo_name())
    value.key = arg
    if value.press_bt: value.press_bt.configure(fg_color='#FFFFFF')
    value.press_bt = bt
    
    if button.cget('state') == 'disabled':
        button.configure(state='active',fg_color='#B5F22F')
    
    bt.configure(fg_color='#8AB42F')


# функция загрузки из конфигурационного файла
def load_file(widg):
    
    if not os.path.isfile(value.file_name):
        
        f = open(value.file_name, 'w')
        f.close()
    with open(value.file_name, 'r') as f:        
        for el in f.readlines():            
            values = el.split()
            button = values[0]            
            
            name = values[1]
            
            value.d_name[button] = name
           
            text_bt = value.get_text_button(name)
            if not text_bt: text_bt = "Пусто"
            
            widg.nametowidget(button).configure(text=text_bt)

# ф-ция открытия ссылок из подвала

def open_link(url):
    webbrowser.open_new(url)


# главное окно
app = customtkinter.CTk()
app.title('ASPIS')
# app.iconbitmap('aspid.ico')
app.geometry("773x591")
# app.attributes('-alpha', 0.5)
app.resizable(False, False)
# app.overrideredirect(True)
app.configure(fg_color='#444444')
#dark_title_bar(app)
import webbrowser


# окна для готовыйх макрос наборов из различных программ
def Photoshop():
    # окно
    new_win_1 = customtkinter.CTkToplevel()
    #dark_title_bar(new_win_1)
    new_win_1.title('Photoshop')
    new_win_1.configure(bg='#1C1D21')
    new_win_1.geometry("400x300")
    new_win_1.configure(fg_color='#444444')


# Ячейки главного, я раскидал их по блокам
logobox = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
logobox.configure(width=175, height=107.4, corner_radius=0)
logobox.place(x=0, y=0)

menu = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
menu.configure(width=175, height=307, corner_radius=0)
menu.place(x=0, y=108)

fotter = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
fotter.configure(width=175, height=176, corner_radius=0)
fotter.place(x=0, y=415)

main = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
main.configure(width=598, height=374, corner_radius=0)
main.place(x=175, y=0)

nav = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
nav.configure(width=607, height=217, corner_radius=0)
nav.place(x=175, y=375)

# Надпись которая зависит от времяни открывания программы

hello = customtkinter.CTkLabel(main, text=welcome_txt[time_of_day], text_color="#FFFFFF", font=("Arial blod", 15))
hello.place(relx=.5, rely=.5, anchor="c")
# различные рандомные вырожения
hello = customtkinter.CTkLabel(nav, text=random.choice(random_txt), text_color="#777777", font=("blod", 10))
hello.place(relx=.5, rely=.5, anchor="c")

# Основня часть ввода клавишл

# ввод крутилок, сделал отдельным окном
def Enq_page(button):
    value.file_name = "Enq_page.txt"
    key_color = "#FFFFFF"
    key_hover = "#B5F22F"
    key_text_color = "#1C1D21"
    key_font = ("", 10)
    Enq_frame = customtkinter.CTkFrame(main, width=598, height=374, corner_radius=0, fg_color="#1C1D21")

    inf_text = customtkinter.CTkLabel(Enq_frame, text="крутить\nв лево", text_color="#777777", font=("blod", 10))
    inf_text.place(x=77, y=114)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="зажать и крутить\nв лево", text_color="#777777",
                                      font=("blod", 10))
    inf_text.place(x=55, y=239)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="нажатие\nна крутилку", text_color="#777777", font=("blod", 10))
    inf_text.place(x=159, y=124)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="крутить\nв право", text_color="#777777", font=("blod", 10))
    inf_text.place(x=265, y=114)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="зажать и крутить\nв право", text_color="#777777",
                                      font=("blod", 10))
    inf_text.place(x=240, y=239)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="крутить в верх", text_color="#777777", font=("blod", 10))
    inf_text.place(x=451, y=110)

    inf_text = customtkinter.CTkLabel(Enq_frame, text="крутить в низ", text_color="#777777", font=("blod", 10))
    inf_text.place(x=451, y=241)

    back_but = customtkinter.CTkButton(Enq_frame, command=key_page, text="вернутся", text_color="#FFFFFF",
                                       fg_color='#303135',
                                       hover_color="#515358", corner_radius=8, width=76, height=25,
                                       bg_color="#1C1D21")
    back_but.place(x=43, y=42)

    key22 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key22", key22, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key22.place(x=151, y=156)

    key23 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key23", key23, button), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key23.place(x=41, y=147)

    key24 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key24", key24, button), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key24.place(x=41, y=190)

    key25 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key25", key25, button), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key25.place(x=225, y=147)

    key26 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key26", key26, button), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key26.place(x=225, y=190)

    key27 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key27", key27, button), corner_radius=8, width=144, height=50,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key27.place(x=411, y=137)

    key28 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: button_function("key28", key28, button), corner_radius=8, width=144, height=50,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key28.place(x=411, y=190)

    load_file(Enq_frame)

    Enq_frame.place(x=0, y=0)


# ввод клавиш, также ентри код и бар готовых макросов
def key_page():                

    value.file_name = "key_page.txt"
    # менем выделение и цвет текста
    led_menu_but.configure(fg_color = "#1C1D21")
    key_menu_but.configure(fg_color = "#B5F22F")
    key_menu_but.configure(text_color="#1C1D21")
    led_menu_but.configure(text_color="#ffffff")
    
    # ввод клавишь -----------------------------------------------------------------------------------------------
    # набор для замены цветов, размера шрифта, итд сразу у всехх клавиш
    
    key_color = "#FFFFFF"
    key_hover = "#B5F22F"
    key_text_color = "#1C1D21"
    key_font = ("", 10)
    key_frame = customtkinter.CTkFrame(main, width=598, height=374, corner_radius=0, fg_color="#1C1D21")

    key0 = customtkinter.CTkButton(key_frame, text="", corner_radius=29, width=556, height=331, border_width=1,
                                   border_color="#444444",
                                   fg_color="#1C1D21", text_color="#1C1D21", hover_color="#1C1D21")
    key0.place(x=21, y=24)

    # кнопки для входа в меню энкодера
    Enq_key = customtkinter.CTkButton(key_frame, command=lambda:Enq_page(button), text=" ", corner_radius=105, width=70, height=70,
                                      fg_color="#EFEFEF", hover_color=key_hover)
    #print(Enq_key.winfo_name())
    Enq_key.place(x=42, y=38)

    Enq_key2 = customtkinter.CTkButton(key_frame, command=lambda:Enq_page(button), text=" ", corner_radius=5, width=160, height=40,
                                       fg_color="#EFEFEF", hover_color=key_hover)
    #print(Enq_key2.winfo_name())
    Enq_key2.place(x=145, y=55)

    # клавишы
    key1 = customtkinter.CTkButton(key_frame, command=lambda: button_function("$key18", key1, button), text="Пусто", corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key1.place(x=337, y=43)

    ToolTip(key1, msg="Ctrl+Alt+e | Ctrl+Alt+shift+e", delay=0, fg="#B5F22F", bg="#1C1D21")

    key2 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key19", key2, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key2.place(x=411, y=43)

    key3 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key20", key3, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key3.place(x=485, y=43)

    key4 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key1", key4, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key4.place(x=41, y=116)

    key5 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key5", key5, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key5.place(x=115, y=116)

    key6 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key6", key6, button),  corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key6.place(x=189, y=116)

    key7 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key9", key7, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key7.place(x=263, y=116)

    key8 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key10", key8, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key8.place(x=337, y=116)

    key9 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key14", key9, button), corner_radius=8, width=70, height=70,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key9.place(x=411, y=116)

    key10 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key21", key10, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key10.place(x=485, y=116)

    key11 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key2", key11, button), corner_radius=8, width=144, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key11.place(x=41, y=189)

    key12 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key7", key12, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key12.place(x=189, y=189)

    key13 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key11", key13, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key13.place(x=263, y=189)

    key14 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key12", key14, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key14.place(x=337, y=189)

    key15 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key15", key15, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key15.place(x=411, y=189)

    key16 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key17", key16, button), corner_radius=8, width=70, height=144,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key16.place(x=485, y=189)

    key17 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key3", key17, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key17.place(x=41, y=262)

    key18 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key4", key18, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key18.place(x=115, y=262)

    key19 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key8", key19, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key19.place(x=189, y=262)

    key20 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key13", key20, button), corner_radius=8, width=144, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key20.place(x=263, y=262)

    key21 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: button_function("$key16", key21, button), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key21.place(x=411, y=262)


    load_file(key_frame)

    key_frame.place(x=0, y=0)


    # окно для работы с кнопками
    entry_frame = customtkinter.CTkFrame(nav, width=607, height=217, corner_radius=0, fg_color="#1C1D21")

    # бар с готовыеми макрос наборами
    toolbar = customtkinter.CTkScrollableFrame(master=entry_frame, scrollbar_button_color="#303135", fg_color="#1C1D21",
                                               orientation="horizontal", width=556, height=51, corner_radius=0)
    toolbar.place(x=42, y=0)

    buttonPs = customtkinter.CTkButton(toolbar, command=Photoshop, text="Photoshop", corner_radius=12, width=90,
                                       height=51, fg_color="transparent", text_color="#777777",
                                       hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonPs.grid(row=0, column=0)
    buttonil = customtkinter.CTkButton(toolbar, text="illustrator", corner_radius=12, width=90,
                                       height=51, fg_color="transparent", text_color="#777777",
                                       hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonil.grid(row=0, column=1)
    buttonPp = customtkinter.CTkButton(toolbar, text="PremierPro", corner_radius=12, width=90,
                                       height=51, fg_color="transparent", text_color="#777777",
                                       hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonPp.grid(row=0, column=2)
    buttonC4D = customtkinter.CTkButton(toolbar, text="Cinema4D", corner_radius=12, width=90,
                                        height=51, fg_color="transparent", text_color="#777777",
                                        hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonC4D.grid(row=0, column=3)
    button3Ds = customtkinter.CTkButton(toolbar, text="3DsMax", corner_radius=12, width=90,
                                        height=51, fg_color="transparent", text_color="#777777",
                                        hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    button3Ds.grid(row=0, column=4)
    buttonBle = customtkinter.CTkButton(toolbar, text="Blender", corner_radius=12, width=90,
                                        height=51, fg_color="transparent", text_color="#777777",
                                        hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonBle.grid(row=0, column=5)
    buttonFig = customtkinter.CTkButton(toolbar, text="Figma", corner_radius=12, width=90,
                                        height=51, fg_color="transparent", text_color="#777777",
                                        hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonFig.grid(row=0, column=6)
    buttonFu = customtkinter.CTkButton(toolbar, text="Fusion 360", corner_radius=12, width=90,
                                       height=51, fg_color="transparent", text_color="#777777",
                                       hover_color="#303135", font=("", 11), border_color="#FFFFFF")
    buttonFu.grid(row=0, column=7)

    # ввод макросов
    label_1 = customtkinter.CTkLabel(entry_frame, text="введите макрос", text_color="#FFFFFF", justify=tkinter.LEFT)
    label_1.place(x=329, y=75)

    entry = customtkinter.CTkEntry(entry_frame, placeholder_text="желательно eng", placeholder_text_color="#474747",
                                   corner_radius=6, width=230, height=30, fg_color="#1C1D21", bg_color="#1C1D21",
                                   text_color='#FFFFFF', border_width=1, border_color="#777777")
    entry.place(x=329, y=103)

    # чекбоксы
    C = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=C, offvalue='', text_color="#B5F22F", text="Ctrl",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=45, y=78)

    A = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=A, offvalue='', text_color="#B5F22F", text="Alt",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=45, y=105)

    S = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=S, offvalue='', text_color="#B5F22F", text="Shift",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=45, y=132)

    T = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=T, offvalue='', text_color="#B5F22F", text="Tab",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=45, y=159)

    E = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=E, offvalue='', text_color="#B5F22F", text="Esc",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=142, y=78)

    B = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=B, offvalue='', text_color="#B5F22F", text="Bac",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=142, y=105)

    En = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=En, offvalue='', text_color="#B5F22F", text="Entr",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=142, y=132)

    D = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=D, offvalue='', text_color="#B5F22F", text="Del",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=142, y=159)

    F10 = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=F10, offvalue='', text_color="#B5F22F", text="F10",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=238, y=78)

    F11 = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=F11, offvalue='', text_color="#B5F22F", text="F11",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=238, y=105)

    Sp = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=Sp, offvalue='', text_color="#B5F22F", text="Space",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=238, y=132)

    Cm = StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=Cm, offvalue='', text_color="#B5F22F", text="Comm",
                                         fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                         bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                         border_width=1, corner_radius=3)
    checkbox.place(x=238, y=159)

    #namekey = "key0000"

    def ser_write(data):
        f_port = None
        print('Search...')
        ports = serial.tools.list_ports.comports()
        if not ports:
            print("Ports not found")
            print("Возможно нет СОМ портов или не установлены драйвера")
            return

        for port in ports:
            if port.pid: f_port = port
            print('Find port ' + port.device)

        if not f_port:
            print("Device not found")
            print("Проверьте правильность подключения устройства в порт и попробуйте еще раз")
            return

        ser = serial.Serial(f_port.device)

        if ser.isOpen():
            ser.close()

        ser = serial.Serial(f_port.device, 9600, timeout=1)
        ser.flushInput()
        ser.flushOutput()
        print('Connect ' + ser.name)

        ser.write(data.encode())
        print(data)
        print("Закрываю порт...")
        ser.close()

    # Работа чекбоксов
    def save():
        name = ""

        if (C.get()):
            name += "+Ctrl"
            C.set("")            

        if (A.get()):
            name += "+Alt"
            A.set("")            

        if (S.get()):
            name += "+Shift"
            S.set("")

        if (T.get()):
            name += "+Tab"
            T.set("")

        if (E.get()):
            name += "+Esc"
            E.set("")

        if (B.get()):
            name += "+Bac"
            B.set("")

        if (En.get()):
            name += "+Enter"
            En.set("")

        if (D.get()):
            name += "+Del"
            D.set("")

        if (F10.get()):
            name += "+F10"
            F10.set("")

        if (F11.get()):
            name += "+F11"
            F11.set("")

        if (Sp.get()):
            name += "+Space"
            Sp.set("")

        if (Cm.get()):
            name += "+Comm"
            Cm.set("")

        if entry.get():
            name += f"+{entry.get()}"

        dataToSend = value.key + name + ";"
        value.press_bt.configure(text=value.get_text_button(dataToSend))

        value.d_name[value.press_bt.winfo_name()] = dataToSend
        entry.delete(0, tkinter.constants.END)
        button.configure(state='disabled', fg_color='#66871E')
        value.press_bt.configure(fg_color='#FFFFFF') 
              

        with open(value.file_name, 'w') as f:
            for key in value.d_name:
                print(key, value.d_name[key], file=f)

               
        ser_write(dataToSend)
        

    # кнопка сохронить
    button = customtkinter.CTkButton(entry_frame, command=lambda: save(), text="Сохранить", text_color="#1C1D21",
                                     fg_color='#66871E',
                                     corner_radius=8, width=113, height=30, bg_color="#1C1D21",
                                     state="disabled")
    button.place(x=441, y=146)

    

    entry_frame.place(x=0, y=0)




# Смена лед подсветки -------------------------------------------------------------------------------------
def led_page():
    led_menu_but.configure(fg_color = "#B5F22F")
    key_menu_but.configure(fg_color = "#1C1D21")
    key_menu_but.configure(text_color="#ffffff")
    led_menu_but.configure(text_color="#1C1D21")
    # ввод клавишь -----------------------------------------------------------------------------------------------
    # цвета для всех клавиш
    workc= "#B5F22F" #цвет выбранный пользователем

    key_color = "#3F3F3F"
    key_hover = "#3F3F3F"
    key_text_color = "#3F3F3F"
    key_font = ("", 10)
    led_clr = "#3F3F3F"

    led_frame = customtkinter.CTkFrame(main, width=598, height=374, corner_radius=0, fg_color="#1C1D21")

    led0 = customtkinter.CTkButton(led_frame, text="", corner_radius=29, width=556, height=331, border_width=5,
                                   border_color=workc,
                                   fg_color="#1C1D21", text_color="#1C1D21", hover_color="#1C1D21")
    led0.place(x=21, y=24)

    # клавишы
    Enq_key = customtkinter.CTkButton(led_frame, text=" ", corner_radius=105, width=70, height=70,
                                      fg_color="#3F3F3F", hover_color="#3F3F3F")
    Enq_key.place(x=42, y=38)

    Enq_key2 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=5, width=160, height=40,
                                       fg_color="#3F3F3F", hover_color="#3F3F3F")
    Enq_key2.place(x=145, y=55)

    led1 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led1.place(x=337, y=43)

    led2 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led2.place(x=411, y=43)

    led3 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led3.place(x=485, y=43)

    led4 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led4.place(x=41, y=116)

    led5 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led5.place(x=115, y=116)

    led6 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led6.place(x=189, y=116)

    led7 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led7.place(x=263, y=116)

    led8 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led8.place(x=337, y=116)

    led9 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                   border_color=led_clr,
                                   fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led9.place(x=411, y=116)

    led10 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led10.place(x=485, y=116)

    led11 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=144, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led11.place(x=41, y=189)

    led12 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led12.place(x=189, y=189)

    led13 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led13.place(x=263, y=189)

    led14 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led14.place(x=337, y=189)

    led15 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led15.place(x=411, y=189)

    led16 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=144, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led16.place(x=485, y=189)

    led17 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led17.place(x=41, y=262)

    led18 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led18.place(x=115, y=262)

    led19 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led19.place(x=189, y=262)

    led20 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=144, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led20.place(x=263, y=262)

    led21 = customtkinter.CTkButton(led_frame, text="", corner_radius=8, width=70, height=70, border_width=5,
                                    border_color=led_clr,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    led21.place(x=411, y=262)

    led_frame.place(x=0, y=0)

    # выбор цвето и настройка подсветки -------------------------------------------------------------------------
    # рамки для цветовых ячеек "размер и цвет"
    cl_wid = 0
    cl_col = "#FFFFFF"

    tc = "#FFFFFF"
    bc = "#333333"
    hc = "#B5F22F"
    uc = "#303135"


    color_frame = customtkinter.CTkFrame(nav, width=607, height=217, corner_radius=0, fg_color="#1C1D21")

    led_effect = customtkinter.CTkSegmentedButton(color_frame, values=["     Градиент     ", "     Выстрел     ", "     Задержка     ", "      Импульс     "],
                                                          text_color=tc,fg_color=bc,unselected_color=uc,selected_color=hc,)
    led_effect.place(x=41, y=41)

    led_on_off = customtkinter.CTkButton(color_frame, text="Выкл\Вкл", text_color="#333333",
                                            fg_color="#FFFFFF",
                                            hover_color="#B5F22F", corner_radius=6, width=101, height=25,
                                            bg_color="#1C1D21")
    led_on_off.place(x=452, y=42)

    slider_1 = customtkinter.CTkSlider(color_frame,  from_=0, to=100,width=514,progress_color=tc,
                                       button_hover_color=workc,button_color=workc)
    slider_1.place(x=41, y=80)
    slider_1.set(50)

    # цветовые ячейки
    color1 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#FFB900", hover_color="#FFB900")
    color1.place(x=41, y=113)

    color2 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#FF8C00", hover_color="#FF8C00")
    color2.place(x=75, y=113)

    color3 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#CA5010", hover_color="#CA5010")
    color3.place(x=109, y=113)

    color4 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#DA3B01", hover_color="#DA3B01")
    color4.place(x=142, y=113)

    color5 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#E81123", hover_color="#E81123")
    color5.place(x=176, y=113)

    color6 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#EA005E", hover_color="#EA005E")
    color6.place(x=210, y=113)

    color7 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#E81123", hover_color="#E81123")
    color7.place(x=245, y=113)

    color8 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#EA005E", hover_color="#EA005E")
    color8.place(x=279, y=113)

    color9 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                     border_color=cl_col, fg_color="#E81123", hover_color="#E81123")
    color9.place(x=314, y=113)

    color10 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#EA005E", hover_color="#EA005E")
    color10.place(x=349, y=113)

    color11 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#C30052", hover_color="#C30052")
    color11.place(x=383, y=113)

    color12 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#E3008C", hover_color="#E3008C")
    color12.place(x=418, y=113)

    color13 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#BF0077", hover_color="#BF0077")
    color13.place(x=453, y=113)

    color14 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#C239B3", hover_color="#C239B3")
    color14.place(x=488, y=113)

    color15 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#9A0089", hover_color="#9A0089")
    color15.place(x=522, y=113)

    color16 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#0078D4", hover_color="#0078D4")
    color16.place(x=41, y=146)

    color17 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#0063B1", hover_color="#0063B1")
    color17.place(x=75, y=146)

    color18 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#8E8CD8", hover_color="#8E8CD8")
    color18.place(x=109, y=146)

    color19 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#6B69D6", hover_color="#6B69D6")
    color19.place(x=142, y=146)

    color20 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#8764B8", hover_color="#8764B8")
    color20.place(x=176, y=146)

    color21 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#744DA9", hover_color="#744DA9")
    color21.place(x=210, y=146)

    color22 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#B146C2", hover_color="#B146C2")
    color22.place(x=245, y=146)

    color23 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#881798", hover_color="#881798")
    color23.place(x=279, y=146)

    color24 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#B5F22F", hover_color="#B5F22F")
    color24.place(x=314, y=146)

    color25 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#D7F22F", hover_color="#D7F22F")
    color25.place(x=349, y=146)

    color26 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#F2EA2F", hover_color="#F2EA2F")
    color26.place(x=383, y=146)

    color27 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#FFFFFF", hover_color="#FFFFFF")
    color27.place(x=418, y=146)

    color28 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#B8C9E2", hover_color="#B8C9E2")
    color28.place(x=453, y=146)

    color29 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#B4DAB5", hover_color="#B4DAB5")
    color29.place(x=488, y=146)

    color30 = customtkinter.CTkButton(color_frame, text="", corner_radius=4, width=31, height=31, border_width=cl_wid,
                                      border_color=cl_col, fg_color="#FFE2BF", hover_color="#FFE2BF")
    color30.place(x=522, y=146)

    color_frame.place(x=0, y=0)  # конец окна


# кнопки меню ----------------------------------------------------------------------------------------------------

# 451
led_menu_but = customtkinter.CTkButton(menu, command=led_page, text="Подсветка", text_color="#ffffff",
                                       hover_color="#B5F22F", corner_radius=8, width=113, height=30, fg_color="#1C1D21")
led_menu_but.place(x=31, y=82)

# 140
key_menu_but = customtkinter.CTkButton(menu, command=key_page, text="Ввод макросов", text_color="#ffffff",
                                       hover_color="#B5F22F", corner_radius=8, width=113, height=30, fg_color="#1C1D21")
key_menu_but.place(x=31, y=42)
# подсказки
ToolTip(key_menu_but, msg="Замена функций клавишь", delay=0, fg="#B5F22F", bg="#1C1D21")
ToolTip(led_menu_but, msg="Замена цвета подсветки", delay=0, fg="#B5F22F", bg="#1C1D21")

# Подвал     ----------------------------------------------------------------------------------------------------
about = customtkinter.CTkLabel(fotter, text="О нас", text_color="#FFFFFF", justify=tkinter.LEFT, font=("", 9))
about.bind("<Button-1>", lambda event: showinfo(title="Информация", message=text_about))
about.place(x=32, y=33)

telega = customtkinter.CTkLabel(fotter, text="telegram", text_color="#7AA7FF", justify=tkinter.LEFT, font=("", 9))
telega.bind("<Button-1>", lambda event: open_link(r"https://t.me/shakirovnz"))
telega.place(x=32, y=58)

dprof = customtkinter.CTkLabel(fotter, text="dprofile", text_color="#7AA7FF", justify=tkinter.LEFT, font=("", 9))
dprof.bind("<Button-1>", lambda event: open_link(r"https://www.behance.net/shakirovnz"))
dprof.place(x=32, y=87)

procg = customtkinter.CTkLabel(fotter, text="23procg 2022", text_color="#FFFFFF", justify=tkinter.LEFT, font=("", 9))
procg.place(x=32, y=114)
ToolTip(procg, msg=":)", delay=0, fg="#FFFFFF", bg="#1C1D21")

app.mainloop()