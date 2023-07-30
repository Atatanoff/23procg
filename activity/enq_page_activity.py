from loguru import logger
import customtkinter

from utils.Utils import load_file, Value
import res


# ввод крутилок, сделал отдельным окном
@logger.catch
def Enq_page(value: Value, main, key_page, led_menu_but, key_menu_but, nav, mode=res.mode[0]):
    value.mode = mode
    value.save_bt.configure(state='disabled', fg_color='#66871E')
    value.d_name = dict()
    value.file_name = f"data/{res.select_activity[1]}_{mode}.txt"
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

    back_but = customtkinter.CTkButton(Enq_frame, command=lambda: key_page(value, led_menu_but, key_menu_but, main, nav), text="вернутся", text_color="#FFFFFF",
                                       fg_color='#303135',
                                       hover_color="#515358", corner_radius=8, width=76, height=25,
                                       bg_color="#1C1D21")
    back_but.place(x=43, y=42)

    key22 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key22", key22), corner_radius=8, width=70, height=70,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key22.place(x=151, y=156)

    key23 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key23", key23), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key23.place(x=41, y=147)

    key24 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key24", key24), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key24.place(x=41, y=190)

    key25 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key25", key25), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key25.place(x=225, y=147)

    key26 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key26", key26), corner_radius=8, width=106, height=40,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key26.place(x=225, y=190)

    key27 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key27", key27), corner_radius=8, width=144, height=50,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key27.place(x=411, y=137)

    key28 = customtkinter.CTkButton(Enq_frame, text="Пусто", command=lambda: value.button_function("key28", key28), corner_radius=8, width=144, height=50,
                                    fg_color=key_color, text_color=key_text_color, hover_color=key_hover, font=key_font)
    key28.place(x=411, y=190)

    load_file(Enq_frame, value)

    Enq_frame.place(x=0, y=0)