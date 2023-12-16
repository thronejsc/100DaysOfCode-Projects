from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"


current_word = {}
to_learn = {}
# --------------- READ DATA FROM .CSV FILE  --------------- #
try:
    french_words = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = french_words.to_dict(orient="records")


# --------------- BUTTON FUNCTION  --------------- #


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_front, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def known_card():
    to_learn.remove(current_word)
    next_word()

    remaining_words = pandas.DataFrame(to_learn)
    remaining_words.to_csv("data/words_to_learn.csv", index=False)


# --------------- UI SETUP  --------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Text", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

card_back_img = PhotoImage(file="images/card_back.png")

canvas.grid(column=0, row=0, columnspan=2)

button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_word)
button_wrong.grid(column=0, row=1)

button_right_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, command=known_card)
button_right.grid(column=1, row=1)


next_word()
window.mainloop()
