
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0",bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="questions goes here", font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.btn_1 = Button(image=true_img, highlightthickness=0)
        self.btn_1.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.btn_2 = Button(image=false_img, highlightthickness=0)
        self.btn_2.grid(row=2, column=1)

        self.window.mainloop()