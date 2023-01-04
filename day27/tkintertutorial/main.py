from tkinter import *


def button_clicked():
    my_label.config(text=my_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Create a Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Create a Button
button = Button(text="Click Here", command=button_clicked)
button.grid(column=1, row=1)

# Create a second Button
button = Button(text="Click Here")
button.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()


