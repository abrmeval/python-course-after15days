import random
from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()

# Listening for key presses and binding them to functions
# screen.listen()

# def move_forward():
#     timmy.forward(10)

# def move_backward():
#     timmy.backward(10)

# Binding the space key to the move_forward function
# The key parameter specifies which key to listen for, and the fun parameter specifies the function to call when that key is pressed
# We pass a function as an input to other function
# screen.onkey(key="space", fun=move_forward)

# def left():
#     timmy.left(10)

# def right():
#     timmy.right(10)

# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()

# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=left)
# screen.onkey(key="d", fun=right)
# screen.onkey(key="c", fun=clear)

# Challenge Turtle race
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
is_race_on = False

turtles = {}
y_position = -100

for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=-230, y=y_position)
    y_position += 30

if user_bet:
    is_race_on = True

# while is_race_on:
#     random_distance = random.randint(0, 10)
#     rci = random.randint(0, 5)
#     turtles[colors[rci]].forward(random_distance)

while is_race_on:
    for key in turtles:
        random_distance = random.randint(0, 10)
        turtles[key].forward(random_distance)

        if turtles[key].xcor() > 230:
            if(key == user_bet):
                print("Congratulations! You won the bet! The " + key + " turtle is the winner!")
            else:
                print("Sorry, you lost the bet. The " + key + " turtle is the winner.")

            is_race_on = False
            break

# timmy = Turtle(shape="turtle")
# timmy.color("red")
# timmy.penup()
# timmy.goto(x=-230, y=-100)


screen.exitonclick()
