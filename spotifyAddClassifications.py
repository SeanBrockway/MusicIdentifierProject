import requests
import json
import pymongo
import time
import spotipy
import spotipy.util as util 
from spotipy.oauth2 import SpotifyClientCredentials
from pymongo import MongoClient
import urllib.parse

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

conn = MongoClient("mongodb://localhost:27017/")
db = conn['gym-music-database']
content_col = db['test_songlist']
i = 0 
query = content_col.find({})

for document in query: #For each stored playlist in the DB, get tracks 
    i+= 1
    print(i)
    myQuery = { "track_id": document['track_id'] }
    data = {"song_type" : 'gym'} 
    newValues = { "$set": data }
    content_col.update_one(myQuery, newValues)
    