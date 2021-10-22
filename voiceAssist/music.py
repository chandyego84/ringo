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
        self.is_Spotify = False
    
    def play_randPlaylist(self):
            if (not self.is_Spotify):
                    # open spotify once
                    os.system("spotify")
                    self.is_Spotify = True
                    sleep(1.5)

            res = self.sp.devices()
            print(res)
            print(res['devices'][0]['id'])
            self.sp.start_playback(device_id=res['devices'][0]['id'], context_uri='spotify:playlist:4l807VAitl48GiTH35LwC4')