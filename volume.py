import osascript

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

def get_curr_volume():
	return osascript.run(GET_VOL)

def set_curr_volume(vol):
	return osascript.run(SET_VOL % (vol))