from tkinter import *
import pyqrcode
from PIL import ImageTk, Image


def generate_qrcode():
    link_name = entry_name.get()
    link = entry_link.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=4)
    image = ImageTk.PhotoImage(Image.open(file_name))
    img_lbl = Label(image=image)
    img_lbl.image = image
    canvas.create_window(200,460, window=img_lbl)


window = Tk()

canvas = Canvas(window, height=600, width=400)
canvas.pack()

app_lbl = Label(text="QR Code Generator", fg='blue', font=('Arial', 30))
canvas.create_window(200, 100, window=app_lbl)

name_lbl = Label(text='Link Name')
canvas.create_window(200,200, window=name_lbl)

link_lbl = Label(text='Link')
canvas.create_window(200,280, window=link_lbl)

entry_name = Entry()
canvas.create_window(200,230, window=entry_name)

entry_link = Entry()
canvas.create_window(200,300, window=entry_link)

btn = Button(text='Generate QR Code', command=generate_qrcode)
canvas.create_window(200,350, window=btn)

window.mainloop()
