#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
# to show the video pic
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
# to download from youtube
import pafy


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

def check(*args):
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
            video = pafy.new(url.get())
            title = video.title
            right_name = ttk.Label(right, text=title[:35])            
            right_name.grid(column=0, row=0, sticky=W)
            right_duration = ttk.Label(right, text=video.duration)            
            right_duration.grid(column=0, row=1, sticky=W)

            right_vformats = video.streams
            right_vcombo = ttk.Combobox(right, values=right_vformats)
            right_vcombo.grid(column=0, row=3, sticky=W, pady=15)

            right_aformats = video.audiostreams
            right_acombo = ttk.Combobox(right, values=right_aformats)
            right_acombo.grid(column=0, row=5, sticky=W, pady=15)
        except Exception as e:
            print("change title + durration + streams")
            print(e)

        #--------------------------------------------------------------------------------
        # refresh gui
        #--------------------------------------------------------------------------------
        root.mainloop()
    except Exception as e:
        print(e)

#----------------------------------------------------------------------------------------
def download(*args):
    try:
        print("Download command")
    except ValueError:
        pass

root = Tk()
root.title("YouTube Downloader")

#----------------------------------------------------------------------------------------
# FRAMES
#----------------------------------------------------------------------------------------
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
top_check.grid(column=1, row=1, sticky=W, padx=15)

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
bottom_path     = "C:\dummy\demo"
bottom_text     = ttk.Label(bottom, text="SAVE TO:")
bottom_plabel   = ttk.Label(bottom, text=bottom_path)
bottom_download = ttk.Button(bottom, text="Download", command=download)
bottom_progress = ttk.Progressbar(bottom, orient=HORIZONTAL, length=350, mode='determinate')
bottom_text.grid(    column=0, row=0, sticky=W)
bottom_plabel.grid(  column=0, row=1, sticky=W)
bottom_download.grid(column=2, row=3, sticky=E, padx=15)
bottom_progress.grid(column=0, row=3, columnspan=2, pady=15)

#----------------------------------------------------------------------------------------
# draw gui
#----------------------------------------------------------------------------------------
root.mainloop()