# Import the required library
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# Create an instance of tkinter frame and window
win=Tk()
win.geometry("700x300")

name = askstring('Name', 'What is your name?')
showinfo('Hello!', 'Hi, {}'.format(name))

win.mainloop()