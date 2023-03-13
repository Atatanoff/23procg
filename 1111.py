import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")


frame_1 = customtkinter.CTkFrame(master=app )
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function )
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1,progress_color="red")
switch_1.pack(pady=10, padx=10)

def slider_callback(value):
    progressbar_1.set(value)

app.mainloop()