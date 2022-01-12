from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter.simpledialog import askstring
import tkinter.messagebox
from compression_decompression import compress,decompress

filenamecm = None
filenamedc = None

def open_file_com():
    global filenamecm
    filenamecm = filedialog.askopenfilename(initialdir='/', title="Select file to compress")
    lbl_open = Label(frame, text=filenamecm)
    lbl_open.grid(row=2, column=1)
    return filenamecm

def open_file_decom():
    global filenamedc
    filenamedc = filedialog.askopenfilename(initialdir='/', title="Select file to compress")
    lbl_open = Label(frame, text=filenamedc)
    lbl_open.grid(row=9, column=1)
    return filenamedc

# def choose_dir():
#     filename = filedialog.askdirectory(initialdir='/', title="Select directory to save")
#     return filename

def file_name():
    fname = askstring('File Name', 'Please enter file name to compress/decompress')
    return fname

def comp(i,o):
    compress(i,o)
    lblcmpspac = Label(frame, text= filenamecm + " || File Compressed succesfully!!")
    lblcmpspac.grid(row=5, column=1)


def decomp(i,o):
    decompress(i,o)
    lblcmpspac = Label(frame, text= filenamedc + " || File Decompressed succesfully!!")
    lblcmpspac.grid(row=12, column=1)

def quit():
    ans = tkinter.messagebox.askyesno("Exit", 'Are you sure you want to exit application?')
    if ans == True:
        window.quit()
    else:
        window.mainloop()


window = Tk()
window.title("Compression and decompression")

canvas = Canvas(window, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

lblcmphed = Label(frame, text="Compressing a File", font='20', bg='gray')
lblcmphed.grid(row=0, column=1)

lblcmpsp = Label(frame, text="")
lblcmpsp.grid(row=1, column=1)

lblcmp = Label(frame, text="Choose file to Compress")
lblcmp.grid(row=2, column=0)

btn_browse = Button(frame, text="Browse Files", command= lambda : open_file_com())
btn_browse.grid(row=2, column=2)

lblcmpspa = Label(frame, text="")
lblcmpspa.grid(row=3, column=1)

btn_comp = Button(frame, text="Compress", bg='yellow', command= lambda: comp(filenamecm,file_name()))
btn_comp.grid(row=4, column=1)

lblcmpspac = Label(frame, text="")
lblcmpspac.grid(row=5, column=1)

lblcmpspacc = Label(frame, text="")
lblcmpspacc.grid(row=6, column=1)

lbldecmphed = Label(frame, text="Decompressing a File", font='20', bg='gray')
lbldecmphed.grid(row=7, column=1)

lblcmpspc = Label(frame, text="")
lblcmpspc.grid(row=8, column=1)

lbldecmp = Label(frame, text="Choose file to Decompress")
lbldecmp.grid(row=9, column=0)

btn_browse_de = Button(frame, text="Browse Files", command= lambda : open_file_decom())
btn_browse_de.grid(row=9, column=2)

lblcmpspp = Label(frame, text="")
lblcmpspp.grid(row=10, column=1)

btn_decomp = Button(frame, text="Decompress", bg='yellow', command= lambda: decomp(filenamedc,file_name()))
btn_decomp.grid(row=11, column=1)

lblcmpsap = Label(frame, text="")
lblcmpsap.grid(row=13, column=1)

btn_quit = Button(frame, text="Exit", bg='red', height=1, width=20, command= lambda: quit())
btn_quit.grid(row=15, column=1)


statusbar = Label(window, text="Welcome to Compress/Decompress Appliction!! ", bg="gray", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()