import tkinter

def hello_button_clicked():
    print("Hello")

root = tkinter.Tk()
button = tkinter.Button(root, text="Click Me", command=hello_button_clicked)
button.pack()
root.mainloop()