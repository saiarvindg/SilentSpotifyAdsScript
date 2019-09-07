import osascript

# since the program always runs in the background - store in memory for now
# TODO: think about storing in env var or file
STORED_VOL = 0

GET_VOL = """
tell application "Spotify"
	get the sound volume
end tell
"""

SET_VOL = f"""
tell application "Spotify"
	set the sound volume to %d
end tell
"""

def get_curr_vol():
	return osascript.run(GET_VOL)

def setup_stored_vol():
	"""
	Run on first startup of program
	"""
	global STORED_VOL
	curr_vol = get_curr_vol()
	if STORED_VOL == 0 and curr_vol == 0:
		STORED_VOL = 55
	else:
		STORED_VOL = curr_vol

def save_curr_vol(first_start = False):
	global STORED_VOL
	STORED_VOL = osascript.run(GET_VOL)
	return STORED_VOL

def set_curr_vol(vol):
	return osascript.run(SET_VOL % (vol))

def restore_vol():
	"""
	Restores Spotiy's volume
	"""
	return set_curr_vol(STORED_VOL)

def mute_vol():
	return set_curr_vol(0)