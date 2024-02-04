from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/48ab47c49e2c5f566c59"
blogs = requests.get(url=url).json()

@app.route('/')
def home():
    return render_template('./index.html', blogs=blogs)

@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/sample')
def sample_post():
    return render_template('./post.html')

@app.route('/contact')
def contact():
    return render_template('./contact.html')

@app.route('/post/<int:num>')
def get_post(num):
    requested_post = None
    for blog in blogs:
        if blog['id'] == num:
            requested_post = blog
    return render_template('./post.html', blog=requested_post)
                                    

if __name__ == "__main__":
    app.run(debug=True)