from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.lbl_score = Label(text=f"Score: {self.quiz.score}",fg="white", bg=THEME_COLOR)
        self.lbl_score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Your question goes here",
            fill=THEME_COLOR,
            font=FONT
        )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.btn_true.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_question, text=f"You've reached the end of the quiz. Your final score is {self.quiz.score}")
            self.btn_false.config(state="disabled")
            self.btn_true.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


