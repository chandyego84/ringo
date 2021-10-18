import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from time import sleep

class SpotMusic():
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                               client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                               redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
                                               scope="user-read-playback-state,user-modify-playback-state"))
    
    def play_randPlaylist(self):
            res = self.sp.devices()
            print(res)
            print(res['devices'][0]['id'])
            self.sp.start_playback(device_id=res['devices'][0]['id'], context_uri='spotify:playlist:6iCyHoSP9BRg128a9AXetz')


