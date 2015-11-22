#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
# to show the video pic
import io
from PIL import Image, ImageTk
from urllib.request import urlopen
# to download from youtube
import pafy
# to file browse
import os
from tkinter import filedialog
# to progressbar
import threading

#----------------------------------------------------------------------------------------
# CHECK BUTTON
#----------------------------------------------------------------------------------------
def url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)

    raise Exception("URL validation failed!!!")

def check():
    t = threading.Thread(target=check_thread)
    t.daemon = True
    t.start()

def check_thread():
    try:
        #--------------------------------------------------------------------------------
        # show thumbnail
        #--------------------------------------------------------------------------------
        pic_url = "http://img.youtube.com/vi/" + url_validation(url.get())   + "/0.jpg"
        # open the web page picture and read it into a memory stream
        # and convert to an image Tkinter can handle
        dl_pic = urlopen(pic_url)
        # create an image file object
        my_picture = io.BytesIO(dl_pic.read())
        # use PIL to open image formats like .jpg  .png  .gif  etc.
        pil_img = Image.open(my_picture)
        pil_img = pil_img.resize((240,180))
        # convert to an image Tkinter can use
        tk_img  = ImageTk.PhotoImage(pil_img)
        # put the image on a typical widget
        video_pic = ttk.Label(left, image=tk_img)
        video_pic.grid(column=0, row=0, sticky=W)

        #--------------------------------------------------------------------------------
        # change title + durration + streams
        #--------------------------------------------------------------------------------
        try:
            global video
            global right_vcombo
            global right_acombo
            video = pafy.new(url.get())
            title = video.title
            right_name     = ttk.Label(right, text=title[:35])            
            right_duration = ttk.Label(right, text=video.duration)            
            right_name.grid(    column=0, row=0, sticky=W)
            right_duration.grid(column=0, row=1, sticky=W)

            right_vformats = ["-"]
            for s in video.streams:
                right_vformats.append(str(s))
            right_vcombo = ttk.Combobox(right, values=right_vformats)
            right_vcombo.current(0)
            right_vcombo.grid(column=0, row=3, sticky=W, pady=15)
            
            right_aformats = ["-"]
            for s in video.audiostreams:
                right_aformats.append(str(s))
            right_acombo = ttk.Combobox(right, values=right_aformats)
            right_acombo.current(0)
            right_acombo.grid(column=0, row=5, sticky=W, pady=15)
        except Exception as e:
            print("Error in change title + durration + streams")
            print(e)

        #--------------------------------------------------------------------------------
        # refresh gui
        #--------------------------------------------------------------------------------
        root.mainloop()
    except Exception as e:
        print(e)

#----------------------------------------------------------------------------------------
# BROWSE BUTTON
#----------------------------------------------------------------------------------------
def browse():
    bottom_pentry.delete(0, END)
    bottom_pentry.insert(0, filedialog.askdirectory())

#----------------------------------------------------------------------------------------
# DOWNLOAD BUTTON
#----------------------------------------------------------------------------------------
def download():
    t = threading.Thread(target=download_thread)
    t.daemon = True
    t.start()

def download_thread():
    try:
        global video
        global bottom_pentry
        streams = video.allstreams
        streamlist = []
        for s in streams:
            streamlist.append(str(s))
        #--------------------------------------------------------------------------------
        # download video
        #--------------------------------------------------------------------------------
        try:
            stream_num = streamlist.index(str(right_vcombo.get()))
            streams[stream_num].download(filepath=bottom_pentry.get(), quiet=True, callback=progress)
        except:
            pass
        #--------------------------------------------------------------------------------
        # download video
        #--------------------------------------------------------------------------------
        try:
            stream_num = streamlist.index(str(right_acombo.get()))
            streams[stream_num].download(filepath=bottom_pentry.get(), quiet=True, callback=progress)
        except:
            pass

    except Exception as e:
        print("Error in download!!!")
        print(e)

def progress(total, received, ratio, rate, eta):
    global bottom_progress
    bottom_progress["maximum"] = total
    bottom_progress["value"]   = received

#----------------------------------------------------------------------------------------
# FRAMES
#----------------------------------------------------------------------------------------
root = Tk()
root.title("YouTube Downloader")
mainframe = ttk.Frame(root, padding="20 20 20 20")
top    = ttk.Frame(mainframe, borderwidth=5)
left   = ttk.Frame(mainframe, borderwidth=5)
right  = ttk.Frame(mainframe, borderwidth=5)
bottom = ttk.Frame(mainframe, borderwidth=5)
mainframe.grid(column=0, row=0)
top.grid(      column=0, row=0, sticky=(W,N), columnspan=2)
left.grid(     column=0, row=1, sticky=W)
right.grid(    column=1, row=1, sticky=E)
bottom.grid(   column=0, row=2, sticky=(W,S), columnspan=2)
# ugly solution
video = None

#----------------------------------------------------------------------------------------
# TOP
#----------------------------------------------------------------------------------------
url = StringVar()
url.set("https://www.youtube.com/watch?v=cJEjQxuc5yk") # ONLY FOR TEST!
top_text  = ttk.Label(top,  text="Enter video URL")
top_entry = ttk.Entry(top,  textvariable=url, width=43)
top_check = ttk.Button(top, text="Check", command=check)
top_text.grid( column=0, row=0, sticky=W)
top_entry.grid(column=0, row=1, sticky=W)
top_check.grid(column=1, row=1, sticky=E, padx=15)

#----------------------------------------------------------------------------------------
# LEFT
#----------------------------------------------------------------------------------------
dummy_pic = Canvas(left, width=240, height=180, bg='black')
dummy_pic.grid(column=0, row=0, sticky=W)

#----------------------------------------------------------------------------------------
# RIGHT
#----------------------------------------------------------------------------------------
right_title    = ttk.Label(right, text="")
right_duration = ttk.Label(right, text="")
right_video  = ttk.Label(right, text="VIDEO format")
right_vcombo = ttk.Combobox(right, textvariable="")
right_audio  = ttk.Label(right, text="AUDIO format")
right_acombo = ttk.Combobox(right, textvariable="")
right_title.grid(   column=0, row=0, sticky=W)
right_duration.grid(column=0, row=1, sticky=W)
right_video.grid(   column=0, row=2, sticky=W, pady=10)
right_vcombo.grid(  column=0, row=3, sticky=W, pady=15)
right_audio.grid(   column=0, row=4, sticky=W, pady=10)
right_acombo.grid(  column=0, row=5, sticky=W, pady=15)

#----------------------------------------------------------------------------------------
# BOTTOM
#----------------------------------------------------------------------------------------
bottom_text     = ttk.Label( bottom, text="SAVE TO:")
bottom_pentry   = ttk.Entry( bottom, width=43)
bottom_download = ttk.Button(bottom, text="Download", command=download)
bottom_browse   = ttk.Button(bottom, text="Browse",   command=browse)
bottom_progress = ttk.Progressbar(bottom, orient=HORIZONTAL, length=350, mode='determinate')
bottom_text.grid(    column=0, row=0, sticky=W)
bottom_pentry.grid(  column=0, row=1, sticky=W)
bottom_browse.grid(  column=2, row=1, sticky=W, padx=15)
bottom_download.grid(column=2, row=3, sticky=W, padx=15)
bottom_progress.grid(column=0, row=3, columnspan=2, pady=15)
# set current directory to save path
bottom_pentry.insert(0, os.path.dirname(os.path.realpath(__file__)))

#----------------------------------------------------------------------------------------
# draw gui
#----------------------------------------------------------------------------------------
root.mainloop()