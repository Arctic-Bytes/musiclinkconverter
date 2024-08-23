import spotipy
import re
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from songInfoFromSearch import songInfoForSearch

load_dotenv()
scope = "user-library-read", "playlist-modify-public", "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def spotifySearch(song, artist):
    songInfo = songInfoForSearch(song, artist)
    spotifyLink = sp.search(songInfo, limit=10, type="track", market="US")
    spotifyURL = spotifyLink['tracks']['items'][0]['external_urls']['spotify']
    return spotifyURL
def getIDFromLink(link):
    match = re.match(r'https://open.spotify.com/track/(.*)', link)
    match = match.group(1)
    return match

def spotifyPlaylistConversion(song, artist):
    songURL = spotifySearch(song, artist)
    songID = getIDFromLink(songURL)
    songURI = 'spotify:track:' + songID
    return songURI

def createPlaylistWithSongs(URIlist):
    user = sp.current_user()
    userID = user['id']
    playlist = sp.user_playlist_create(userID, "Converted Playlist", public=False)
    playlistID = playlist['id']
    for id in range(0, len(URIlist), 100):
        sp.playlist_add_items(playlistID, URIlist[id:id+100])

