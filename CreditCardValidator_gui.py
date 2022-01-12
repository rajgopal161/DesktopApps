from tkinter import *


def validate():
    cnumber = card_entry.get()
    num_list = list(cnumber)

    odd_sum = 0
    even_sum = 0
    dbl_evn_list = []

    for (idx, val) in enumerate(num_list):
        if (idx % 2) != 0:
            odd_sum += int(val)
        else:
            dbl_evn_list.append(int(val) * 2)

    dbl_list_str = ""

    for x in dbl_evn_list:
        dbl_list_str += str(x)

    dbl_list_str = list(dbl_list_str)
    for evn_list in dbl_list_str:
        even_sum += int(evn_list)

    net_sum = 0
    net_sum = odd_sum + even_sum
    if net_sum % 10 == 0:
        status_lbl = Label(text="Valid Card", fg='green')
        canvas.create_window(250,250, window=status_lbl)
    else:
        status_lbl = Label(text="Invalid Card", fg='red')
        canvas.create_window(250,250, window=status_lbl)

def only_numbers(char):
    return char.isdigit()


window = Tk()


canvas = Canvas(window, height=500, width=500)
canvas.pack()


app_lbl = Label(text="Credit/Debit Card Validator", fg='gray', font=('Arial', 30))
canvas.create_window(250, 50, window=app_lbl)

card_lbl = Label(text="Enter Credit/Debit Card Number to Validate")
canvas.create_window(250, 150, window=card_lbl)

validation = window.register(only_numbers)
card_entry = Entry(window, validate='key', validatecommand=(validation, '%S'))
canvas.create_window(250,180, window=card_entry)

validate_btn = Button(text="Validate Card", command= lambda : validate())
canvas.create_window(250,220, window=validate_btn)

window.mainloop()
