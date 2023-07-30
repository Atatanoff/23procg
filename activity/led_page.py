import customtkinter


 # Смена лед подсветки -------------------------------------------------------------------------------------
def led_page(led_menu_but, key_menu_but, main, nav, value):
    value.state_nav = False
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