# Creating tic tac toe game player vs player

boardgame = {'7':' ','8':' ','9':' ',
             '4':' ','5':' ','6':' ',
             '1':' ','2':' ','3':' '}

board_keys = []
for key in boardgame:
    board_keys.append(key)


def formingboard(x):
    print(x['7'] + '|' + x['8'] + '|' +x['9'])
    print('-+-+-')
    print(x['4'] + '|' + x['5'] + '|' + x['6'])
    print('-+-+-')
    print(x['1'] + '|' + x['2'] + '|' + x['3'])

print(formingboard(boardgame))

def game():
    turn = 'x'
    count = 0

    for i in range(9):
        formingboard(boardgame)
        print("Its your turn "+turn+"move to which place?")
        move = input("Enter the place")

        if boardgame[move] == ' ':
            boardgame[move] = turn
            count += 1


        else:
            print("The place is occupied enter a valid place")
            continue

        if count>=5:
            if boardgame['7'] == boardgame['8'] == boardgame['9'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break


            elif boardgame['4'] == boardgame['5'] == boardgame['6'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['1'] == boardgame['2'] == boardgame['3'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['7'] == boardgame['4'] == boardgame['1'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['8'] == boardgame['5'] == boardgame['2'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['9'] == boardgame['6'] == boardgame['3'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['7'] == boardgame['5'] == boardgame['3'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break

            elif boardgame['9'] == boardgame['5'] == boardgame['1'] != ' ' :
                print("\nGAME OVER\n")
                print("fuck you"+turn+"won.")
                break


        if count == 9:
            print("\nGAME OVER\n")
            print("It's a tie")


        if turn == 'x':
            turn = 'o'

        else:
            turn = 'x'

    restart = input("Do you want to play again? enter('y' or 'n')")
    if restart == "Y" or restart == "y":
        for key in board_keys:
            boardgame[key] = " "
        game()


game()












