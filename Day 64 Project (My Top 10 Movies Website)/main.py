from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

api_key = os.environ.get("TMDB_API_KEY")


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZmY4YzhlZTY4NmExYjdiMzNmZWIxMjU2MjdlNTcwYyIsInN1YiI6IjY1Yzc4Mzk5YWFkOWMyMDE2NGI2MGYxOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.IOVMYvn4TT1JRMOM2XOByrzZLVQD8_gyzus6d4aUjZ4"
}


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-10-movies.db"
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(100), nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    
# new_movie = Movie(
#     title="MEgamind 2",
#     year=2007,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
# CREATE TABLE

with app.app_context():
    db.create_all()


class MovieForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Done')
    
    
class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by((Movie.ranking).desc()))
    all_movies = result.scalars()
    return render_template("index.html", all_movies=all_movies)


@app.route('/add', methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        search_movie_endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
         "query": form.title.data
        }
        response = requests.get(url=search_movie_endpoint, params=params, headers=headers)
        all_movies = response.json()['results']
        print(all_movies)
        return render_template('select.html', all_movies=all_movies)
        
    return render_template('add.html', form=form)
    
@app.route('/movie-details')
def movie_details():
    movie_id = request.args.get("id")
    if movie_id:
        movie_endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "language": "en-US"
        }
        response = 
        

@app.route('/edit-<int:id>', methods= ["GET", "POST"])
def edit(id):
    form = MovieForm()
    if form.validate_on_submit():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html', form=form)


@app.route('/delete-<int:id>')
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))
    
    

if __name__ == '__main__':
    app.run(debug=True)
