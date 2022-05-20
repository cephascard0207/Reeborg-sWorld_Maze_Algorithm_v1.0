# Reeborg'sWorld_Maze_Algorithm_v1.0
# Created by Cephas Cardozo
# Developed using Python

# functions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# loops
while front_is_clear():
    move()
while not at_goal():

  # conditionals
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()