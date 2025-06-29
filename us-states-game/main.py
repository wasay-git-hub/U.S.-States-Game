import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
screen.setup(width=700)
turtle.shape(img)
score = 0

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color("black")
scoreboard.teleport(0,235)
scoreboard.write(f"{score}/50", align="center", font=("Arial", 20, "bold"))

game_is_on = True
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title="Guess a State", prompt="What's another state's name?(Type 'exit' to Exit)").title()
    for state in states_list:
        if answer_state == "Exit":
            game_is_on = False
            break

        if answer_state == state and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            score += 1
            idx = states_list.index(state)
            x_val = x_list[idx]
            y_val = y_list[idx]

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.teleport(x_val,y_val)
            t.write(answer_state, align="center", font=("Arial", 10, "normal"))

            scoreboard.clear()
            scoreboard.teleport(0, 235)
            scoreboard.write(f"{score}/50", align="center", font=("Arial", 20, "bold"))

        if score >= 50:
            game_is_on = False
            break