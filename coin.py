from enum import Enum
import random

class Coin:
    """ Coin object for testing kelly criterion """
    def __init__(self, weight):
        self.weight = weight

    def flip(self):
        result = random.random()
        if (result <= self.weight):
            return Face.HEADS
        else:
            return Face.TAILS
               
# coin class

class Face(Enum):
    HEADS = 1
    TAILS = 2
# face class
