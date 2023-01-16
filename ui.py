from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300,
                             height=250,
                             highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                text="test",
                                font=("Arial", 20, "italic"),
                                width=280)
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        self.score_label = Label(text="Score: 0",
                                 bg=THEME_COLOR,
                                 foreground="white",
                                 pady=10,
                                 padx=10)
        self.score_label.grid(column=1, row=0)

        # Add True/False Buttons
        right_image = PhotoImage(file="./images/true.png")
        self.right = Button(image=right_image,
                            highlightthickness=0,
                            border=0,
                            activebackground="white",
                            command=self.user_guess_true)
        self.right.grid(column=0, row=2)
        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image,
                            highlightthickness=0,
                            border=0,
                            activebackground="pink",
                            command=self.user_guess_false)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game.")
            self.wrong.config(state="disabled")
            self.right.config(state="disabled")

    def user_guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_guess_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


