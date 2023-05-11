import tkinter
from tkinter import *
import customtkinter
import webbrowser
import serial

#авто подключение к ардуйно
import serial.tools.list_ports

print('Search...')
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print('Find port '+ port.device)

ser = serial.Serial(port.device)
if ser.isOpen():
    ser.close()

ser = serial.Serial(port.device, 9600, timeout=1)
ser.flushInput()
ser.flushOutput()
print('Connect ' + ser.name)



#главный экранs
root_tk = customtkinter.CTk()
root_tk.title('ASPIS')
root_tk.iconbitmap('aspid.ico')
root_tk.geometry("670x400")
root_tk.resizable(False,False)
root_tk.configure(bg='#313335')

img = PhotoImage(file='background.png')
Label(root_tk,image=img,bg='#000000').pack()



#первый ряд


#1key
def mini_tk_18():
    namekey = "key18"
    file = open('key1.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key18.txt")
button = customtkinter.CTkButton(command=mini_tk_18,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.562, rely=0.115)

def mini_tk_19():
    namekey = "key19"
    file = open('key1.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key19.txt")
button = customtkinter.CTkButton(command=mini_tk_19,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.684, rely=0.115)

def mini_tk_20():
    namekey = "key20"
    file = open('key1.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key20.txt")
button = customtkinter.CTkButton(command=mini_tk_20,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.805, rely=0.115)

def mini_tk_1():
    namekey = "key1"
    file = open('key1.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key1.txt")
button = customtkinter.CTkButton(command=mini_tk_1,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.083, rely=0.316)

def mini_tk_5():
    namekey = "key5"
    file = open('key5.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key5.txt")
button = customtkinter.CTkButton(command=mini_tk_5,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.201, rely=0.316)

def mini_tk_6():
    namekey = "key6"
    file = open('key6.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key6.txt")
button = customtkinter.CTkButton(command=mini_tk_6,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.321, rely=0.316)

def mini_tk_9():
    namekey = "key9"
    file = open('key9.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key9.txt")
button = customtkinter.CTkButton(command=mini_tk_9,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.44, rely=0.316)

def mini_tk_9():
    namekey = "key9"
    file = open('key9.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key9.txt")
button = customtkinter.CTkButton(command=mini_tk_9,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.44, rely=0.316)

def mini_tk_10():
    namekey = "key10"
    file = open('key10.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key10.txt")
button = customtkinter.CTkButton(command=mini_tk_10,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.562, rely=0.316)

def mini_tk_14():
    namekey = "key14"
    file = open('key14.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key14.txt")
button = customtkinter.CTkButton(command=mini_tk_14,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.684, rely=0.316)

def mini_tk_21():
    namekey = "key21"
    file = open('key21.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key21.txt")
button = customtkinter.CTkButton(command=mini_tk_21,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=158.5,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.805, rely=0.316)

def mini_tk_2():
    namekey = "key2"
    file = open('key2.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key2.txt")
button = customtkinter.CTkButton(command=mini_tk_2,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=158.5,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.083, rely=0.516)

def mini_tk_7():
    namekey = "key7"
    file = open('key7.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key7.txt")
button = customtkinter.CTkButton(command=mini_tk_7,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.321, rely=0.516)

def mini_tk_11():
    namekey = "key11"
    file = open('key11.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key11.txt")
button = customtkinter.CTkButton(command=mini_tk_11,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.44, rely=0.516)

def mini_tk_12():
    namekey = "key12"
    file = open('key12.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key12.txt")
button = customtkinter.CTkButton(command=mini_tk_12,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.562, rely=0.516)

def mini_tk_15():
    namekey = "key15"
    file = open('key15.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key15.txt")
button = customtkinter.CTkButton(command=mini_tk_15,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.684, rely=0.516)

def mini_tk_15():
    namekey = "key15"
    file = open('key15.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key15.txt")
button = customtkinter.CTkButton(command=mini_tk_15,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.684, rely=0.516)

def mini_tk_3():
    namekey = "key3"
    file = open('key3.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key3.txt")
button = customtkinter.CTkButton(command=mini_tk_3,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.083, rely=0.718)

def mini_tk_4():
    namekey = "key4"
    file = open('key4.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key4.txt")
button = customtkinter.CTkButton(command=mini_tk_4,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.201, rely=0.718)

def mini_tk_8():
    namekey = "key8"
    file = open('key8.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key8.txt")
button = customtkinter.CTkButton(command=mini_tk_8,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.321, rely=0.718)

def mini_tk_13():
    namekey = "key13"
    file = open('key13.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key13.txt")
button = customtkinter.CTkButton(command=mini_tk_13,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=160,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.44, rely=0.718)

def mini_tk_16():
    namekey = "key16"
    file = open('key16.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key16.txt")
button = customtkinter.CTkButton(command=mini_tk_16,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.684, rely=0.718)

def mini_tk_17():
    namekey = "key17"
    file = open('key17.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key17.txt")
button = customtkinter.CTkButton(command=mini_tk_17,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=15,width=79.7,height=79.7,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.805, rely=0.718)


#Энкодер
def mini_tk_23():
    namekey = "key23"
    file = open('key23.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key23.txt")
button = customtkinter.CTkButton(command=mini_tk_23,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=0,width=55,height=10,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.22, rely=0.145)


def mini_tk_24():
    namekey = "key24"
    file = open('key24.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key24.txt")
button = customtkinter.CTkButton(command=mini_tk_24,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=0,width=55,height=10,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.083, rely=0.145)





def mini_tk_22():
    namekey = "key22"
    file = open('key22.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key22.txt")
button = customtkinter.CTkButton(command=mini_tk_22,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=0,width=55,height=55,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.15, rely=0.115)



#Валик

def mini_tk_27():
    namekey = "key27"
    file = open('key27.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key27.txt")
button = customtkinter.CTkButton(command=mini_tk_27,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=0,width=140,height=35,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.321, rely=0.115)

def mini_tk_28():
    namekey = "key28"
    file = open('key28.txt','w')
    y_padding = 5
    #окно
    new_win_1 = customtkinter.CTkToplevel()
    new_win_1.title('ASPIS')
    new_win_1.iconbitmap('aspid.ico')
    new_win_1.configure(bg='black')
    new_win_1.geometry("400x300")
    new_win_1.resizable(False, False)
    new_win_1.configure(bg='#313335')
    #подокно для вёрстки
    frame_1 = customtkinter.CTkFrame(master=new_win_1, corner_radius=15,fg_color='#313335')
    frame_1.pack(pady=10, padx=10, fill="both", expand=True)
    #надпись в окне
    label_1 = customtkinter.CTkLabel(text="Введите макрос набор",text_color="#cce74f", master=frame_1, justify=tkinter.LEFT)
    label_1.pack(pady=y_padding, padx=3)
    #полле ввода
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="eng")
    entry_1.pack(pady=y_padding, padx=15)


    #окна для вёрстки чекбоксов
    f_top = Label(master=frame_1,bg='#313335')
    f_top.place(relx=0.17, rely=0.30)
    f_bop = Label(master=frame_1, bg='#313335')
    f_bop.place(relx=0.14, rely=0.42)
    f_jop = Label(master=frame_1, bg='#313335')
    f_jop.place(relx=0.14, rely=0.54)


    #процесс сохронения и записи диджета
    #что он делает: на клавиатуру через COM3 или любой другой COM отпраляется текст
    def save():
        name = entry_1.get()
        entrycode = (f'{name}')

        if entry_1.get():
            keyname = entrycode
            name = "+" + entrycode
        else:
            keyname = ""
            name = ""

        if (C.get()):
            keynamec = "Ctrl+\n"
            namec = "+Ctrl"
        else:
            keynamec = ""
            namec = ""

        if (S.get()):
            keynames = "Shift+\n"
            names = "+Shift"
        else:
            keynames = ""
            names = ""

        if (T.get()):
            keynamet = "Tab+\n"
            namet = "+Tab"
        else:
            keynamet = ""
            namet = ""

        if (A.get()):
            keynamea = "Alt+\n"
            namea = "+Alt"
        else:
            keynamea = ""
            namea = ""

        if (Sp.get()):
            keynamesp = "Space+\n"
            namesp = "+Space"
        else:
            keynamesp = ""
            namesp = ""

        if (D.get()):
            keynamed = "Del+\n"
            named = "+Del"
        else:
            keynamed = ""
            named = ""

        if (B.get()):
            keynameb = "Back+\n"
            nameb = "+Back"
        else:
            keynameb = ""
            nameb = ""

        if (Es.get()):
            keynamees = "Esc+\n"
            namees = "+Esc"
        else:
            keynamees = ""
            namees = ""

        dataToSend =  "$" +  namekey + namec + names + namet + namea + namesp + named + nameb + namees + name + ";"
        ser.write(dataToSend.encode())
        print(dataToSend)
        datakey = "\n" + keynamec + keynames + keynamet + keynamea + keynamesp + keynamed + keynameb + keynamees + keyname
        file.write(datakey)
        new_win_1.destroy()
        file.close()

    #Чекбоксы отметки главных клавиш
    C = StringVar()
    C_text = "Ctrl"
    checkbox_1 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=C_text, variable=C,onvalue=C_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_1.pack(side=LEFT,padx=5)
    S = StringVar()
    S_text = "Shift"
    checkbox_2 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=S_text, variable=S, onvalue=S_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_2.pack(side=LEFT,padx=5)
    T = StringVar()
    T_text = "Tab"
    checkbox_3 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=T_text, variable=T, onvalue=T_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_3.pack(side=LEFT,padx=5)
    A = StringVar()
    A_text = "Alt"
    checkbox_4 = customtkinter.CTkCheckBox(master=f_top,text_color="#cce74f",text_font=('OpenSans', 9),text=A_text,variable=A, onvalue=A_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_4.pack(side=LEFT,padx=5)
    Sp = StringVar()
    Sp_text = "Space"
    checkbox_5 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=Sp_text,variable=Sp, onvalue=Sp_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_5.pack(side=LEFT,padx=5)
    D = StringVar()
    D_text = "Del"
    checkbox_6 = customtkinter.CTkCheckBox(master=f_bop,text_color="#cce74f",text_font=('OpenSans', 9),text=D_text,variable=D, onvalue=D_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_6.pack(side=LEFT,padx=5)
    B = StringVar()
    B_text = "Back"
    checkbox_7 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9),text=B_text,variable=B, onvalue=B_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_7.pack(side=LEFT,padx=5)
    Es = StringVar()
    Es_text = "Esc"
    checkbox_8 = customtkinter.CTkCheckBox(master=f_bop, text_color="#cce74f",text_font=('OpenSans', 9), text=Es_text,variable=Es, onvalue=Es_text, offvalue='',fg_color="#cce74f",hover_color="#cce74f",checkmark_color="#313335")
    checkbox_8.pack(side=LEFT,padx=5)
    #этот раздел не подключён

    Entr_text = "Entr"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=Entr_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F1"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text,variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "F2"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)

    F1_text = "commnd"
    checkbox_9 = customtkinter.CTkCheckBox(master=f_jop, text_color="#cce74f", text_font=('OpenSans', 9), text=F1_text, variable=Es, onvalue=Es_text, offvalue='', fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335")
    checkbox_9.pack(side=LEFT, padx=5)





    #Кнопка сохронения
    button_1 = customtkinter.CTkButton(master=frame_1,command=save,text="Сохронить", text_color="#cce74f",text_font=('OpenSans', 9),fg_color='#394cb0')
    button_1.place(relx=0.32, rely=0.82)
    #чтобы окно было главнее всех
    new_win_1.grab_set()
    new_win_1.focus_set()
    new_win_1.wait_window()
button_name_1 = open("key27.txt")
button = customtkinter.CTkButton(command=mini_tk_28,text=f'{button_name_1.read()}',text_color="#008bd0",text_font=('OpenSans', 9),corner_radius=0,width=140,height=35,fg_color='#dddddd',hover_color="#00ac65")
button.place(relx=0.321, rely=0.20)







#информацияонный подвал
border_1 = customtkinter.CTkLabel(text_font=('OpenSans', 5),text="©Aspis Keyboard 2022",text_color="#cce74f", justify=tkinter.LEFT)
border_1.place(relx=0.01, rely=0.95)

def behance(event):
    webbrowser.open_new(r"https://www.behance.net/shakirovnz")
labelr = Label(root_tk, text="behance", fg="#0058fb", cursor="hand2",bg='#313335')
labelr.bind("<Button-1>", behance)
labelr.place(relx=0.36, rely=0.95)

def telegram(event):
    webbrowser.open_new(r"https://t.me/shakirovnz")
labelr = Label(root_tk, text="telegram", fg="#2aa2de", cursor="hand2",bg='#313335')
labelr.bind("<Button-1>", telegram)
labelr.place(relx=0.45, rely=0.95)




root_tk.mainloop()
