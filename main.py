import os
import sys
from coin import Coin, Face

# used to clear multiple command line outputs
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def startGame():
    print('::::::::::::::: Kelly Criterion Game :::::::::::::::')
    print('            Press CTRL + C to exit game             ')
    print() # empty line
    cash = 25.00
    coin = Coin(weight=0.60)    # set weigthed coin to 60% heads 

    while True:
        # user interface
        print('Account size: ${0}'.format(cash))
        betInput = input("Bet size: $")
        bet = float(betInput)
        bet = round(bet, 2)     # round to 2 decimal places

        # prevent user from wagering more than account size
        if (bet > cash):
            bet = cash
        # prevent user from wagering negative or 0
        elif (bet < 0.01):
            bet = 0.01
        
        if (coin.flip() == Face.HEADS):
            cash += bet     # heads pays
            print('Result: Heads | last bet ${0} |  won ${0}'.format(bet))
        else:
            cash -= bet     # tails lose
            print('Result: Tails | last bet ${0} | lost ${0}'.format(bet))

        # clear account size and bet size lines
        sys.stdout.write(CURSOR_UP_ONE) # up to result line
        sys.stdout.write(CURSOR_UP_ONE) # up to bet line
        sys.stdout.write(ERASE_LINE)    # erase bet line
        sys.stdout.write(CURSOR_UP_ONE) # up to account size line
        sys.stdout.write(ERASE_LINE)    # erase account size line

        if (cash == 0.00):
            print('Game over!')
            return False
    # end while
# end game
        
if __name__ == "__main__":
    startGame()
