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
content_col = db['debug_data']

trackCount = 0
tracks = sp.playlist_tracks('52x5bviOftPPcvdjZ3OsWk', fields=None, limit=100, offset=0, market=None) #API Call to get tracklist for the current playlist
artist_name_arr = []
artist_id_arr = []
for track in tracks['items']: #for each track, add to database
    if (track['track'] is not None):
        artistCount = 0
        print('track')
        trackCount = trackCount + 1
        # print('\t', key, '->', track['track'])
        if ('artists' in track['track']['album']):
            print('artist in track')
            for artist in track['track']['artists']: 
                print(artist['name'])
                artist_name_arr.append(artist['name'])
                artist_id_arr.append(artist['id'])
                artistCount = artistCount + 1
            print(artistCount)
        mydict = { "track": track['track']['name'], "track_id": track['track']['id'], "artist_name": artist_name_arr, "artist_id": artist_id_arr } 
        # content_col.insert_one(mydict)
print(trackCount)

 