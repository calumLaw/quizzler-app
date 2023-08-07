from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Canvas text

        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some text", font=FONT, fill="black")

        # Buttons
        self.tick = PhotoImage(file="images/true.png")
        self.red_x = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=self.tick, highlightthickness=0, command=self.select_true)
        self.correct_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_button = Button(image=self.red_x, highlightthickness=0, command=self.select_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        # Score label
        self.current_score = self.quiz.score
        self.score_label = Label(text=f"score: {self.current_score}", bg=THEME_COLOR, fg="white", font="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def select_true(self):
        if self.quiz.check_answer("True"):
            self.display_correct()
        else:
            self.display_false()
        self.current_score = self.quiz.score
        self.score_label.config(text=f"score: {self.current_score}", bg=THEME_COLOR, fg="white", font="white")

    def select_false(self):

        if self.quiz.check_answer("False"):
            self.display_correct()
        else:
            self.display_false()
        self.current_score = self.quiz.score
        self.score_label.config(text=f"score: {self.current_score}", bg=THEME_COLOR, fg="white", font="white")

    def display_correct(self):
        self.canvas.config(bg="green")
        self.window.after(1000, self.get_next_question)


    def display_false(self):
        self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
