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
marks = ""
timer = None
is_running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")

    global is_running
    global reps
    reps = 0
    is_running = False

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global is_running
    global reps

    if is_running:
        return
    
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    reps += 1
    is_running = True

    if reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_sec)
    else:
        count_down(short_sec)
        title_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global marks

    count_mins = count // 60
    count_seconds = count % 60

    # Updates the text of an item in a canvas
    canvas.itemconfig(timer_text, text=f"{count_mins:02d}:{count_seconds:02d}")
    global timer

    if count > 0:
        # Calls a function after an amount of time
        timer = window.after(1000, count_down, count - 1)

    else:
        if reps % 2 == 1:
            marks = marks + "✔️"
            check_label.config(text=marks)

        timer = window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 30), fg=GREEN)
title_label.config(bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 11), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 11), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 8), fg=GREEN)
check_label.config(bg=YELLOW)

check_label.grid(row=3, column=1)


window.mainloop()
