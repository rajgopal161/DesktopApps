from tkinter import *
import tkinter as tk
import psycopg2
import tkinter.messagebox

window= Tk()
window.title("Student Data")


def get_data(name, age, add):
    conn = psycopg2.connect(dbname="studentdb", port="5432", user="postgres", password="raj161", host="localhost")
    curs = conn.cursor() #curs is pointing to your DB
    # name = ent_name.get()
    # age = ent_age.get()
    # add = ent_add.get()
    query = '''INSERT INTO test(Name,age,address) VALUES(%s, %s, %s);'''
    curs.execute(query,(name,age,add))
    statusbar = Label(window, text="Data Captured Successfully!! ", bg="gray", bd=1, relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X)
    print("Data captured successfully!!!")
    clear_all()
    conn.commit()
    conn.close()

def clear_all():
    ent_name.delete(0,END)
    ent_age.delete(0,END)
    ent_add.delete(0,END)
    ent_search.delete(0,END)
    
   
       

def find_student(name):
    conn = psycopg2.connect(dbname="studentdb", port="5432",user="postgres",password="raj161",host="localhost")
    curs = conn.cursor()
    query = '''SELECT * FROM test WHERE name=%s'''
    curs.execute(query,(name,))
    row = curs.fetchone()
    display_search(row)
    conn.commit()
    conn.close()

#results = None

def display_search(row):
    #global results
    results = Listbox(frame, height=1, width=20)
    results.grid(row=10, column=1)
    results.insert(END, row)
    statusbar = Label(window, text="Your Data! ", bg="gray", bd=1, relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X)


def quit():
    ans = tkinter.messagebox.askokcancel("Exit", "Are you sure you want to exit Student? ")
    if ans == True:
        window.quit()
    else:
        window.mainloop()


def only_numbers(char):
    return char.isdigit()

canvas = Canvas(window, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

mymenu = Menu(window)
window.config(menu=mymenu)

filesubmenu = Menu(mymenu)

mymenu.add_cascade(label="Options" , menu=filesubmenu)

filesubmenu.add_command(label="Clear All", command= lambda : clear_all())
#filesubmenu.add_command(label="Save")
filesubmenu.add_separator()
filesubmenu.add_command(label="Exit", command= lambda : quit())

lbl = Label(frame, text="Add Students Data", font="20")
lbl.grid(row=0, column=2)

Label(frame, text="").grid(row=1)

lbln = Label(frame, text="Name")
lbln.grid(row=2, column=0)

ent_name = Entry(frame)
ent_name.grid(row=2, column=1)

lbla = Label(frame, text="Age")
lbla.grid(row=3, column=0)

validation = frame.register(only_numbers)
ent_age = Entry(frame, validate="key", validatecommand=(validation, '%S'))
ent_age.grid(row=3, column=1)


lblad = Label(frame, text="Address")
lblad.grid(row=4, column=0)

ent_add = Entry(frame)
ent_add.grid(row=4, column=1)

sub_button = Button(frame, text="Submit", command=lambda : get_data(ent_name.get(),ent_age.get(),ent_add.get()))
sub_button.grid(row=5, column=2)

Label(frame, text="").grid(row=6)

lbhe = Label(frame, text="Search Students Data", font="20")
lbhe.grid(row=7, column=2)

Label(frame, text="").grid(row=8)

lblse = Label(frame, text="Search_by Name")
lblse.grid(row=9, column=0)

ent_search = Entry(frame) # If you want to add validations --> , validate="key", validatecommand=(validation, '%S')
ent_search.grid(row=9, column=1)

srch_button = Button(frame, text="Click Here", command=lambda : find_student(ent_search.get()))
srch_button.grid(row=9, column=2)

Label(frame, text="").grid(row=11)
Button(frame, text="Exit", width=15,bg="red", command = lambda : quit()).grid(row=12, column=2)

statusbar = Label(window, text="Welcome to Student Database Appliction!! ", bg="gray", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()