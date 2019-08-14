import os
import sys
from pathlib import Path
import spotipy.util as sputil
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
username = os.getenv("USERNAME")
redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")
scope = 'user-read-currently-playing user-modify-playback-state'

def check_env_set():
	return client_id and client_secret and username and redirect_url

def get_auth_token():
	token = sputil.prompt_for_user_token(username, scope)
	if token:
		return True, "Token retrieved successfully", token
	else:
		return False, "Can't get token for" + username, ""