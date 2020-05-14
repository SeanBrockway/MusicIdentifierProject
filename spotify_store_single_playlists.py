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
content_col = db['Murph Playlist 2']
trackCount = 0
tracks = sp.playlist_tracks('5QZLsm9Q0sGnpt6hqZjId9', fields=None, limit=None, offset=0, market=None) #API Call to get tracklist for the current playlist
for track in tracks['items']: #for each track, add to database
    if (track['track'] is not None):
        trackCount = trackCount + 1
        artist_name_arr = []
        artist_id_arr = []
        genre_arr = []
        # Appending and preparing artist data for storage #

        if ('artists' in track['track']['album']):
            # print('artist in track')

            # Storing artist/s id and title in a list to be sent to mongoDB #

            for artist in track['track']['artists']: 
                # print(artist['name'])
                artist_name_arr.append(artist['name'])
                artist_id_arr.append(artist['id'])

            # Using artist id to get genre data and prepare for storage #
                if (artist['id'] is not None):
                    artist_details = sp.artist(artist['id'])
                    if ('genres' in artist_details):
                        for genre in artist_details['genres']:
                            genre_arr.append(genre)
                    else:
                        genre_arr.append('no genres found')
                    # print(genre_arr)
        #        End of artist and genre data section.   #
        if (track['track']['id'] is not None):
            features = sp.audio_features(track['track']['id']) #API Call to get features for the current song

        # build the record for it to be inserted into the DB
        if (features[0] is not None):
            song_record = { 
                "track": track['track']['name'], 
                "track_id": track['track']['id'],
                "artist_name": artist_name_arr,
                "artist_id": artist_id_arr,
                "genres": genre_arr,
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
        else: 
                song_record = { 
                "track": track['track']['name'], 
                "track_id": track['track']['id'],
                "artist_name": artist_name_arr,
                "artist_id": artist_id_arr,
                "genres": genre_arr,
                "danceability" : 'Features not found',
                "energy" : 'Features not found',
                "key" : 'Features not found',
                "loudness" : 'Features not found',
                "mode" : 'Features not found',
                "speechiness" : 'Features not found',
                "acousticness" : 'Features not found',
                "instrumentalness" : 'Features not found',
                "liveness" : 'Features not found',
                "valence" : 'Features not found',
                "tempo" : 'Features not found',
                "duration_ms" : 'Features not found',
                "time_signature" : 'Features not found'
                
            } 
        find_duplicates = content_col.find_one({"track_id": track['track']['id']})
        print(find_duplicates)
        if(find_duplicates is None):
            content_col.insert_one(song_record)
    # print(song_record)
    print(trackCount)
        

 