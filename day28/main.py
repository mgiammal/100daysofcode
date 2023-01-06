import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ONE_MIN_SEC = 60
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mrk.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * ONE_MIN_SEC
    short_break_time = SHORT_BREAK_MIN * ONE_MIN_SEC
    long_break_time = LONG_BREAK_MIN * ONE_MIN_SEC

    if reps % 8 == 0:
        # 8th long break
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        # 2/4/6 short break
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_time)
    else:
        # 1/3/7 work
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min_left = math.floor(count / 60)
    sec_left = count % 60

    sec_left = f"0{sec_left}" if sec_left < 10 else sec_left

    canvas.itemconfig(timer_text, text=f"{min_left}:{sec_left}")
    if count > 0:
        global timer
        window.lift()
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mrk.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Upload Photo
photo = PhotoImage(file="tomato.png")

# Configure and put Photo on screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Buttons
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mrk = Label(fg=GREEN, bg=YELLOW)
check_mrk.grid(column=1, row=3)

window.mainloop()
