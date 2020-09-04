# creating an hand game

import random

x1 = 1
x2 = 1

y1 = 1
y2 = 1
choice = random.randint(1,2)

def player_one(x1 , x2):
    right_finger1 = x1
    left_finger1  = x2
    return right_finger1 , left_finger1

def player_two(y1 , y2):
    right_finger2 = y1
    left_finger2  = y2
    return right_finger2 , left_finger2

print("Initially the player one finger" , player_one(x1 , x2))
print("Initially the player two finger" ,player_two(y1 , y2))

def win():
    globals()
    if right_finger1 == 0 and left_finger1 == 0:
        print("player two won")
    elif right_finger2 == 0 and left_finger2 == 0:
        print("player one won the match")
    return
def who_strtfirst():

    if choice%2 == 0:
        print("player one shall start the game")

    else:
        print("player two shall start the game")

    return

print(who_strtfirst())

while True:
    if choice%2 == 0:
        player_int = input("right or left")
        if player_int in ["right","Right","r","R"]:
            player_int = "y1"
            y1 += 1

            if y1 ==5:
                y1 = 0
            elif y1 == 6:
                y1 = 1

            elif y1 == 7:
                y1 = 2

            elif y1 == 8:
                y1 = 3

            elif y1 == 9:
                y1 =4

            elif y1 == 10:
                y1 = 0
                print("Y1 value is:", y1)


        elif player_int in ["left","Left","L","l"]:
            player_int = "y2"
            y2 += 1
            if y2 == 5:
                y2 = 0
            elif y2 == 6:
                y2 = 1

            elif y2 == 7:
                y2 = 2

            elif y2 == 8:
                y2 = 3

            elif y2 == 9:
                y2 = 4

            elif y2 == 10:
                y2 = 0
                print("Y1 value is:", y2)


    if choice%2 != 0:
        player_inT = input("right or left")
        if player_inT in ["right", "Right", "r", "R"]:
            player_inT = "x1"
            x1 += 1
            if x1 == 5:
                x1 = 0
            elif x1 == 6:
                x1 = 1

            elif x1== 7:
                x1 = 2

            elif x1 == 8:
                x1 = 3

            elif x1 == 9:
                x1 = 4

            elif x1 == 10:
                x1 = 0
            print(" X1 value is :",x1)

        elif player_inT in ["left", "Left", "L", "l"]:
            player_inT = "x2"
            x2 += 1
            if x2 == 5:
                x2 = 0
            elif x2 == 6:
                x2 = 1

            elif x2 == 7:
                x2 = 2

            elif x2 == 8:
                x2 = 3

            elif x2 == 9:
                x2 = 4

            elif x2 == 10:
                x2 = 0
            print(" X2 value is :",x2)























