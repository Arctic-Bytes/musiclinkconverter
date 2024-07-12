from Spotify import songArtistNames
from AppleMusic import musicSearch

# Step 1: User enters the Spotify link so the program can retrieve the song and artist name
print("Spotify to Apple Music link converter.")
musicLink = input("Paste Spotify link here: ")

# Step 2: Turn the link into the song and artist name and give it their variables
song, artist = songArtistNames(musicLink)
print("Your song:", song, "by", artist)
# Step 3: Use the song and artist name to get a link on Apple Music
URL = musicSearch(song, artist)
# Step 4: Give the link to the user
print("Apple Music URL:", URL)
