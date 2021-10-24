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
    
    def playSpecific(self, song):
        if (not self.is_Spotify):
            # open spotify once
            os.system("spotify")
            self.is_Spotify = True
            sleep(1.5)
        # search for song
        res = self.sp.devices() # get device
        searchRes = self.sp.search(q=song, type='track') 
        # get artists of first 10 tracks in search results
        artists = []
        for i in range(10):
            artists.append(searchRes['tracks']['items'][i]['artists'][0]['name'])
        print(artists)

        # get first track in search results
        track = searchRes['tracks']['items'][0]
        # get the track id
        track_id = track['id']
        # play the song
        self.sp.start_playback(device_id=res['devices'][0]['id'], uris=['spotify:track:' + track_id])