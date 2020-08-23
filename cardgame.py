# creating a deck of cards and trying to create a game
import os,random,time

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Heart","Diomand","Spade","Club"]
deck =[]
value = 1
for i in ranks:
    for j in suits:
        deck.append([i+ ":of" +j , value])
    value += 1

random.shuffle(deck)
score = 0
card1 = deck.pop(random.randrange(len(deck)))
while True:
    os.system("cls")
    print("The current score is: ",score)
    print("/n/nThe card we got is  ",card1[0])
    choice = input("Higher or Lower")
    if choice in ["Higher","higher","High","high","H","h"]:
        choice = "h"
    elif choice in ["Lower","lower","Low","low","L","l"]:
        choice ="l"
    else:
        break

    card2 = deck.pop(random.randrange(len(deck)))
    print("The another card got is ",card2)
    time.sleep(1)

    if choice == "h" and card2[1]>>card1[1]:
        print("wrong choice")
        time.sleep(1)
    elif choice == "h" and card2[1]<<card1[1]:
        print("The choice is correct")
        score += 1
        time.sleep(1)
    elif choice == "l" and card2[1]>>card1[1]:
        print("The choice is correct")
        score += 1
        time.sleep(1)
    elif choice == "l" and card2[1]<<card1[1]:
        print("The choice is wrong")
        time.sleep(1)

    else:
        print("Both are same")
        card1==card2




