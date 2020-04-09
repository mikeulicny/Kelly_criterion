import os
import sys
from coin import Coin, Face
from player import Player

# used to clear multiple command line outputs
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def startGame():
    print('::::::::::::::: Kelly Criterion Game :::::::::::::::')
    print('            Press CTRL + C to exit game             ')
    print() # empty line
    
    player = Player(balance=25.00)
    player.call(Face.HEADS)
    player.bet(1.00)

    coin = Coin(weight=0.60)    # set weigthed coin to 60% heads 

    while True:
        line_count = 0
        # user interface
        print('Account size: ${0}'.format(player.balance))
        line_count += 1
        print('[1] BET: ${0}'.format(player.bet_size))
        line_count += 1
        if player.called == Face.HEADS:
            print('[2] CALL: HEADS')
        elif player.called == Face.TAILS:
            print('[2] CALL: TAILS')
        line_count += 1
        print('[ENTER] FLIP!')
        line_count += 1

        userInput = input("option: ")
        line_count += 1

        # option 1
        if (userInput == "1"):
            betInput = round(float(input("Bet size: $")), 2) # convert to float -> round to 2 decimals
            line_count += 1
            player.bet(betInput)
        
        # option 2
        elif (userInput == "2"):
            print("[H] Heads")
            line_count += 1
            print("[T] Tails")
            line_count += 1
            callInput = input(">")
            line_count += 1
            if (callInput == "H"):
                player.call(Face.HEADS)
            elif (callInput == "T"):
                player.call(Face.TAILS)

        # option ENTER
        elif (userInput == ""):
            
            # win
            if (coin.flip() == player.called): 
                player.balance += player.bet_size
            # loss
            else:
                player.balance -= player.bet_size 
                if player.bet_size > player.balance:
                    player.bet(player.balance)

        # clear account size and bet size lines
        for iter in range(0,line_count):
            sys.stdout.write(CURSOR_UP_ONE) # up a line
            sys.stdout.write(ERASE_LINE)    # erase line
        
        if (player.balance <=  0.00):
            print('Game over!')
            return False
    # end while
# end game
        
if __name__ == "__main__":
    startGame()
