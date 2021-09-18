import urllib.request, json
from selenium import webdriver
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def search_for_new_vid():
    api_key = 'AIzaSyD84lJPl2g99LQxlDMTJMO8yTZVeih0PUk'
    channel_key = 'UCO7bzHSJiCH8BokoFVwoKnw'
    base_vid_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_key)
    inp = urllib.request.urlopen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']
    video_exists = False    

    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidId:
            driver = webdriver.Chrome()
            driver.get(base_video_url + vidID)
            video_exists = True
    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId' : vidId}
            json.dump(data, json_file)
try:
    while True:
        search_for_new_vid()
        time.sleep(10)
except KeyboardInterrupt:
    print('ceasing search for new video')