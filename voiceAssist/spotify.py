import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="5ceba33083f9440aa4b1d56878faa463",
                                               client_secret="772c980cdc63400a9618d6cf35495bb8",
                                               redirect_uri="https://www.google.com/",
                                               scope="user-read-playback-state,user-modify-playback-state"))

res = sp.devices()
pprint(res)
print(res['devices'][0]['id'])

# Change track
sp.start_playback(device_id=res['devices'][0]['id'], uris=['spotify:track:3wBAhQLR9VjWfyYO3u4oPR'])
