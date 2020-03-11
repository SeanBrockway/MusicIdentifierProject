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
playlists_col = db['Spotify Non-Gym Playlists']
content_col = db['test_songlist']

for document in playlists_col.find(): #For each stored playlist in the DB, get tracks 
    print('Document')
    trackCount = 0
    tracks = sp.playlist_tracks(document['playlist_id'], fields=None, limit=100, offset=0, market=None) #API Call to get tracklist for the current playlist

    for track in tracks['items']: #for each track, add to database
        print('track')
        trackCount = trackCount + 1
        # print('\t', key, '->', track['track'])
        mydict = { "track": track['track']['name'], "track_id": track['track']['id'], "song_type": 'relax/sleeps'} 
        content_col.insert_one(mydict)
    print(trackCount)

 