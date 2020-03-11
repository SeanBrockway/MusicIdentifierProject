import requests
import os
import json
import pymongo
import urllib.parse
from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017/")
db = conn['gym-music-database']
collection = db['YouTube Gym Playlists']

response = requests.request('GET', 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=gym%music&type=playlist&key=AIzaSyDwNGLWnhFzIuacufMr-VSyfozjrnBnJ-A&maxResults=50')

youtubePlaylists = response.json()
# print(youtubePlaylists)
for playlist in youtubePlaylists['items']:
    print('Playlist', playlist['id']['playlistId'])
    for key in playlist:
        print('\t', key, '->', playlist[key])
        
    mydict = {"playlist_name": playlist['snippet']['title'], "playlist_id": playlist['id']['playlistId'], "source": "YouTube"}
    collection.insert_one(mydict)

