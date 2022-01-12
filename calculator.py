from tkinter import *
import parser
import tkinter.messagebox

#Get the user input and display that in the text box
i = 0
def inp_var(num):
    global i
    display.insert(i, num)
    i += 1

def calc():
    entire_str = display.get()
    try:
        a = parser.expr(entire_str).compile()
        res = eval(a)
        clear_all()
        display.insert(0,res)
    except exception:
        clear_all()
        display.insert(0, "Error")


def get_oper(oper):
    global i
    length = len(oper)
    display.insert(i,oper)
    i += length

def clear_all():
    display.delete(0,END)

def clear_one():
    entire_string = display.get()
    if len(entire_string):
        new_str = entire_string[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"Error")
    #display.delete(i-1)

def quit():
    ans = tkinter.messagebox.askokcancel("Exit", "Are you sure you want to exit calculator?")
    if ans == True:
        window.quit()
    else:
        window.mainloop()

# def only_numbers(char):
#     return char.isdigit()

window = Tk()
window.title("Calculator")
window.configure(background="black")
window.resizable(height=0, width=0)

#Adding a display to the calculator
#validation = window.register(only_numbers)
display = Entry(window)
display.grid(row=1,columnspan=6, sticky=W+E)


#Adding the number buttons for the calculator

Button(window, text="1", height=1, width=2, command = lambda : inp_var(1)).grid(row=2, column=0)
Button(window, text="2", height=1, width=2, command = lambda : inp_var(2)).grid(row=2, column=1)
Button(window, text="3", height=1, width=2, command = lambda : inp_var(3)).grid(row=2, column=2)

Button(window, text="4", height=1, width=2, command = lambda : inp_var(4)).grid(row=3, column=0)
Button(window, text="5", height=1, width=2, command = lambda : inp_var(5)).grid(row=3, column=1)
Button(window, text="6", height=1, width=2, command = lambda : inp_var(6)).grid(row=3, column=2)

Button(window, text="7", height=1, width=2, command = lambda : inp_var(7)).grid(row=4, column=0)
Button(window, text="8", height=1, width=2, command = lambda : inp_var(8)).grid(row=4, column=1)
Button(window, text="9", height=1, width=2, command = lambda : inp_var(9)).grid(row=4, column=2)

Button(window, text=".", height=1, width=2, command = lambda : inp_var(".")).grid(row=5, column=0)
Button(window, text="0", height=1, width=2, command = lambda : inp_var(0)).grid(row=5, column=1)
Button(window, text="=", height=1, width=2, command=calc).grid(row=5, column=2)

#Adding match operation buttons

Button(window, text="+", height=1, width=3, bg="orange", command = lambda : get_oper("+")).grid(row=2, column=3)
Button(window, text="-", height=1, width=3, bg="orange", command = lambda : get_oper("-")).grid(row=3, column=3)
Button(window, text="*", height=1, width=3, bg="orange", command = lambda : get_oper("*")).grid(row=4, column=3)
Button(window, text="/", height=1, width=3, bg="orange", command = lambda : get_oper("/")).grid(row=5, column=3)

Button(window, text="<-", height=1, width=3, bg="orange", command=clear_one).grid(row=2, column=4)
Button(window, text="(", height=1, width=3, bg="orange", command = lambda : get_oper("(")).grid(row=3, column=4)
Button(window, text="%", height=1, width=3, bg="orange", command = lambda : get_oper("%")).grid(row=4, column=4)
Button(window, text="^2", height=1, width=3, bg="orange", command = lambda : get_oper("**2")).grid(row=5, column=4)

Button(window, text="C", height=1, width=3, bg="orange", command=clear_all).grid(row=2, column=5)
Button(window, text=")", height=1, width=3, bg="orange", command = lambda : get_oper(")")).grid(row=3, column=5)
Button(window, text="pi", height=1, width=3, bg="orange", command = lambda : get_oper("*3.14")).grid(row=4, column=5)
Button(window, text="ex", height=1, width=3, bg="red", command = lambda : quit()).grid(row=5, column=5)


window.mainloop()