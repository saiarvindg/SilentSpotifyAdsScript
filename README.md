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

