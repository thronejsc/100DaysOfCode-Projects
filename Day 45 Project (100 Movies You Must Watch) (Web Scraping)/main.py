import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "html.parser")

movie_titles = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")

titles = [title.getText() for title in movie_titles]

with open("movies-to-watch.txt", "w") as file:
    for title in range(len(titles)-1, -1, -1):
        file.write(f"{titles[title]}\n")
