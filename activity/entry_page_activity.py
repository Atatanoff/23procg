import customtkinter
import tkinter

from utils.Utils import save, select_mode
import activity
import res
import sqlite3



    

def entry_page(value):
    # окно для работы с кнопками
    entry_frame = customtkinter.CTkFrame(value.nav, width=607, height=217, corner_radius=0, fg_color="#1C1D21")

    # бар с готовыеми макрос наборами
    toolbar = customtkinter.CTkScrollableFrame(master=entry_frame, scrollbar_button_color="#303135", fg_color="#1C1D21",
                                            orientation="horizontal", width=556, height=51, corner_radius=0)
    toolbar.place(x=42, y=0)

    with sqlite3.connect(res.data) as con:
        cur = con.cursor()
        c = 0
        for el in cur.execute('SELECT id, name FROM programs').fetchall():
            ph = customtkinter.CTkButton(
                toolbar,
                command=lambda i=el[0]: activity.ProgramWin(i, value),
                text=el[1],
                corner_radius=12,
                width=90,
                height=51,
                fg_color="transparent",
                text_color="#777777",
                hover_color="#303135",
                font=("", 11),
                border_color="#FFFFFF",
                state="disabled")
            ph.grid(row=0, column=c)
            value.toolbar_prog.append(ph)
            c+=1

    # ввод макросов
    value.entry_var = tkinter.StringVar()

    entry = customtkinter.CTkEntry(entry_frame, textvariable=value.entry_var, placeholder_text="желательно eng", placeholder_text_color="#474747",
                                corner_radius=6, width=230, height=30, fg_color="#1C1D21", bg_color="#1C1D21",
                                text_color='#FFFFFF', border_width=1, border_color="#777777")
    entry.place(x=323, y=118)

    # чекбоксы
    value.list_var["+Ctrl"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Ctrl"], offvalue='', text_color="#B5F22F", text="Ctrl",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=45, y=78)

    value.list_var["+Alt"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Alt"], offvalue='', text_color="#B5F22F", text="Alt",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=45, y=105)

    value.list_var["+Shift"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Shift"], offvalue='', text_color="#B5F22F", text="Shift",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=45, y=132)

    value.list_var["+Tab"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Tab"], offvalue='', text_color="#B5F22F", text="Tab",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=45, y=159)

    value.list_var["+Esc"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Esc"], offvalue='', text_color="#B5F22F", text="Esc",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=142, y=78)

    value.list_var["+Bac"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Bac"], offvalue='', text_color="#B5F22F", text="Bac",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=142, y=105)

    value.list_var["+Entr"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Entr"], offvalue='', text_color="#B5F22F", text="Entr",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=142, y=132)

    value.list_var["+Del"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Del"], offvalue='', text_color="#B5F22F", text="Del",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=142, y=159)

    value.list_var["+F10"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+F10"], offvalue='', text_color="#B5F22F", text="F10",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=238, y=78)

    value.list_var["+F11"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+F11"], offvalue='', text_color="#B5F22F", text="F11",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=238, y=105)

    value.list_var["+Space"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Space"], offvalue='', text_color="#B5F22F", text="Space",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=238, y=132)

    value.list_var["+Comm"] = tkinter.StringVar()
    checkbox = customtkinter.CTkCheckBox(entry_frame, variable=value.list_var["+Comm"], offvalue='', text_color="#B5F22F", text="Comm",
                                        fg_color="#B5F22F", hover_color="#B5F22F", checkmark_color="#313335",
                                        bg_color="#1C1D21", width=70, checkbox_width=13, checkbox_height=13,
                                        border_width=1, corner_radius=3)
    checkbox.place(x=238, y=159)

    mode_frame = customtkinter.CTkFrame(entry_frame, width=238, height=36, corner_radius=9, fg_color="#303135")
    mode_frame.place(x=323, y=75)

    custom_font = ("Arial", 9,)

    button_ok = customtkinter.CTkButton(mode_frame, text="Одно нажатие", command=lambda: select_mode(value, button_ok, res.mode[0]), font=custom_font, text_color="#FFFFFF",
                                     fg_color='#1C1D21', hover_color="#AA61EC",
                                     corner_radius=7, width=73, height=30, bg_color="#303135")
    button_ok.place(x=3, y=3)
    if not value.press_mode:
        value.press_mode = button_ok
        button_ok.configure(fg_color="#AA61EC")

    button_ho = customtkinter.CTkButton(mode_frame, text="Удержание", command=lambda: select_mode(value, button_ho, res.mode[1]), font=custom_font, text_color="#FFFFFF",
                                        fg_color='#1C1D21',hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    button_ho.place(x=83, y=3)

    button_dk = customtkinter.CTkButton(mode_frame, text="Два нажатия", command=lambda: select_mode(value, button_dk, res.mode[2]), font=custom_font, text_color="#FFFFFF",
                                        fg_color='#1C1D21',hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    button_dk.place(x=161, y=3)
    
    value.buttons_mode = (button_ok, button_ho, button_dk)

    # кнопка сброс
    value.clear_bt = customtkinter.CTkButton(entry_frame, command=lambda: save(value), text="Очистить", text_color="#FFFFFF",
                                     fg_color='#1C1D21', hover_color="#AA61EC",
                                     corner_radius=8, width=113, height=30, bg_color="#1C1D21",
                                     state="disabled")
    value.clear_bt.place(x=323, y=156)      

    # кнопка сохранить
    value.save_bt = customtkinter.CTkButton(entry_frame, command=lambda: save(value), text="Сохранить", text_color="#1C1D21",
                                    fg_color='#66871E',
                                    corner_radius=8, width=113, height=30, bg_color="#1C1D21",
                                    state="disabled")
    value.save_bt.place(x=448, y=156)   

    entry_frame.place(x=0, y=0)