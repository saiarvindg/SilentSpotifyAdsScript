# SilentSpotifyAdsScript
Mute Spotify ads

## Workflow
1) Use Spotify API to get currently playing song and store the remaining time
2) Calculate the time for the next song to start
3) If the current track is an ad - then continue to next steps. Else skip to step 8
3) ~~Set volume to 0 (with Spotify's Beta Web API) when current playing song is not a song~~ (apparently a premium only feature 😔)
4) Use AppleScript to get the application volume of Spotify and save it
5) Use AppleScript to set the application volume of Spotify to 0
6) Wait for the ad to finish
7) Use AppleScript to set the application volume of Spotify to what it was
8) Go to step 1

## Special cases to handle:
- if the user starts spotify muted - then `STORED_VOL` will start out as 0
- how to set `STORED_VOL` when music first played
- negative volume issue after ad plays

## TODO (after basic workflow is done):
- Handling special cases
- Add logging so print statements are logged to file not stdout
- Fix print/log statements, grammar/spelling, 
- Maybe improve code (add constants for equality checks, methods to handle parsing/formatting, fix package imports)
