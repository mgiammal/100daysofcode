from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
save_file = "data/words_to_learn.csv"
language_file = "data/italian_words.csv"
cur_card = {}
omit_list = []


def load_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card = random.choice(language_data)
    canvas.itemconfig(rand_word, text=f"{cur_card.get('Italian')}", fill="black")
    canvas.itemconfig(cur_language, text=f"Italian", fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, func=change_card)


def change_card():
    canvas.itemconfig(rand_word, text=f"{cur_card.get('English')}", fill="white")
    canvas.itemconfig(cur_language, text=f"English", fill="white")
    canvas.itemconfig(card_img, image=card_bck_img)


def save_progress():
    language_data.remove(cur_card)
    pandas.DataFrame(language_data).to_csv(save_file, index=False)
    load_card()


try:
    data = pandas.read_csv(save_file)
except FileNotFoundError:
    data = pandas.read_csv(language_file)
    print(data)
finally:
    language_data = pandas.DataFrame(data).to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, load_card)

# Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_bck_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
cur_language = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
rand_word = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
x_img = PhotoImage(file="images/wrong.png")
x_btn = Button(image=x_img, highlightthickness=0, command=load_card)
x_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=save_progress)
right_btn.grid(row=1, column=1)

# Load first card
load_card()

window.mainloop()
