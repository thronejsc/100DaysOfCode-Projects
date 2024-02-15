from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date as d


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class BlogForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle",validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    results = db.session.execute(db.select(BlogPost)).scalars().all()
    if results:
        for post in results:
            post_json = {
                "id": post.id,
                "title": post.title,
                "subtitle": post.subtitle,
                "date": post.date,
                "body": post.body,
                "author": post.author,
                "img_url": post.img_url,
            }
            posts.append(post_json)
        
        return render_template("index.html", all_posts=posts)
    else:
        not_found = {
            "error": {
                "Not Found": "There are no cafes in the database"
            }
        }
        return not_found
    

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=d.today().strftime('%B %d, %Y'),
            author=form.author.data,
            body=form.body.data,
            img_url=form.img_url.data
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edit_form = BlogForm()
    edit_form.title.data = post_to_edit.title
    edit_form.subtitle.data = post_to_edit.subtitle
    edit_form.author.data = post_to_edit.author
    edit_form.img_url.data = post_to_edit.img_url
    edit_form.body.data = post_to_edit.body

    if edit_form.validate_on_submit():
        post_to_edit.title = request.form['title']
        post_to_edit.subtitle = request.form['subtitle']
        post_to_edit.author = request.form['author']
        post_to_edit.body = request.form['body']
        post_to_edit.img_url = request.form['img_url']
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template('make-post.html', form=edit_form, edit_head="Edit Post")


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5005)
