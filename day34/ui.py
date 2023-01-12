from tkinter import *

from day34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = self.setup_canvas()
        self.question_text = self.canvas.create_text(150, 125, text="TEXT", fill=THEME_COLOR, font=FONT, width=280)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, command=self.click_true)
        self.false_btn = Button(image=false_img, command=self.click_false)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.score_label = self.setup_label()

        self.quiz_brain = quiz_brain
        self.get_next_question()
        self.window.mainloop()

    def setup_canvas(self):
        canvas = Canvas(width=300, height=250)
        canvas.grid(row=1, column=0, columnspan=2, pady=50)
        return canvas

    def setup_label(self):
        label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        label.grid(column=1, row=0)
        return label

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz_brain.still_has_questions():
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz. Your final score "
                                                            f"is {self.quiz_brain.score}")

    def click_true(self):
        self.give_feedback(self.quiz_brain.check_answer("true"))

    def click_false(self):
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score_label.configure(text=f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.get_next_question)
