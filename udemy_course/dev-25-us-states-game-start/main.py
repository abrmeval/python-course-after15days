import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# We load an image of the U.S map and set it as the background of the turtle screen.
# The image is in GIF format, which is supported by the turtle graphics library.
image = "blank_states_img.gif"
screen.addshape(image)
# We set the shape of the turtle to the image of the U.S map.
# This allows us to use the turtle graphics library to draw on top of the map and interact with it.
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


def set_state(x, y, name):
    score_board = turtle.Turtle()
    score_board.hideturtle()
    score_board.penup()
    score_board.color("black")
    score_board.setposition(x, y)
    score_board.write(name, move=False, align="center")


guessed_states = {}
score = 0
while True:
    # We prompt the user and read the input then we convert the input to title case using the title() method.
    answer_state = screen.textinput(
        title=f"Guess the State ({score}/50)", prompt="What's another state's name?"
    ).title()
    print(answer_state)

    row = data[data["state"] == answer_state]
    print(row)

    if not row.empty and answer_state not in guessed_states:
        # dict = row.to_dict()
        # iloc is used to access the first row of the DataFrame, and we extract the x, y coordinates and state name from that row.
        print((row.iloc[0]["x"], row.iloc[0]["y"], row.iloc[0]["state"]))
        set_state(row.iloc[0]["x"], row.iloc[0]["y"], row.iloc[0]["state"])
        guessed_states[answer_state] = True
        score += 1

    if score == 50:
        turtle.Turtle().write(
            "Congratulations! You guessed all the states!",
            move=False,
            align="center",
            font=("Arial", 16, "bold"),
        )
        break

pandas.DataFrame({"Score": [score]}).to_csv("score.csv", index=False)

# This code is to get the x and y coordinates of the mouse click on the turtle screen.

# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# This line is used to keep the turtle graphics window open and responsive to user input.
# It starts the event loop that listens for events such as mouse clicks and keyboard input.
#  Without this line, the window would close immediately after the program finishes executing.
turtle.mainloop()

# screen.exitonclick()
