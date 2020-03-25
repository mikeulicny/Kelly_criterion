from coin import Coin, Face

class Player:
    """  Player interface for betting """
    def __init__(self, balance):
        if (balance <= 0):
            balance = 25.00     # default balance size
        else:
            self.balance = balance
        self.bet_size = None
        self.called = None

    def bet(self, bet_size):
         
        # cannot set bet below 0.01
        # betting more than account is considered "all in"
        if (bet_size < 0.01):
            self.bet_size = 0.01
        elif (bet_size > self.balance):
            self.bet_size = self.balance
        else:
            self.bet_size = bet_size

    def call(self, face):
        self.called = face 
