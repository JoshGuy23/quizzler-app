from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.new_question()

        self.window.mainloop()

    def new_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_true(self):
        self.quiz.check_answer("True")
        self.update_score()

    def answer_false(self):
        self.quiz.check_answer("False")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.new_question()
