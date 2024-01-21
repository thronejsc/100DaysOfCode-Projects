from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ["YOUR_CLIENT_ID"]
CLIENT_SECRET = ["YOUR_CLIENT_SECRET"]
USERNAME = ["YOUR_SPOTIFY_USERNAME"]

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100'
# 2000-08-12

date = input("Which year do you want to travel to? Type the date in this format, YYYY-MM-DD: ")

response = requests.get(url=f"{BILLBOARD_URL}/" + date)
billboard_web = response.text

soup = BeautifulSoup(billboard_web, "html.parser")


songs = soup.findAll(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
song_number_one = soup.find("h3").getText().strip()
song_titles = [title.find("h3").getText().strip() for title in songs]
song_titles.insert(0,song_number_one)

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               username=USERNAME))


results = spotify.current_user()
USER_ID = results['id']

song_uris = [spotify.search(title)['tracks']['items'][0]['uri'] for title in song_titles]

PLAYLIST_ID = spotify.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public="false", description=f"Top 100 Billboard songs of {date}")['id']

# add songs  to the playlist

spotify.playlist_add_items(PLAYLIST_ID, items=song_uris)






