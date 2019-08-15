import sys
import json
from auth import *
from spotify import *

token = ""


def run(token):
	curr_track = get_curr_track(token) # currently_playing_type
	print(curr_track)
	print("\n")
	track_type = get_curr_track_type(token)
	print(track_type)
	print("DONE")


if not check_env_set():
	print("Please ensure the client id, client secret, username, and redirect url are set in the environment")
	sys.exit(1)
result, msg, auth_token = get_auth_token()
if not result:
	print(msg)
	sys.exit(1)

token = auth_token
run(token)