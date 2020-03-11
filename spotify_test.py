import os
import sys
import json
import spotipy
import spotipy.util as util 
from json.decoder import JSONDecodeError

username = 'revy173'
scope = 'user-library-read'

token = util.prompt_for_user_token(username,scope,client_id='96a71a9efaa84bb0811f793c02bf7cba',client_secret='36693ddccae24cfcb852ff5bb74a9c53',redirect_uri='https://www.google.com/')
spotify = spotipy.Spotify(auth=token)


results = spotify.featured_playlists(locale=None, country=None, timestamp=None, limit=20, offset=0)
# results = spotify.categories(locale=None, country=None, limit=30, offset=0)

print('\nMessage: ', results['message'])

for playlist in results['playlists']['items']:
    print('Playlist')
    
    for key in playlist:
        print('\t', key, '->', playlist[key])
    
    description = playlist['description']
    name = playlist['name']
        # print(key, ': ', value)

# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])
    
# print(results)
