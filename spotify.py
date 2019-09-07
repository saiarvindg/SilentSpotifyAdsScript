import spotipy
from datetime import datetime, timedelta

def get_curr_track(token):
	sp = spotipy.Spotify(auth=token)
	curr_track = dict(sp.current_user_playing_track())
	if curr_track is None or curr_track["currently_playing_type"] is None:
		return (False, "Could not get the currently playing track")
	
	return (True, curr_track)

# see: https://stackoverflow.com/questions/11523918/python-start-a-function-at-given-time
def calc_track_end_time(total_duration, curr_progress):
	"""
	Returns the time the current track will end in seconds
	"""
	time_left = total_duration - curr_progress
	now = datetime.now()
	run_at = now + timedelta(milliseconds=time_left)
	delay = (run_at - now).total_seconds() - 1.0 # - 1.0 to account for delays due to processing/lag
	return delay