import os
import sys
import spotipy
import spotipy.util as sputil
from dotenv import load_dotenv


load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
username = os.getenv("USERNAME")
redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")
scope = 'user-read-currently-playing user-modify-playback-state'

# check the env vars are set
if not client_id or not client_secret or not username or not redirect_url:
	print("Please ensure the client id, client secret, username, and redirect url are set")
	sys.exit()

token = sputil.prompt_for_user_token(username, scope)

if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.current_user_playing_track()
	print(results)
else:
	print("Can't get token for", username)