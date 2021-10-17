import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from time import sleep

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                               client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                               redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
                                               scope="user-read-playback-state,user-modify-playback-state"))

res = sp.devices()
pprint(res)
print(res['devices'][0]['id'])

# Change track
sp.start_playback(device_id=res['devices'][0]['id'], uris=['spotify:track:3wBAhQLR9VjWfyYO3u4oPR'])
