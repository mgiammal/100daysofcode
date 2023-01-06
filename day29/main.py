from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_e = website_entry.get()
    email_e = eu_entry.get()
    pw_e = pw_entry.get()

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
gen_pwd = Button(text="Generate Password")
gen_pwd.grid(column=2, row=3)
add = Button(text="Add", width=31, command=save_password)
add.grid(column=1, row=4, columnspan=2)

# Configure Text Input
website_entry = Entry(width=36)
website_entry.grid(columnspan=2, column=1, row=1)
website_entry.focus()
eu_entry = Entry(width=36)
eu_entry.grid(columnspan=2, column=1, row=2)
eu_entry.insert(0, "myemail@gmail.com")
pw_entry = Entry(width=18)
pw_entry.grid(column=1, row=3)

window.mainloop()
