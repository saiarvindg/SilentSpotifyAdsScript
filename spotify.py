import spotipy

def get_curr_track(token):
	sp = spotipy.Spotify(auth=token)
	return sp.current_user_playing_track()

def get_curr_track_type(token):
	sp = spotipy.Spotify(token)
	return sp.current_playback()

def calc_track_end_time(remaining_ms, track_type):
	print("remaining ms: " + str(remaining_ms) + " for track: " +track_type)