from random import randrange
from tkinter import *
from tkinter.simpledialog import askstring

top = Tk()
top.geometry("700x700")
top.configure(bg='#00CC00')
top.title("Rechnen üben")
max_number_1 = 4
max_number_2 = 5
label = Label(top, text="Erzeuge eine Rechenaufgabe:", font=('Calibri 40 bold'))
label.pack(pady=20)


def generate_calculation():
    """
    Generate a calculation using two random numbers and check if the calculation was correct
    :return:
    """
    number_1 = randrange(max_number_1)
    number_2 = randrange(max_number_2)
    result = askstring('Hier ist deine Rechnung', f'Was ist {number_1+1} + {number_2+1}?')
    if int(result) == number_1 + number_2 + 2:
        label["text"] = "RICHTIG"
        label["bg"] = "#FFFFFF"
        label["fg"] = "#00AA00"
        top.configure(bg='#00CC00')
    else:
        label["text"] = f"FALSCH\n richtiges Ergebnis: {number_1+1} + {number_2+1} = {number_1 + number_2 + 2}"
        label["bg"] = "#FFFFFF"
        label["fg"] = "#AA0000"
        top.configure(bg='#CC0000')


button = Button(top, fg='#FFFFFF', bg='#000000', text="HIER BITTE DRÜCKEN für eine Rechenaufgabe", font=('Calibri 20 bold'), height=20, width=50, command=generate_calculation)
button.place(x=200, y=50)
button.pack(pady=20)
top.mainloop()

