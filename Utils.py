import os
import customtkinter
from loguru import logger


# Вспомогательный класс переменных и состояний
class Value:
    def __init__(self) -> None:
        self.key = None        
        self.d_name = dict()   #Коллекция кнопок и значений 
        self.press_bt: customtkinter.CTkButton = None   #Нажатая кнопка
        self.file_name = None #Активное окно. Нужно для сохранения значений кнопок
        self.chboxs: dict[customtkinter.CTkCheckBox] = dict() #Чекбоксы   
        self.ph: customtkinter.CTkButton = None

    # ф-ция форматирования текста кнопки
    def get_text_button(self, data_to_send):
        
        name_bt = data_to_send.split('+')    
        name_bt.pop(0)
        text_bt = ''
        for i in range(len(name_bt) - 1):
            text_bt += name_bt[i] + '+' + '\n'
        
        if name_bt: text_bt += name_bt[-1][:-1]
        
        return text_bt
    #обработка чекбоксов
    def chboxduble(self, var):
        
        self.chboxs[var].deselect()

# функция сохранения значния выбраной кнопки клавиатуры
 
    def button_function(self, arg: str, bt: customtkinter.CTkButton, button: customtkinter.CTkButton):
   
        self.key = arg
        if self.press_bt: self.press_bt.configure(fg_color='#FFFFFF')
        self.press_bt = bt

        if self.ph.cget('state') == 'disabled':
            self.ph.configure(state='active')
        
        if button.cget('state') == 'disabled':
            button.configure(state='active',fg_color='#B5F22F')
        
        
        bt.configure(fg_color='#8AB42F')

# функция загрузки из конфигурационного файла
@logger.catch
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


