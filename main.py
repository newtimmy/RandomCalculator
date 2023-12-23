from random import randrange
from tkinter import *
from tkinter.simpledialog import askstring

top = Tk()
top.geometry("700x700")
top.configure(bg='#00CC00')
max_number_1 = 4
max_number_2 = 5
label = Label(top, text="", font=('Calibri 20 bold'))
label.pack(pady=20)


def generate_calculation():
    number_1 = randrange(max_number_1)
    number_2 = randrange(max_number_2)
    result = askstring('Hier ist deine Rechnung', f'Was ist {number_1+1} + {number_2+1}?')
    if int(result) == number_1 + number_2 + 2:
        label["text"] = "RICHTIG"
    else:
        label["text"] = "FALSCH"


button = Button(top, fg='#00CC00', bg='#000000', text="eine Rechnung, bitte!", height=30, width=30, command=generate_calculation)
button.place(x=150, y=150)
button.pack(pady=20)
top.mainloop()

