import tkinter
from tkinter import *
import tkinter.constants
from tkinter.messagebox import showinfo
import customtkinter
from tktooltip import ToolTip
import random
from PIL import ImageTk, Image

from utils.Utils import open_link, time_of_day
from utils.value import Value
from res import *
import activity


# def dark_title_bar(window):
#     window.update()
#     set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
#     get_parent = ct.windll.user32.GetParent
#     hwnd = get_parent(window.winfo_id())
#     value = 2
#     value = ct.c_int(value)
#     set_window_attribute(hwnd, 20, ct.byref(value),4)

value = Value()

def run():
    # главное окно
    app = customtkinter.CTk()
    app.title('23procg')
    icon = ImageTk.PhotoImage(Image.open("res/drawable/23procg_nobg.jpg"))
    # img = Image.open("res/drawable/icon.ico")
    app.tk.call('wm', 'iconphoto', app._w, icon) 
    
    
    #app.iconphoto(True, icon)
    app.geometry("773x591")
    # app.attributes('-alpha', 0.5)
    app.resizable(False, False)
    # app.overrideredirect(True)
    app.configure(fg_color='#444444')
    #dark_title_bar(app)

    # Ячейки главного, я раскидал их по блокам
    logobox = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
    logobox.configure(width=175, height=107.4, corner_radius=0)
    logobox.place(x=0, y=0)
    # числами в методе resize регулировать высоту и ширину логотипа
    logo_img = ImageTk.PhotoImage(Image.open("res/drawable/23procg_nobg.jpg").resize((115, 25)))
    
    label_logo_img = Label(logobox, image=logo_img, borderwidth=0)
    label_logo_img.place(x=29, y=41)

    menu = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
    menu.configure(width=175, height=307, corner_radius=0)
    menu.place(x=0, y=108)

    fotter = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
    fotter.configure(width=175, height=176, corner_radius=0)
    fotter.place(x=0, y=415)

    value.main = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
    value.main.configure(width=598, height=374, corner_radius=0)
    value.main.place(x=175, y=0)

    value.nav = customtkinter.CTkFrame(master=app, fg_color="#1C1D21")
    value.nav.configure(width=607, height=217, corner_radius=0)
    value.nav.place(x=175, y=375)

    # Надпись которая зависит от времени открывания программы

    hello = customtkinter.CTkLabel(value.main, text=welcome_txt[time_of_day()], text_color="#FFFFFF", font=("Arial blod", 15))
    hello.place(relx=.5, rely=.5, anchor="c")
    # различные рандомные вырожения
    hello = customtkinter.CTkLabel(value.nav, text=random.choice(random_txt), text_color="#777777", font=("blod", 10))
    hello.place(relx=.5, rely=.5, anchor="c")

# кнопки меню ----------------------------------------------------------------------------------------------------

    # 451
    value.led_menu_but = customtkinter.CTkButton(menu, command=lambda:activity.led_page(value), text="Подсветка", text_color="#ffffff",
                                        hover_color="#B5F22F", corner_radius=8, width=113, height=30, fg_color="#1C1D21", state="disabled")
    value.led_menu_but.place(x=31, y=82)

    # 140
    value.key_menu_but = customtkinter.CTkButton(menu, command=lambda: activity.key_page(value), text="Ввод макросов", text_color="#ffffff",
                                        hover_color="#B5F22F", corner_radius=8, width=113, height=30, fg_color="#1C1D21")
    value.key_menu_but.place(x=31, y=42)
    # подсказки
    ToolTip(value.key_menu_but, msg="Замена функций клавишь", delay=0, fg="#B5F22F", bg="#1C1D21")
    ToolTip(value.led_menu_but, msg="Замена цвета подсветки", delay=0, fg="#B5F22F", bg="#1C1D21")

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


if __name__ == "__main__":
    run()