import os
import customtkinter
import webbrowser
import time
import serial.tools.list_ports
from loguru import logger
import sqlite3

import res
from utils.save_bt import save_name_bt


def select_mode(value, bt = None, mode=res.mode[0]):
    value.press_mode.configure(fg_color='#1C1D21')
    value.press_mode = bt if bt else value.buttons_mode[0]
    value.press_mode.configure(fg_color="#AA61EC")
    value.activity(value, mode)
    

# функция загрузки из конфигурационного файла

def load_file(widg: customtkinter.CTkFrame, value):    
    with sqlite3.connect(res.data) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Button (
        button TEXT NOT NULL,
        name TEXT NOT NULL,
        act TEXT NOT NULL
        )''')
        cur.execute(f"SELECT button, name, act FROM Button WHERE act = '{value.mode}'")
       
        for el in cur:            
            button = el['button']         
            name = el['name']            
            value.d_name[button] = name                      
            widg.nametowidget(button).configure(text=name)

def load_file2(widg: customtkinter.CTkFrame, value):
    #data = get_data()  
    data = ()    
    for el in data:            
        button = el[0]
                   
        name = el[1]           
        value.d_name[button] = name           
        text_bt = value.get_text_button(name)
        if not text_bt: text_bt = "Пусто"            
        widg.nametowidget(button).configure(text=text_bt)

# ф-ция открытия ссылок из подвала
def open_link(url):
    webbrowser.open_new(url)

# ф-ция записи в порт
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

#ф-ция сохранения 
def save(value):
    name = "" 

    for key, item in value.list_var.items():
        if item.get():
            name += key
            item.set("")

    if value.entry_var.get():
        name += f"+{value.entry_var.get()}"

    savemacro(value, name)


def savemacro(value, name):
    dataToSend = value.key + value.mode + name + ";"
    
    text_bt = value.get_text_button(name)
    value.press_bt.configure(text=text_bt)
    #value.press_bt.configure(text=name)
    value.d_name[value.press_bt.winfo_name()] = text_bt  
    #entry.delete(0, tkinter.constants.END)
    value.entry_var.set("")
    value.save_bt.configure(state='disabled', fg_color='#66871E')
    value.clear_bt.configure(state='disabled')
    value.ph.configure(state='disabled')
    value.press_bt.configure(fg_color='#FFFFFF')           

   
    
    save_name_btmb(value)
                    
    ser_write(dataToSend)

def save_name_btmb(value):
    with sqlite3.connect(res.data) as con:
        cur = con.cursor()
        for el in value.d_name:
            cur.execute("INSERT INTO Button VALUES(?, ?, ?)",(el, value.d_name[el], value.mode))

def savemacros2(value, name=None, icon = None, color = None):
    dataToSend = value.key + value.mode + name + ";"
    #text_bt = value.get_text_button(dataToSend)
    #value.press_bt.configure(text=name)

    '''
    если текст (название либо макрос) то присваиваем
    текст, иначе назначаем иконку, если есть цвет, то меням цвет
    '''
    if name:
        value.press_bt.configure(text=value.get_text_button(dataToSend))
    else:
        value.press_bt.configure(text='')
        value.press_bt.configure(image=icon)
    if color:
        value.press_bt.configure(fg_color=color)
    value.d_name[value.press_bt.winfo_name()] = dataToSend   
    #entry.delete(0, tkinter.constants.END)
    value.entry_var.set("")
    value.save_bt.configure(state='disabled', fg_color='#66871E')
    value.clear_bt.configure(state='disabled')
    value.ph.configure(state='disabled')
    value.press_bt.configure(fg_color='#FFFFFF')           

    '''
    этот блок меняем на запись в бд
    '''
    with open(value.file_name, 'w') as f:
        for key in value.d_name:
            print(key, value.d_name[key], file=f)
                    
    ser_write(dataToSend)

def time_of_day():
    t = time.localtime().tm_hour
    if 6 < t < 11:
        return "morning"
    elif 11 <= t < 16:
        return "afternoon"
    elif 16 <= t < 21:
        return "evening"
    elif 21 <= t < 24:
        return "night"
    else: return "awake"