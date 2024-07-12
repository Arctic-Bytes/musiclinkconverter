from os import getenv

import requests
import json
from dotenv import load_dotenv

load_dotenv()

def musicSearch(song, artist):
    songInfo = songInfoForSearch(song, artist)

    cookies = {
        'geo': 'US',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': getenv('TOKEN'),
        # 'cookie': 'geo=US',
        'origin': 'https://music.apple.com',
        'priority': 'u=1, i',
        'referer': 'https://music.apple.com/',
        'sec-ch-ua': getenv('BROWSERINFO'),
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': getenv('USERAGENT'),
    }

    params = {
        'art[music-videos:url]': 'c',
        'art[url]': 'f',
        'extend': 'artistUrl',
        'fields[albums]': 'artistName,artistUrl,artwork,contentRating,editorialArtwork,editorialNotes,name,playParams,releaseDate,url,trackCount',
        'fields[artists]': 'url,name,artwork',
        'format[resources]': 'map',
        'include[albums]': 'artists',
        'include[music-videos]': 'artists',
        'include[songs]': 'artists',
        'include[stations]': 'radio-show',
        'l': 'en-US',
        'limit': '1',
        'omit[resource]': 'autos',
        'platform': 'web',
        'relate[albums]': 'artists',
        'relate[songs]': 'albums',
        'term': songInfo,
        'types': 'songs',
        'with': 'lyricHighlights,lyrics,serverBubbles',
    }

    response = requests.get(
        'https://amp-api-edge.music.apple.com/v1/catalog/us/search',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    URLID = strippedURLInfo(response)
    finalURL = IDtoURL(URLID)
    return finalURL

def songInfoForSearch(song, artist):
    songInfo = song + " " + artist
    return songInfo

def strippedURLInfo(info):
    urlInfo = json.loads(info.text)
    if 'song' in urlInfo['results']:
        urlid = urlInfo['results']['song']['data'][0]['id']
    else:
        print("ERROR: Song not found on Apple Music")
        urlid = None
    return urlid

def IDtoURL(id):
    if id == None:
        finalURL = None
    else:
        finalURL = 'music.apple.com/us/song/' + id
    return finalURL
