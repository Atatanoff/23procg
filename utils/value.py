import customtkinter
import sqlite3
import res
from loguru import logger
from PIL import Image


# Вспомогательный класс переменных и состояний
class Value:
    def __init__(self) -> None:
        self.key = None                                 #значение нажатой кнопки
        self.d_name = dict()                            #Коллекция кнопок и значений 
        self.press_bt: customtkinter.CTkButton = None   #Нажатая кнопка
        self.save_bt: customtkinter.CTkButton = None
        self.clear_bt: customtkinter.CTkButton = None
        self.file_name = None                           #Путь к файлу значений кнопок активного окна
        self.ph: customtkinter.CTkButton = None
        self.state_nav = False                          #состояние навбара
        self.list_var = dict()                          #словарь переменных выделенных чекбоксов
        self.entry_var = None                           #значение поля ентри
        self.press_mode = None                          #нажатая кнопка выбора режима
        self.buttons_mode = ()                          #кнопки выбора режимов
        self.activity = None                            #функция активного окна
        self.toolbar_prog = list()                      #список кнопок программ
        self.mode = None                                #текущий режим окна
        #параметры сохраняемой кнопки
        self.edit_set_button = None                     #кнопка для которой параметры требуется изменить 
        self.name_button = None                         #имя сохраняемой кнопки
        self.image_button = None                        #id иконки кнопки
        self.color_button = "#EFEFEF"                      #id программы скрипт которой назначен кнопке

        self.macros_id = None                           #id сохраняемого макроса
        self.bt_last_color = None                       #цвет кнопки перед нажатием
        #фреймы
        self.main = None
        self.led_menu_but = None
        self.key_menu_but = None
        self.nav = None

    def disprog(self):
        for el in self.toolbar_prog:
            el.configure(state='disabled')
            
    # ф-ция форматирования текста кнопки
    def get_text_button(self, name):        
        name_bt = name.split('+')[1:]

        #name_bt.pop(0)
        text_bt = ''
        #for i in range(len(name_bt) - 1):
            #text_bt += name_bt[i] + '+' + '\n'        
        #if name_bt: text_bt += name_bt[-1][:-1]
        if name_bt: text_bt = "+\n".join(name_bt)     
        return text_bt

# функция сохранения значния выбраной кнопки клавиатуры
    def button_function(self, arg: str, bt: customtkinter.CTkButton):   
        self.key = arg

        if self.press_bt: self.press_bt.configure(fg_color=self.bt_last_color)
        self.press_bt = bt
        self.bt_last_color = bt.cget('fg_color')

        for el in self.toolbar_prog:
            el.configure(state='active')
        # if self.ph.cget('state') == 'disabled':
        #     self.ph.configure(state='active')
        
        if self.save_bt.cget('state') == 'disabled':
            self.save_bt.configure(state='active',fg_color='#B5F22F')
            self.clear_bt.configure(state='active')        
        
        bt.configure(fg_color='#8AB42F')
# функция сохраненич параметров кнопки в бд
    def save_name_btmb(self):
        
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            id = cur.execute("SELECT id FROM buttons WHERE buttons=?", (self.press_bt.winfo_name(),)).fetchone()
            
            if id:
                           
                cur.execute("UPDATE buttons SET name=NULL, icon_id=?, program_id=? WHERE id=?",
                                (self.image_button, self.color_button, id[0]))
            else:   
                cur.execute(
                    "INSERT INTO buttons VALUES(NULL, ?, ?, ?, ?, ?)",        
                    (
                    self.press_bt.winfo_name(),
                    self.name_button if self.name_button else None,
                    self.mode,
                    self.image_button if self.image_button else None,
                    self.color_button if self.color_button else None
                    )
                    )
        self.edit_set_button = self.press_bt
        self.set_button()     

        
    #обнулние значений сохраняемой или загружаемой кнопки
    def reset(self):
        self.name_button = None
        self.image_button = None
        self.color_button = "#EFEFEF"

    #установка параметров кнопки

    def set_button(self):
        name = self.name_button
        with sqlite3.connect(res.data) as con:
            cur = con.cursor()
            if isinstance(self.image_button, int):
                icon = cur.execute(
                    "SELECT icons, mode, width, hight FROM icons WHERE id=?",
                    (self.image_button,)).fetchone()
                image = customtkinter.CTkImage(
                    Image.frombytes(icon[1], (icon[2], icon[3]), icon[0]))
            else: image = None 
            if isinstance(self.color_button, int):
                color = cur.execute(
                "SELECT color FROM programs WHERE id=?",
                (self.color_button,)).fetchone()[0]
                name = None
                    
            else: color = "#EFEFEF"
        self.edit_set_button.configure(
            text=name,
            image=image,
            fg_color=color,
            )
        self.bt_last_color = color
        self.reset()