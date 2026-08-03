from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
input_website.grid(row=1, column=1, sticky="ew", columnspan=2, padx=(10, 0), pady=(0, 5))
input_username = Entry(width=35)
input_username.grid(
    row=2, column=1, padx=(10, 0), sticky="ew",columnspan=2, pady=(0, 5)
)
input_password = Entry(width=21)
input_password.grid(row=3, column=1, sticky="ew", columnspan=1, padx=(10, 0), pady=(0, 5))

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="w", padx=(10, 0), pady=(0, 5))
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, sticky="ew",columnspan=2, padx=(10, 0))


window.mainloop()
