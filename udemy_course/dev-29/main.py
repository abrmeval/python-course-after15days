# import * does not import other modules, it only imports the names defined in the module.
from tkinter import *
from tkinter import messagebox
from password_gen import generate_password
import pyperclip
import pandas as pd

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    password = generate_password()
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)  # Copy the password to the clipboard so that the user can paste it into the password field of the website.

# ---------------------------- SAVE PASSWORD ------------------------------- #


def validate(username, password, website):
    any_errors = False
    message_field = ""
    if not username:
        message_field = "\t - The username must not be empty."
        any_errors = True
    if not password:
        message_field += "\t\n - The password must not be empty."
        any_errors = True
    if not website:
        message_field += "\t\n - The website must not be empty."
        any_errors = True

    if any_errors:
        messagebox.showerror(
            title="Invalid data", message=f"Please make sure all fields are filled:\n {message_field}"
        )

    return not any_errors


def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    data = pd.DataFrame(
        {"URL": [website], "Username": [username], "Password": [password]}
    )
    data.to_csv("data.csv", mode="a", sep="|", index=False, header=False)
    input_website.delete(0, END)
    input_username.delete(0, END)
    input_password.delete(0, END)


def save_file():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    if not validate(username, password, website):
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?",
    )
    messagebox.showerror
    if is_ok:
        with open("data.txt", mode="a", encoding="utf-8") as file:
            format = f"{website} | {username} | {password}\n"
            file.write(format)
            input_website.delete(0, END)
            input_username.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=200, height=200)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.config(justify="right")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.config(justify="right")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", justify="right")
password_label.grid(row=3, column=0)

input_website = Entry(width=35)
input_website.grid(
    row=1, column=1, sticky="ew", columnspan=2, padx=(10, 0), pady=(0, 5)
)
input_website.focus()
input_username = Entry(width=35)
input_username.insert(END, "example@outlook.com")
input_username.grid(
    row=2, column=1, padx=(10, 0), sticky="ew", columnspan=2, pady=(0, 5)
)
input_password = Entry(width=21)
input_password.grid(
    row=3, column=1, sticky="ew", columnspan=1, padx=(10, 0), pady=(0, 5)
)

generate_password_button = Button(text="Generate Password", command=new_password)
generate_password_button.grid(row=3, column=2, sticky="w", padx=(10, 0), pady=(0, 5))
add_button = Button(text="Add", width=36, command=save_file)
add_button.grid(row=4, column=1, sticky="ew", columnspan=2, padx=(10, 0))


window.mainloop()
