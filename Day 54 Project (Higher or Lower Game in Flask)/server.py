from flask import Flask
from random import randint

app = Flask(__name__)


def is_correct(function):
    random_number = randint(0, 9)

    def wrapper(**kwargs):
        if kwargs["number"] == random_number:
            return function(**kwargs)
        elif kwargs["number"] > random_number:
            return ("<h1>It's Too High</h1>"
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGdrdTI0dmxpNmQ0OW9nemtuOHF2a2czMWhpbDBxNWhuNnowYmhiNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ijgLeINIH40Jor6TD1/giphy.gif'>")
        else:
            return ("<h1>It's Too Low</h1>"
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDN1ZGVoZmdoa2ZuOGpkczBiNXlqeTVxcDljNG1tZmMzMGRhOXZjbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dKpEvFHdGsZBRuszpv/giphy.gif'>")
    return wrapper


@app.route("/")
def hello_world():

    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:number>")
@is_correct
def correct(number):
    return (f"<h1 color:green>You're Correct! The correct answer is {number}</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGJicWVodTc0bTdmOWQ4MmsydGIxNzB1N2Y4eHBsZzBrbWF4ZnRjZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gffcSKwGREETNo9rsy/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)