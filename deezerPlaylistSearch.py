import requests
import json
import pymongo
import deezer
from pymongo import MongoClient
import urllib.parse
conn = MongoClient("mongodb://localhost:27017/")
db = conn['gym-music-database']
collection = db['Deezer Gym Playlists']
# dz = deezer.Client(app_id='', app_secret='')
deezerPlaylists = requests.request('GET', 'https://api.deezer.com/search/playlist?q=gym')
# print(deezerPlaylists.text)
playlists = deezerPlaylists.json()
print(playlists['data'])
for playlist in playlists['data']:
    print('Playlist')
    
    for key in playlist:
        print('\t', key, '->', playlist[key])

    mydict = { "playlist_name": playlist['title'], "playlist_id": playlist['id'], "source": "Deezer"}
    collection.insert_one(mydict)