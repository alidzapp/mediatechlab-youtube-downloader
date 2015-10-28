from tkinter import *
from tkinter import ttk

def check(*args):
    try:
        print("Check command")
    except ValueError:
        pass

def download(*args):
    try:
        print("Download command")
    except ValueError:
        pass
    
def dlg(*args):
    try:
        print("Dlg command")
        messengerbox.showinfo('About', 'Home Work\nMedia Technology Laboratory 2.\nCreated by Peter Demeter\n2015')
    except ValueError:
        pass

root = Tk()
root.title("YouTube Downloader")

#FRAMES
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

feet = StringVar()
meters = StringVar()

#TOP
top_text  = ttk.Label(top, text="Enter video URL")
top_entry = ttk.Entry(top, textvariable=feet, width=43)
top_check = ttk.Button(top, text="Check", command=check)
top_text.grid( column=0, row=0, sticky=W)
top_entry.grid(column=0, row=1, sticky=W)
top_check.grid(column=1, row=1, sticky=W, padx=15)

#LEFT
dummy_pic = Canvas(left, width=240, height=160, bg='black')
dummy_pic.grid(column=0, row=0, sticky=W)

#RIGHT
video_name     = "dummy video name"
right_vformats = StringVar()
right_aformats = StringVar()
right_name   = ttk.Label(right, text=video_name)
right_video  = ttk.Label(right, text="VIDEO format")
right_vcombo = ttk.Combobox(right, textvariable=right_vformats)
right_audio  = ttk.Label(right, text="AUDIO format")
right_acombo = ttk.Combobox(right, textvariable=right_aformats)
right_name.grid(  column=0, row=0, sticky=W)
right_video.grid( column=0, row=1, sticky=W, pady=15)
right_vcombo.grid(column=0, row=2, sticky=W, pady=15)
right_audio.grid( column=0, row=3, sticky=W, pady=15)
right_acombo.grid(column=0, row=4, sticky=W, pady=15)

#BOTTOM -----------
bottom_path     = "C:\dummy\demo"
bottom_text     = ttk.Label(bottom, text="SAVE TO:")
bottom_plabel   = ttk.Label(bottom, text=bottom_path)
#bottom_dlgbtn	= ttk.Button(bottom, text="Browse", command=dlg)
bottom_download = ttk.Button(bottom, text="Download", command=download)
bottom_progress = ttk.Progressbar(bottom, orient=HORIZONTAL, length=350, mode='determinate')
bottom_text.grid(    column=0, row=0, sticky=W)
bottom_plabel.grid(	 column=0, row=1, sticky=W)
#bottom_dlgbtn(       column=1, row=1, pady=15)
bottom_download.grid(column=2, row=3, sticky=E, padx=15)
bottom_progress.grid(column=0, row=3, columnspan=2, pady=15)

root.mainloop()