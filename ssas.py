import sys
import json
import time
from datetime import datetime, timedelta

from auth import *
from spotify import *
from volume import *

token = ""

ad_length = 30000  # assume ads are only 30 seconds since the spotify api does not give ad lengths :(


def run(token):
	print("Getting currently playing track...")
	result, curr_track = get_curr_track(token)  # currently_playing_type
	if result:
		track_type = curr_track["currently_playing_type"]
		curr_progress = curr_track["progress_ms"]
		if track_type == "track":
			# song
			set_curr_volume(75)  # TODO: get the current volume and set it to that
			song = curr_track["item"]["name"]
			artists = [item["name"]
                            for item in curr_track["item"]["artists"] if item["name"]]
			duration = curr_track["item"]["duration_ms"]
			print(f"Currenty playing track is: {song} by " + ", ".join(
				[str(a) for a in artists]) + f" lasting for {duration} ms with {curr_progress} ms already played")
			print(
				f"spotify api will be called in {duration - curr_progress} ms to check for the next track")
			return (True, calc_track_end_time(duration, curr_progress))
		elif track_type == "ad":
			# ad
			print(
				f"currenty playing an ad for lasting for {ad_length - curr_progress} ms. Spotify will be muted for the duration")
			set_curr_volume(0)  # TODO: save the current volume
			return (True, calc_track_end_time(ad_length, curr_progress))
		else:
			print(
				f"A valid track type was not returned - result: {result}, curr_track: {curr_track} ")
			return (False, -1)
	else:
		print(
			f"could not get current track b/c: ${curr_track}. Spotify may not be playing.")
		return (False, -1)


run_result = True
while run_result:
	if not check_env_set():
		print("Please ensure the client id, client secret, username, and redirect url are set in the environment")
		sys.exit(1)

	result, msg, auth_token = get_auth_token()
	if not result:
		print(msg)
		sys.exit(1)

	run_result, time_to_next_call = run(auth_token)
	print("Run result: " + str(run_result))
	print("Time to next call: " + str( datetime.now() + timedelta(seconds=time_to_next_call) ) + "\n")
	if run_result:
		time.sleep(time_to_next_call)
	else:
		print(
			f"run failed - run_result: {run_result}, time to next call: {time_to_next_call}")
		sys.exit()
