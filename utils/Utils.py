import os
import customtkinter
import webbrowser
import time
import serial.tools.list_ports
from loguru import logger

import res


# Вспомогательный класс переменных и состояний
class Value:
    def __init__(self) -> None:
        self.key = None                                 #значение нажатой кнопки
        self.d_name = dict()                            #Коллекция кнопок и значений 
        self.press_bt: customtkinter.CTkButton = None   #Нажатая кнопка
        self.save_bt: customtkinter.CTkButton = None
        self.clear_bt: customtkinter.CTkButton = None
        self.file_name = None                           #Активное окно. Нужно для сохранения значений кнопок 
        self.ph: customtkinter.CTkButton = None
        self.state_nav = False                          #состояние навбара
        self.list_var = dict()                          #словарь переменных выделенных чекбоксов
        self.entry_var = None                           #значение поля ентри
        self.mode = None                                #режим

    # ф-ция форматирования текста кнопки
    def get_text_button(self, data_to_send):        
        name_bt = data_to_send.split('+')    
        name_bt.pop(0)
        text_bt = ''
        for i in range(len(name_bt) - 1):
            text_bt += name_bt[i] + '+' + '\n'        
        if name_bt: text_bt += name_bt[-1][:-1]        
        return text_bt

# функция сохранения значния выбраной кнопки клавиатуры
    def button_function(self, arg: str, bt: customtkinter.CTkButton):   
        self.key = arg
        if self.press_bt: self.press_bt.configure(fg_color='#FFFFFF')
        self.press_bt = bt

        if self.ph.cget('state') == 'disabled':
            self.ph.configure(state='active')
        
        if self.save_bt.cget('state') == 'disabled':
            self.save_bt.configure(state='active',fg_color='#B5F22F')       
        
        bt.configure(fg_color='#8AB42F')

# функция загрузки из конфигурационного файла

def load_file(widg: customtkinter.CTkFrame, value: Value):    
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
def save(value: Value):
    name = "" 

    for key, item in value.list_var.items():
        if item.get():
            name += key
            item.set("")

    if value.entry_var.get():
        name += f"+{value.entry_var.get()}"

    savemacro(value, name)


def savemacro(value: Value, name):
    dataToSend = value.key + value.mode + name + ";"
    value.press_bt.configure(text=value.get_text_button(dataToSend))
    value.d_name[value.press_bt.winfo_name()] = dataToSend   
    #entry.delete(0, tkinter.constants.END)
    value.entry_var.set("")
    value.save_bt.configure(state='disabled', fg_color='#66871E')
    value.ph.configure(state='disabled')
    value.press_bt.configure(fg_color='#FFFFFF')           

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