# -----------------------------------------------------------
# This class have different types of methods to make little process
# and calculus
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
import random
from GameParameters import GameParameters
from Alien import Alien
from SpaceShip import SapaceShip
class Utils:

    #Function who returns a position in "X" who is multiple of the size of a block
    def getRandomNuMberForXPosition(self):
        number=random.randint(0, GameParameters.WINDOW_WIDTH)
        if number !=0 :
            if number % GameParameters.BLOCK_SIZE == 0:
                return number
            else:
                return self.getRandomNuMberForXPosition()

        else:
            return self.getRandomNuMberForXPosition()

    def printStats(self,aliens,spaceship):
        for alien in aliens :
            alien.toStringAlien()
        spaceship.toString()