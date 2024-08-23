from tkinter import *
from tkinter import ttk

from WindowDisplay import songSearch, playlistConverter

# Revised Step 1: Make user interface and make it search all songs
# This command does pretty much everything. Look in WindowDisplay.py for all search code
def startScreen():
    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()

    ttk.Button(frm, text="Song Search", command=songSearch).grid(column=0, row=0, pady=10)
    ttk.Button(frm, text="Playlist Converter (to Spotify)", command=playlistConverter).grid(column=0, row=1, pady=10)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, pady=10)

    root.mainloop()

startScreen()