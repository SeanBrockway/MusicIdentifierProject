import requests
import json
import pymongo
import time
import spotipy
import pandas as pd
import numpy as np
import spotipy.util as util 
from spotipy.oauth2 import SpotifyClientCredentials
from pymongo import MongoClient
import urllib.parse

conn = MongoClient("mongodb://localhost:27017/")
db = conn['gym-music-database']
content_col = db['Spotify Playlist Content']
query = content_col.find({})
i = 0

for document in query: #For each stored song in the DB
    i+= 1
    print(i)

    obj = {
        "danceability" : document['danceability'],
        "energy" : document['energy'],
        "key" : document['key'],
        "loudness" : document['loudness'],
        "mode" : document['mode'],
        "speechiness" : document['speechiness'],
        "acousticness" : document['acousticness'],
        "instrumentalness" : document['instrumentalness'],
        "liveness" : document['liveness'],
        "valence" : document['valence'],
        "tempo" : document['tempo'],
        "duration_ms" : document['duration_ms'],
        "time_signature" : document['time_signature']
    }
    songSeries = pd.Series(obj)

    print(songSeries)