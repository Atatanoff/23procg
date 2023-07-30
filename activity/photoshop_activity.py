import customtkinter

from utils.Utils import savemacro


def Photoshop(value):
    
    # окно
    new_win_1 = customtkinter.CTkToplevel()
    #dark_title_bar(new_win_1)
    new_win_1.title('Photoshop')
    new_win_1.configure(bg='#1C1D21')
    new_win_1.geometry("400x300")
    new_win_1.configure(fg_color='#444444')

    # кнопки с предопределёнными макросами
    bt_macro = customtkinter.CTkButton(new_win_1, text="hold+Tab+qwe", corner_radius=8, width=70,
                                 height=70, fg_color="#FFFFFF", text_color="#1C1D21",
                                 hover_color="#B5F22F", font=("", 10),
                                 command=lambda: savemacro(value, "+hold+Tab+qwe" # записываемый макрос
                                                           ))
    bt_macro.pack()

    bt_macro = customtkinter.CTkButton(new_win_1, text="F11+Tab+54", corner_radius=8, width=70,
                                 height=70, fg_color="#FFFFFF", text_color="#1C1D21",
                                 hover_color="#B5F22F", font=("", 10),
                                 command=lambda: savemacro(value, "+F11+Tab+54"
                                                           ))
    bt_macro.pack()