import customtkinter

import utils.Utils as ut


def Photoshop(value):    
    # окно
    new_win_1 = customtkinter.CTkToplevel()
    #dark_title_bar(new_win_1)
    new_win_1.title('Photoshop')
    new_win_1.configure(bg='#1C1D21')
    new_win_1.geometry("400x300")
    new_win_1.configure(fg_color='#444444')
