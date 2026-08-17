from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_img)


language_text = canvas.create_text(
    400, 150, text="title", fill="black", font=("Arial", 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="word", fill="black", font=("Arial", 60, "bold")
)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=wrong_image, highlightthickness=0, bd=0)
left_button.grid(row=1, column=0)


window.mainloop()
