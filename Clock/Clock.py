from tkinter import *
from time import *

root = Tk()
root.title("Clock by Manfateh Singh")

def time():
    String=strftime('%H:%M: %S  %p')
    label.config(text=String)
    label.after(1000, time)


label=Label(root, font = ("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
