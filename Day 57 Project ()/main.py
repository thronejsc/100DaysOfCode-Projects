from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
all_blogs = requests.get(url=url).json()
blog_objects = []

for blog in all_blogs:
    post = Post(blog["id"], blog["body"], blog["title"], blog["subtitle"])
    blog_objects.append(post)


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_objects)


@app.route('/blog/<int:num>')
def get_blog(num):
    for blog_post in blog_objects:
        if blog_post.id == num:
            return render_template('post.html', blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
