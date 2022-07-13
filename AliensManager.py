# -----------------------------------------------------------
# This class manage the aliens
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------


from GameParameters import GameParameters
from Utils import Utils
from Alien import Alien
import pygame
class AliensManager:

    def __init__(self):
        self.utils=Utils()
    #Creates Aliens
    def createAliens(self,aliens,actualAlienId):
        # creation of an alien :

            alien = Alien(actualAlienId, self.utils.getRandomNuMberForXPosition(), 1)
            aliens.append(alien)
            actualAlienId += 1
    # It removes Aliens who are dead or who are in the bord of
    #the map
    def removeAliens(self,aliens):
        for alien in aliens:
            if not(alien.isAlive()) and (len(aliens))>0 :
                aliens.remove(alien)
            if alien.isGone() and (len(aliens))>0 :
                aliens.remove(alien)
    # Checks if an alien it's out of the map
    def checkIfAlienIsGone(self,aliens):
        for alien in aliens:
            if alien.y > GameParameters.WINDOW_HEIGHT :
                alien.gone=True
    # Moves evry alien
    def mouveAliens(self,aliens):

            for alien in aliens :
                alien.decrement()