
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, qb: QuizBrain):
        self.window = Tk()
        self.quiz_b = qb
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0",bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="questions goes here", font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.btn_1 = Button(image=true_img, highlightthickness=0, command=self.tru_ans)
        self.btn_1.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.btn_2 = Button(image=false_img, highlightthickness=0, command=self.fals_ans)
        self.btn_2.grid(row=2, column=1)
        self.get_question()

        self.window.mainloop()


    def get_question(self):
        question_is = self.quiz_b.next_question()
        self.canvas.itemconfig(self.question, text=question_is)

    def tru_ans(self):
        self.result(self.quiz_b.check_answer("True"))

    def fals_ans(self):
        self.result(self.quiz_b.check_answer("False"))

    def result(self, ans):
        if ans:
            print("True")
        else:
            print("False")

