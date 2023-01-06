from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pw():

    pw_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    pw_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    pw_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)
    pw = "".join(password_list)
    pw_entry.insert(0, pw)
    pyperclip.copy(pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_e = website_entry.get()
    email_e = eu_entry.get()
    pw_e = pw_entry.get()

    if len(web_e) == 0 or len(pw_e) == 0:
        messagebox.showwarning(title="Empty Fields", message="Website or PW is empty")
    else:
        is_ok = messagebox.askokcancel(title=web_e, message=f"These are the details entered \nEmail: {email_e}\n"
                                                            f"Password: {pw_e}\nIs it OK to save?")

        if is_ok:
            with open(file="data.txt", mode="a") as data:
                data.write(f"{web_e} | {email_e} | {pw_e}\n")
                clear_entries()


def clear_entries():
    """
    Clears website and pw text field entries
    :return:
    """
    website_entry.delete(0, END)
    pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Upload Photo
photo = PhotoImage(file="logo.png")

# Configure and put Photo on screen
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Configure Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Configure Buttons
gen_pwd = Button(text="Generate Password", command=gen_pw)
gen_pwd.grid(column=2, row=3)
add = Button(text="Add", width=31, command=save_password)
add.grid(column=1, row=4, columnspan=2)

# Configure Text Input
website_entry = Entry(width=36)
website_entry.grid(columnspan=2, column=1, row=1, sticky=W)
website_entry.focus()
eu_entry = Entry(width=36)
eu_entry.grid(columnspan=2, column=1, row=2, sticky=W)
eu_entry.insert(0, "myemail@gmail.com")
pw_entry = Entry(width=28)
pw_entry.grid(column=1, row=3, sticky=W)

window.mainloop()
