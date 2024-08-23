import tkinter
from tkinter import *
from tkinter import ttk

from AppleMusic import musicSearch, appleMusicConversion
from SoundCloud import soundCloudSearch
from Spotify import spotifySearch
from YouTubeMusic import ytMusicSearch


def songSearch():
    # Retrieves the variables from the text box
    def searchButtonClick():
        song = songInput.get()
        artist = artistInput.get()

        appleMusicURL = musicSearch(song, artist)
        appleMusicLabel.delete("1.0", tkinter.END)
        appleMusicLabel.insert(tkinter.END, appleMusicURL)

        spotifyURL = spotifySearch(song, artist)
        spotifyLabel.delete("1.0", tkinter.END)
        spotifyLabel.insert(tkinter.END, spotifyURL)

        ytMusicURL = ytMusicSearch(song, artist)
        ytMusicLabel.delete("1.0", tkinter.END)
        ytMusicLabel.insert(tkinter.END, ytMusicURL)

        soundCloudURL = soundCloudSearch(song, artist)
        soundCloudLabel.delete("1.0", tkinter.END)
        soundCloudLabel.insert(tkinter.END, soundCloudURL)


    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    # Guidelines for search + search button
    ttk.Label(frm, text="Song Name:").grid(column=0, row=0)
    songInput = ttk.Entry(frm)
    songInput.grid(column=1, row=0)
    ttk.Label(frm, text="Artist Name:").grid(column=2, row=0, pady=10)
    artistInput = ttk.Entry(frm)
    artistInput.grid(column=3, row=0)
    ttk.Button(frm, text="Search", command=searchButtonClick).grid(column=2, row=1)
    # Music search results
        # Spotify
    ttk.Label(frm, text="Spotify:").grid(column=0, row=2, pady=10)
    spotifyLabel = Text(frm, height=1, borderwidth=0)
    spotifyLabel.grid(column=1, row=2, pady=10, columnspan=4)
        # Apple Music
    ttk.Label(frm, text="Apple Music:").grid(column=0, row=4, pady=10)
    appleMusicLabel = Text(frm, height=1, borderwidth=0)
    appleMusicLabel.grid(column=1, row=4, pady=10, columnspan=4)
        # SoundCloud
    ttk.Label(frm, text="Soundcloud:").grid(column=0, row=6, pady=10)
    soundCloudLabel = Text(frm, height=1, borderwidth=0)
    soundCloudLabel.grid(column=1, row=6, pady=10, columnspan=4)
        # YouTube Music
    ttk.Label(frm, text="YouTube Music:").grid(column=0, row=8, pady=10)
    ytMusicLabel = Text(frm, height=1, borderwidth=0)
    ytMusicLabel.grid(column=1, row=8, pady=10, columnspan=4)
    # Quit Button
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=10)

    root.mainloop()

def playlistConverter():
    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()

    def playlistConversion():
        URL = appleMusicURL.get()
        appleMusicConversion(URL)
        ttk.Label(frm, text="Done! Check your Spotify library for your converted playlist!").grid(column=0, row=1, pady=10, columnspan=2)


    ttk.Button(frm, text="Convert", command=playlistConversion).grid(column=2, row=2)
    ttk.Label(frm, text="Paste Apple Music link here:").grid(column=0, row=0, pady=10)
    appleMusicURL = ttk.Entry(frm)
    appleMusicURL.grid(column=1, row=0, pady=10, columnspan=3)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, pady=10)

    root.mainloop()
