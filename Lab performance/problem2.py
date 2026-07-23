
player1 = 0
player2 = 0

while True:

    dice = int(input("Player 1: "))

    if player1 + dice <= 24:
       player1 = player1 + dice

    if player1 == 24:
        print("Player 1 wins")
        break

    dice = int(input("Player 2: "))

    if player2 + dice <= 24:
        player2 = player2 + dice

    if player2 == 24:
        print("Player 2 wins")
        break    


