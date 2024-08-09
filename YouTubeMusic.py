from ytmusicapi import YTMusic
from songInfoFromSearch import songInfoForSearch

yt = YTMusic()

def ytMusicSearch(song, artist):
    songInfo = songInfoForSearch(song, artist)
    ytMusicLink = yt.search(songInfo, limit=10, ignore_spelling=True)
    ytMusicID = ytMusicLink[0]['videoId']
    ytMusicURL = "https://music.youtube.com/watch?v=" + ytMusicID
    return ytMusicURL