import pandas as pd
import turtle
FONT = ('Courier', 8, 'normal')

# Adding the screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading CSV data
data = pd.read_csv("50_states.csv")
states = list(data.state)

count = 0
guessed_list = []


game_is_on=True
while game_is_on:
    # Adding title, getting state name from the user
    answer_state = screen.textinput(title=f" {count}/50 States Correct:", prompt="What is the another state?")
    answer_state = answer_state.title()

    # Key word to exit from the game
    if answer_state == "Exit":
        break

    # Placing the states to correct coordinates
    if answer_state in states:
        x_cor1 = data[data.state == answer_state]
        x_cor = int(x_cor1.x)
        y_cor1 = data[data.state == answer_state]
        y_cor = int(y_cor1.y)
        
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.color("black")
        text.penup()
        text.goto(x_cor, y_cor)
        text.write(answer_state, align="center", font=FONT)

        guessed_list.append(answer_state)
        count +=1
        if count == 50:
            game_is_on = False

# Creating the CSV data for unpredicted states
states_to_learn = list(set(states) - set(guessed_list))
x_learn= []
y_learn = []
for state in states_to_learn:
    state_data = data[data.state == state]
    x_learn.append(int(state_data.x))
    y_learn.append(int(state_data.y))

learn_dict = {"state":states_to_learn,
              "x":x_learn,
              "y":y_learn}

learn_data = pd.DataFrame(learn_dict)
learn_data.to_csv("states_to_learn.csv")

