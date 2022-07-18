## game link 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    for _ in range(3):
        if right_is_clear():
            turn_right()
            move()
        else:
             break
    if front_is_clear():
        move()
    else :
        turn_left()