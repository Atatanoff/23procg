import customtkinter


app = customtkinter.CTk()
app.title('ASPIS')
app.configure(bg='#1C1D21')
app.geometry("556x78")
app.resizable(False, False)
app.configure(bg='#1C1D21')

scroll_frame = customtkinter.CTkScrollableFrame(master=app,scrollbar_button_color="#303135",fg_color="#1C1D21",
                                                orientation="horizontal",width=556, height=51, corner_radius=0)

scroll_frame.place(x=0, y=0)

buttonPs = customtkinter.CTkButton(scroll_frame, text="Photoshop", corner_radius=12, width=90,
                                   height=51, fg_color="transparent", text_color="#777777",
                                   hover_color="#303135", font=("", 11), border_color="#FFFFFF")
buttonPs.grid(row=0, column=0)

app.mainloop()