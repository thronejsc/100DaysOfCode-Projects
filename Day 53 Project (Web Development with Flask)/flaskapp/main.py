from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def make_bold(function):
    def wrapper_bold():
        return f"<b>{function()}</b>"

    return wrapper_bold


def make_emphasis(function):
    def wrapper_emphasis():
        return f"<em>{function()}</em>"

    return wrapper_emphasis


def make_underlined(function):
    def wrapper_underlined():
        return f"<u>{function()}</u>"

    return wrapper_underlined


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
