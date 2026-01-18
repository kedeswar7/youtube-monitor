import os
import requests

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_IDS = os.getenv("CHANNEL_IDS").split(",")

def get_latest_video(channel_id):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": API_KEY,
        "channelId": channel_id,
        "part": "snippet",
        "order": "date",
        "maxResults": 1
    }
    r = requests.get(url, params=params).json()
    if not r.get("items"):
        return None
    v = r["items"][0]
    return v["id"]["videoId"], v["snippet"]["title"]