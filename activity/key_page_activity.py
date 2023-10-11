import customtkinter
from tktooltip import ToolTip

from utils.Utils import load_file
import activity
import res



def key_page(value, mode=res.mode[0]):
    #запись состояний активного окна
    value.mode = mode
    value.activity = key_page
    if value.save_bt: value.save_bt.configure(state='disabled', fg_color='#66871E')                

    value.file_name = f"data/{res.select_activity[0]}_{mode}.txt"
    
    # менем выделение и цвет текста
    value.led_menu_but.configure(fg_color = "#1C1D21")
    value.key_menu_but.configure(fg_color = "#B5F22F")
    value.key_menu_but.configure(text_color="#1C1D21")
    value.led_menu_but.configure(text_color="#ffffff")
    
    # ввод клавишь -----------------------------------------------------------------------------------------------
    # набор для замены цветов, размера шрифта, итд сразу у всехх клавиш
    
    key_color = "#FFFFFF"
    key_hover = "#B5F22F"
    key_text_color = "#1C1D21"
    key_font = ("", 10)

    #активация кнопок выбора режима
    for el in value.buttons_mode:
        el.configure(state='active')
    if mode == res.mode[0]: pass
    

    key_frame = customtkinter.CTkFrame(value.main, width=598, height=374, corner_radius=0, fg_color="#1C1D21")

    key0 = customtkinter.CTkButton(key_frame, text="", corner_radius=29, width=556, height=331, border_width=1,
                                border_color="#444444",
                                fg_color="#1C1D21", text_color="#1C1D21", hover_color="#1C1D21")
    key0.place(x=21, y=24)

    # кнопки для входа в меню энкодера
    Enq_key = customtkinter.CTkButton(key_frame, command=lambda:activity.Enq_page(value), text=" ", corner_radius=105, width=70, height=70,
                                    fg_color="#EFEFEF", hover_color=key_hover)
    #print(Enq_key.winfo_name())
    Enq_key.place(x=42, y=38)

    Enq_key2 = customtkinter.CTkButton(key_frame, command=lambda:activity.Enq_page(value), text=" ", corner_radius=5, width=160, height=40,
                                    fg_color="#EFEFEF", hover_color=key_hover)
    #print(Enq_key2.winfo_name())
    Enq_key2.place(x=145, y=55)

    # клавишы
    key1 = customtkinter.CTkButton(key_frame, command=lambda: value.button_function("$key18", key1), text="Пусто", corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key1.place(x=337, y=43)

    ToolTip(key1, msg="Ctrl+Alt+e | Ctrl+Alt+shift+e", delay=0, fg="#B5F22F", bg="#1C1D21")

    key2 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key19", key2), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key2.place(x=411, y=43)

    key3 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key20", key3), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key3.place(x=485, y=43)

    key4 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key1", key4), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key4.place(x=41, y=116)

    key5 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key5", key5), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key5.place(x=115, y=116)

    key6 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key6", key6),  corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key6.place(x=189, y=116)

    key7 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key9", key7), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key7.place(x=263, y=116)

    key8 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key10", key8), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key8.place(x=337, y=116)

    key9 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key14", key9), corner_radius=8, width=70, height=70,
                                fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key9.place(x=411, y=116)

    key10 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key21", key10), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key10.place(x=485, y=116)

    key11 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key2", key11), corner_radius=8, width=144, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key11.place(x=41, y=189)

    key12 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key7", key12), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key12.place(x=189, y=189)

    key13 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key11", key13), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key13.place(x=263, y=189)

    key14 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key12", key14), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key14.place(x=337, y=189)

    key15 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key15", key15), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key15.place(x=411, y=189)

    key16 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key17", key16), corner_radius=8, width=70, height=144,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key16.place(x=485, y=189)

    key17 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key3", key17), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key17.place(x=41, y=262)

    key18 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key4", key18), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key18.place(x=115, y=262)

    key19 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key8", key19), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key19.place(x=189, y=262)

    key20 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key13", key20), corner_radius=8, width=144, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key20.place(x=263, y=262)

    key21 = customtkinter.CTkButton(key_frame, text="Пусто", command=lambda: value.button_function("$key16", key21), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key21.place(x=411, y=262)


    load_file(key_frame, value)

    key_frame.place(x=0, y=0)
    
    if not value.state_nav:
        value.state_nav = True
        activity.entry_page(value)
        
