from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil



def download():
    url = link_entry.get()
    file_path = path_lbl.cget("text")
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)

    #code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', file_path)
    #code for mp3

    video_clip.close()
    shutil.move(mp4,file_path)
    lbl_status = Label(window, text='Download Complete!!')
    canvas.create_window(340, 380, window=lbl_status)



def get_path():
    path = filedialog.askdirectory()
    path_lbl.config(text=path)


window = Tk()

canvas = Canvas(window, height=650, width=600 )
canvas.pack()

app_lbl = Label(window, text="YouTube Video Downloader", fg='gray', font=('Arial', 30))
canvas.create_window(300, 100, window=app_lbl)

link_nme = Label(window, text='Enter YouTube Link')
canvas.create_window(200,200, window=link_nme)

link_entry = Entry()
canvas.create_window(340, 200, window=link_entry)

path_lbl = Label(text="Select path to download")
canvas.create_window(340,240, window=path_lbl)


browse_btn = Button(text="Browse", command=get_path)
canvas.create_window(340, 280, window=browse_btn)

download_btn = Button(text="Download", command=download)
canvas.create_window(340, 330, window=download_btn)

window.mainloop()