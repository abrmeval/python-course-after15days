from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
SECONDS = 3
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"
FRENCH_WORDS_PATH = "data/french_words.csv"
timer = NONE
running = FALSE

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(400, 263, image=front_img)


def get_word_card():
    try:
        rdm_index = random.randint(0, len(data) - 1)
        return data[rdm_index]
    except:
        messagebox.showwarning(
            title="You already finished the word list",
            message="You finished learning the whole list of vocabulary. \nIt is GAME OVER.",
        )
        window.destroy()
        return {}


def remove_from_card_list(dict):
    data.remove(dict)
    data_frame = pd.DataFrame.from_records(data)
    data_frame.to_csv(WORDS_TO_LEARN_PATH, mode="w", index=False)


def show_next_card(word_card, lang="French"):
    global timer, running
    window.after_cancel(timer)

    canvas.itemconfig(background_img, image=front_img)
    canvas.itemconfig(language_text, text=lang, fill="black")
    canvas.itemconfig(word_text, text=word_card[lang], fill="black")

    timer = window.after(SECONDS * 1000, show_reverse_card, word_card)
    running = TRUE


def show_reverse_card(word_card, lang="English"):
    global running

    canvas.itemconfig(background_img, image=back_img)
    canvas.itemconfig(language_text, text=lang, fill="white")
    canvas.itemconfig(word_text, text=word_card[lang], fill="white")
    running = FALSE


def right_click():
    if running:
        return

    global current_card
    remove_from_card_list(current_card)

    new_card = get_word_card()

    if not new_card:
        return

    show_next_card(new_card)
    current_card = new_card


def left_click():
    if running:
        return

    new_card = get_word_card()

    if not new_card:
        return

    show_next_card(new_card)


language_text = canvas.create_text(
    400, 150, text="title", fill="black", font=("Arial", 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="word", fill="black", font=("Arial", 60, "bold")
)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, bd=0, command=right_click
)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=left_click)
left_button.grid(row=1, column=0)

try:
    data_frame = pd.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError as err:
    data_frame = pd.read_csv(FRENCH_WORDS_PATH)
except pd.errors.EmptyDataError as err:
    messagebox.showwarning(
        title="No progress found",
        message="No data was found from the last time played. \nProgress was reset.",
    )
    data_frame = pd.read_csv(FRENCH_WORDS_PATH)
finally:
    data = data_frame.to_dict(orient="records")

print(data)

current_card = get_word_card()
show_next_card(current_card)

window.mainloop()
