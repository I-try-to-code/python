import tkinter

from pytz.tzfile import build_tzinfo

# window = tkinter.Tk()
# window.title("my gui")
# window.minsize(500,300)
#
#
# my_lable=tkinter.Label(text="my label",font=("Calibri",25,"bold"))
# my_lable["text"]= "new Texy"
# my_lable.config(text="sadas")
#
# my_lable.pack()
#
# button = tkinter.Button()
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
window.mainloop()
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# import tkinter as tk
#
# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()
#
#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()
#
#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents
#
#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)
#
#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())
#
# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()







