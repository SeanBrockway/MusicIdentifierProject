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
content_col = db['prediction_test_songs']
i = 0 
query = content_col.find({})

for document in query: #For each stored playlist in the DB, get tracks 
    i+= 1
    print(i)
    if (document['track_id'] is not None):
        features = sp.audio_features(document['track_id']) #API Call to get features for the current song
        myQuery = { "track_id": document['track_id'] }
    if (features[0] is not None):
        data = { 
                "danceability" : features[0]['danceability'],
                "energy" : features[0]['energy'],
                "key" : features[0]['key'],
                "loudness" : features[0]['loudness'],
                "mode" : features[0]['mode'],
                "speechiness" : features[0]['speechiness'],
                "acousticness" : features[0]['acousticness'],
                "instrumentalness" : features[0]['instrumentalness'],
                "liveness" : features[0]['liveness'],
                "valence" : features[0]['valence'],
                "tempo" : features[0]['tempo'],
                "duration_ms" : features[0]['duration_ms'],
                "time_signature" : features[0]['time_signature']
        } 
    newValues = { "$set": data }
    content_col.update_one(myQuery, newValues)
    