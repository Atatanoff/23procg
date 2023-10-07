import customtkinter
from loguru import logger


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
        self.name_button = None                         #имя сохраняемой кнопки
        self.macros_id = None                           #id сохраняемого макроса
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
        print(name_bt)
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
        if self.press_bt: self.press_bt.configure(fg_color='#FFFFFF')
        self.press_bt = bt

        for el in self.toolbar_prog:
            el.configure(state='active')
        # if self.ph.cget('state') == 'disabled':
        #     self.ph.configure(state='active')
        
        if self.save_bt.cget('state') == 'disabled':
            self.save_bt.configure(state='active',fg_color='#B5F22F')
            self.clear_bt.configure(state='active')        
        
        bt.configure(fg_color='#8AB42F')