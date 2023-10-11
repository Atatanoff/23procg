import customtkinter


 # Смена лед подсветки -------------------------------------------------------------------------------------
def led_page(value):
    value.state_nav = False
    value.led_menu_but.configure(fg_color = "#B5F22F")
    value.key_menu_but.configure(fg_color = "#1C1D21")
    value.key_menu_but.configure(text_color="#ffffff")
    value.led_menu_but.configure(text_color="#1C1D21")
    # ввод клавишь -----------------------------------------------------------------------------------------------
    # цвета для всех клавиш
    workc= "#B5F22F" #цвет выбранный пользователем

    key_color = "#3F3F3F"
    key_hover = "#3F3F3F"
    key_text_color = "#3F3F3F"
    key_font = ("", 10)
    led_clr = "#3F3F3F"

    led_frame = customtkinter.CTkFrame(value.main, width=598, height=374, corner_radius=0, fg_color="#1C1D21")

    led_frame.place(x=0, y=0)
    br_cname = "#B5F22F"
    FC = "#A1A1A1"
    HC = "#A1A1A1"
    SB = 0 #размер обводки


    key1 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key1.place(x=338, y=47)
    value.d_name.append(key1)

    key2 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key2.place(x=417, y=47)
    value.d_name.append(key2)

    key3 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key3.place(x=491, y=47)
    value.d_name.append(key3)

    key4 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key4.place(x=36, y=120)
    value.d_name.append(key4)

    key5 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key5.place(x=110, y=120)
    value.d_name.append(key5)

    key6 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key6.place(x=184, y=120)
    value.d_name.append(key6)

    key7 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key7.place(x=264, y=120)
    value.d_name.append(key7)

    key8 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key8.place(x=338, y=120)
    value.d_name.append(key8)

    key9 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key9.place(x=417, y=120)
    value.d_name.append(key9)

    key10 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key10.place(x=491, y=120)
    value.d_name.append(key10)

    key11 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=144, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key11.place(x=36, y=193)
    value.d_name.append(key11)

    key12 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key12.place(x=184, y=193)
    value.d_name.append(key12)

    key13 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key13.place(x=264, y=193)
    value.d_name.append(key13)

    key14 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key14.place(x=338, y=193)
    value.d_name.append(key14)

    key15 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key15.place(x=417, y=193)
    value.d_name.append(key15)

    key16 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=144, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key16.place(x=491, y=193)
    value.d_name.append(key16)

    key17 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key17.place(x=36, y=266)
    value.d_name.append(key17)

    key18 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key18.place(x=110, y=266)
    value.d_name.append(key18)

    key19 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key19.place(x=184, y=266)
    value.d_name.append(key19)

    key20 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=144, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key20.place(x=264, y=266)
    value.d_name.append(key20)

    key21 = customtkinter.CTkButton(led_frame, text=" ", corner_radius=8, width=70, height=70, border_width=SB,
                                   fg_color=FC, hover_color=HC,border_color=br_cname)
    key21.place(x=417, y=266)
    value.d_name.append(key21)


    custom_font = ("Arial", 9,)

    color_menu = customtkinter.CTkFrame(value.nav, width=607, height=217, corner_radius=0, fg_color="#1C1D21")


    # полата цветов -------------------------------------------------------------------------------------
    color_pallet = customtkinter.CTkFrame(color_menu, width=607, height=60, corner_radius=0, fg_color="#1C1D21")
    color_pallet.place(x=36, y=50)

    red = customtkinter.CTkButton(color_pallet, text="",fg_color='#FE1F00', hover_color='#FF8878',
                                  corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                  command=lambda: value.ledfunction("$LEDCOLOR+#FF4025;"))
    red.place(x=0, y=0)

    orng = customtkinter.CTkButton(color_pallet, text="", fg_color='#FF7D01', hover_color='#FFBA78',
                                  corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                  command=lambda: value.ledfunction("$LEDCOLOR+#FF7D01;"))
    orng.place(x=60, y=0)

    yell = customtkinter.CTkButton(color_pallet, text="", fg_color='#FFFA01', hover_color='#FFFC78',
                                  corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                  command=lambda: value.ledfunction("$LEDCOLOR+#FFFA01;"))
    yell.place(x=118, y=0)

    gree = customtkinter.CTkButton(color_pallet, text="", fg_color='#B5F22F', hover_color='#BDE578',
                                   corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                   command=lambda: value.ledfunction("$LEDCOLOR+#B5F22F;"))
    gree.place(x=177, y=0)

    sky = customtkinter.CTkButton(color_pallet, text="", fg_color='#00B3D4', hover_color='#78D7E8',
                                   corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                   command=lambda: value.ledfunction("$LEDCOLOR+#00B3D4;"))
    sky.place(x=237, y=0)

    blue = customtkinter.CTkButton(color_pallet, text="", fg_color='#0030FF', hover_color='#788ADA',
                                   corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                   command=lambda: value.ledfunction("$LEDCOLOR+#0030FF;"))
    blue.place(x=296, y=0)

    viol = customtkinter.CTkButton(color_pallet, text="", fg_color='#B207FE', hover_color='#C288DB',
                                  corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                  command=lambda: value.ledfunction("$LEDCOLOR+#B207FE;"))
    viol.place(x=354, y=0)

    pink = customtkinter.CTkButton(color_pallet, text="", fg_color='#FF0089', hover_color='#FA8AC6',
                                   corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                   command=lambda: value.ledfunction("$LEDCOLOR+#FF0089;"))
    pink.place(x=414, y=0)

    wht = customtkinter.CTkButton(color_pallet, text="", fg_color='#FFFFFF', hover_color='#949597',
                                   corner_radius=6, width=55, height=49, bg_color="#1C1D21",
                                   command=lambda: value.ledfunction("$LEDCOLOR+#FFFFFF;"))
    wht.place(x=471, y=0)

    # меню эфектов -------------------------------------------------------------------------------------
    effect_frame = customtkinter.CTkFrame(color_menu, width=315, height=36, corner_radius=9, fg_color="#303135")
    effect_frame.place(x=34, y=150)

    gradient = customtkinter.CTkButton(effect_frame, text="Градиент", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDMODE+gra;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    gradient.place(x=3, y=3)

    short = customtkinter.CTkButton(effect_frame, text="Выстрел", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDMODE+shrt;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    short.place(x=83, y=3)

    blackout = customtkinter.CTkButton(effect_frame, text="Затухание", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDMODE+blac;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    blackout.place(x=161, y=3)

    impuls = customtkinter.CTkButton(effect_frame, text="Импульс", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDMODE+imp;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=73, height=30, bg_color="#303135")
    impuls.place(x=238, y=3)

    # меню Яркости -------------------------------------------------------------------------------------
    light_frame = customtkinter.CTkFrame(color_menu, width=198, height=36, corner_radius=9, fg_color="#303135")
    light_frame.place(x=364, y=150)


    ziro = customtkinter.CTkButton(light_frame, text="00", font=custom_font,
                                        text_color="#FFFFFF", command=lambda: value.ledfunction("$LEDBRIGHT+0;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=36, height=30, bg_color="#303135")
    ziro.place(x=3, y=3)

    twentyfive = customtkinter.CTkButton(light_frame, text="25", font=custom_font,
                                        text_color="#FFFFFF", command=lambda: value.ledfunction("$LEDBRIGHT+25;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=36, height=30, bg_color="#303135")
    twentyfive.place(x=43, y=3)

    fifty = customtkinter.CTkButton(light_frame, text="50", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDBRIGHT+50;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=36, height=30, bg_color="#303135")
    fifty.place(x=81, y=3)

    seventy = customtkinter.CTkButton(light_frame, text="75", font=custom_font,
                                        text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDBRIGHT+75;"),
                                        fg_color='#1C1D21', hover_color="#AA61EC",
                                        corner_radius=7, width=36, height=30, bg_color="#303135")
    seventy.place(x=120, y=3)

    ninety = customtkinter.CTkButton(light_frame, text="99", font=custom_font,
                                          text_color="#FFFFFF",command=lambda: value.ledfunction("$LEDBRIGHT+100;"),
                                          fg_color='#1C1D21', hover_color="#AA61EC",
                                          corner_radius=7, width=36, height=30, bg_color="#303135")
    ninety.place(x=159, y=3)

    gradient = customtkinter.CTkButton(color_menu, text="цвет подсветки ", font=custom_font,text_color="#FFFFFF",
                                       fg_color='#1C1D21', hover_color="#1C1D21",
                                       corner_radius=7, width=73, height=30, bg_color="#1C1D21")
    gradient.place(x=36, y=15)

    gradient = customtkinter.CTkButton(color_menu, text="еффекты подсветки ", font=custom_font,text_color="#FFFFFF",
                                       fg_color='#1C1D21', hover_color="#1C1D21",
                                       corner_radius=7, width=73, height=30, bg_color="#1C1D21")
    gradient.place(x=36, y=114)

    gradient = customtkinter.CTkButton(color_menu, text="общая яркость", font=custom_font,text_color="#FFFFFF",
                                       fg_color='#1C1D21', hover_color="#1C1D21",
                                       corner_radius=7, width=73, height=30, bg_color="#1C1D21")
    gradient.place(x=360, y=114)



    color_menu.place(x=0, y=0)  # конец окна