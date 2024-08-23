from songInfoFromSearch import songInfoForSearch
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def soundCloudSearch(song, artist):
    songInfo = songInfoForSearch(song, artist)

    headers = {
        'Accept': '',
        'Accept-Language': '',
        'Connection': 'keep-alive',
        'Origin': 'https://soundcloud.com',
        'Referer': 'https://soundcloud.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': '',
        'sec-ch-ua': '',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'q': songInfo,
        'variant_ids': '',
        'facet': 'model',
        'user_id': '',
        'client_id': 'nFddmw3ZibOug7XKUPPyXjYCElJCcGcv',
        'limit': '10',
        'offset': '0',
        'linked_partitioning': '1',
        'app_version': '',
        'app_locale': 'en',
    }

    response = requests.get('https://api-v2.soundcloud.com/search', params=params, headers=headers)

    finalLink = URLRetriever(response)
    return finalLink

def URLRetriever(info):
    urlInfo = json.loads(info.text)
    finalURL = urlInfo['collection'][00]['permalink_url']
    return finalURL
