from tkinter import *


def calculate():
    user_input = float(my_input.get())
    kilometers = round(1.609 * user_input)
    result.config(text=f"{kilometers}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=50, pady=20)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=20)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

my_input = Entry(width=10)
my_input.grid(column=1, row=0)
my_input.insert(END, string="0")

window.mainloop()
