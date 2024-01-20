from bs4 import BeautifulSoup
import requests

# with open("./website.html", encoding='utf-8') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# headings = soup.findAll(id="name")
#
# for head in headings:
#     print(head.getText())


url = "https://news.ycombinator.com/"

response = requests.get(url=url)
hacker_news_webpage = response.text

soup = BeautifulSoup(hacker_news_webpage, "html.parser")

article_titles = soup.findAll(name="span", class_="titleline")
article_upvotes = soup.findAll(class_="score")

titles = [title.getText() for title in article_titles]
links = [link.find("a").get("href") for link in article_titles]
upvotes = [int(upvote.getText().split()[0]) for upvote in article_upvotes]

# for article_tag in article_titles:
#     article_text = article_tag.getText()
#     article_link = article_tag.find("a").get("href")
#     # print(article_tag)
#     print(article_text)
#     print(article_link)



# for i in article_upvotes:
#     upvote = i.getText()
#     upvotes.append(upvote)
print(titles)
print(links)
print(upvotes)

print(max(upvotes))

max_upvote = max(upvotes)
index_max_upvote = upvotes.index(max(upvotes))

print(titles[index_max_upvote])
print(links[index_max_upvote])
print(upvotes[index_max_upvote])

