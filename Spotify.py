import re

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def songArtistNames(musicLink):
    songID = getIDFromLink(musicLink)
    track = sp.track(songID)
    songName = track['name']
    artistName = track['artists'][0]['name']
    return songName, artistName

def getIDFromLink(link):
    match = re.match(r'https://open.spotify.com/track/(.*)\?si=(.*)', link)
    match = match.group(1)
    return match