import spotipy

def get_curr_track(token):
	sp = spotipy.Spotify(auth=token)
	return sp.current_user_playing_track()

def get_curr_track_type(token):
	sp = spotipy.Spotify(token)
	return sp.current_playback()