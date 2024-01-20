from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ec02da87a454498c93d0ac8ccc2949a7"
CLIENT_SECRET = "32ed70e0b88d4b7195ae4f2bfb433b2d"
USERNAME = '31vorrup7io3vcsqwaf23t32dv3y'

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/2000-08-12/'

response = requests.get(url=BILLBOARD_URL)
billboard_web = response.text

soup = BeautifulSoup(billboard_web, "html.parser")

# songs = soup.findAll(name='h3', id="title-of-a-story")

songs = soup.findAll(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
song_titles = [title.find("h3").getText().strip() for title in songs]

print(song_titles)
print(len(song_titles))







sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               username=USERNAME))


year_to_go = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD ")






