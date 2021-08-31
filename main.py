import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Read CSV file
data = pandas.read_csv("50_states.csv")

#Create dictionaries for each column in 50_states.csv
data_dict = data.to_dict()
state_dict = data_dict['state']
state_list = data.state.to_list()
x_dict = data_dict['x']
y_dict = data_dict['y']

#Create turtle to write out state names
state_marker = turtle.Turtle()
state_marker.hideturtle()
state_marker.penup()

#Variables to determine when game is complete
guessed_states = []
game_on = True


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="Please choose a state:").lower()

    for st in state_list:
        if st.lower() == answer_state:
            x = int(data[data.state == st].x)
            y = int(data[data.state == st].y)
            state_marker.goto(x, y)
            state_marker.write(st)
            guessed_states.append(st)

    if answer_state == "exit":
        missed_states = [st for st in state_list if st not in guessed_states]
        break

state_data = {"States Remaining": missed_states}
df = pandas.DataFrame(state_data)
df.to_csv("states not guessed")



state_marker.home()
state_marker.write("Congratulations! You guessed all the states!!", font=80)
game_on = False



