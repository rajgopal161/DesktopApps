import tkinter
from gtts import gTTS
import os
from tkinter import *

def textTospeech(txt):
    t = txt
    output = gTTS(text=t, lang='en', slow=False)
    output.save('outputt.mp3')

    os.system('start outputt.mp3')
    entry.delete(0, END)

window = Tk()
window.title("Text to Speach")

canvas = Canvas(width=400, height=300)
canvas.pack()

lbl = Label(window, text="Enter text which you want to convert to speech", bg="gray")
canvas.create_window(200,130, window= lbl)

entry = Entry(window)
canvas.create_window(200,180, window=entry)

btn = Button(window, text="Click to hear speech", command= lambda : textTospeech(entry.get()))
canvas.create_window(200,250, window=btn)


statusbar = Label(window, text='Welcome to Text to Speech application!!', bg='gray', bd=1, relief=SUNKEN, anchor=W )
statusbar.pack(side=BOTTOM, fill=X)


window.mainloop()
