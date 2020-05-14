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
test_playlist_col = db['example_playlist']
playlist_songs = test_playlist_col.find({})
