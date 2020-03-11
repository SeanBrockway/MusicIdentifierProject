import os
import sys
import json
import spotipy
import spotipy.util as util 
from json.decoder import JSONDecodeError

username = 'revy173'
scope = 'user-library-read'

token = util.prompt_for_user_token(username,scope,client_id='96a71a9efaa84bb0811f793c02bf7cba',client_secret='36693ddccae24cfcb852ff5bb74a9c53',redirect_uri='https://www.google.com/')
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(auth=token)

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])