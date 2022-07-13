# -----------------------------------------------------------
# This class mangage the missils objects
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

from SpaceShip import SapaceShip
from Missil import Missil
from GameParameters import GameParameters
import pygame
class MissilsManager:

    def creationOfAMissil(self,spaceShip,missils):
        missil=Missil(spaceShip.x,spaceShip.y)
        missils.append(missil)
    def checkIfAMissilIsDestroyed(self,missil):
        return missil.isDestroyed()

    def moveMissil(self,missils):
            for missil in missils :
                missil.decrementationY()

    def removeMissils(self,missils):
        for missil in missils :
            if missil.isDestroyed():
                missils.remove(missil)
            #if missil.isGone():
                #missils.remove(missil)
    def checkIfMissilsIsGone(self, missils):
        for missil in missils:
            if (missil.y < 1):
                missil.gone = True

