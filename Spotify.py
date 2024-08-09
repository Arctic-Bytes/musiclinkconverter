import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from songInfoFromSearch import songInfoForSearch

load_dotenv()
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def spotifySearch(song, artist):
    songInfo = songInfoForSearch(song, artist)
    spotifyLink = sp.search(songInfo, limit=10, type="track", market="US")
    spotifyURL = spotifyLink['tracks']['items'][0]['external_urls']['spotify']
    return spotifyURL