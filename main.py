#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk


#------------------------------------------------------------------------------#
# FRAMES
#------------------------------------------------------------------------------#
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

#------------------------------------------------------------------------------#
# TOP
#------------------------------------------------------------------------------#
url = StringVar()
url.set("https://www.youtube.com/watch?v=cJEjQxuc5yk") # ONLY FOR TEST!
top_text  = ttk.Label(top,  text="Enter video URL")
top_entry = ttk.Entry(top,  textvariable=url, width=43)
top_check = ttk.Button(top, text="Check", command=check)
top_text.grid( column=0, row=0, sticky=W)
top_entry.grid(column=0, row=1, sticky=W)
top_check.grid(column=1, row=1, sticky=E, padx=15)

#------------------------------------------------------------------------------#
# LEFT
#------------------------------------------------------------------------------#
dummy_pic = Canvas(left, width=240, height=180, bg='black')
dummy_pic.grid(column=0, row=0, sticky=W)

#------------------------------------------------------------------------------#
# RIGHT
#------------------------------------------------------------------------------#
right_duration = ttk.Label(right, text="")
right_title    = ttk.Label(right, text="")
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

#------------------------------------------------------------------------------#
# BOTTOM
#------------------------------------------------------------------------------#
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

#------------------------------------------------------------------------------#
# draw gui
#------------------------------------------------------------------------------#
root.mainloop()
