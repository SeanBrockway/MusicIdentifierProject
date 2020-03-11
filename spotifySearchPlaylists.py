import requests
import json
import pymongo
import spotipy
import spotipy.util as util 
from spotipy.oauth2 import SpotifyClientCredentials
from pymongo import MongoClient
import urllib.parse

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

conn = MongoClient("mongodb://localhost:27017/")
db = conn['gym-music-database']
collection = db['Spotify Non-Gym Playlists']

playlists = sp.search('sleep', limit=50, offset=0, type='playlist', market=None)

for playlist in playlists['playlists']['items']:
    print('Playlist')
    
    for key in playlist:
        print('\t', key, '->', playlist[key])

    mydict = { "playlist_name": playlist['name'], "playlist_id": playlist['id'], "source": "Spotify"}
    collection.insert_one(mydict)

