# -----------------------------------------------------------
# This class manage the collisisions in the game
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------



from SpaceShip import SapaceShip
from Alien import Alien
from GameParameters import GameParameters
import pygame
class MouvementManager :
    def __init__(self,timeOfAlienMouvement):
        self.timeOfAlienMouvement=timeOfAlienMouvement


    def checkColisionBetweenAlienAndSapaceShip(self, spaceShip, aliens):

        for alien in aliens:
            if self.subCheckColisionBetweenAlienAndSpaceShip(spaceShip, alien) :
                spaceShip.decrementLifes()
                alien.die()

    def subCheckColisionBetweenAlienAndSpaceShip(self, spaceShip, alien):
        timeObject = pygame.time.get_ticks()
        if ((alien.x - 20) < spaceShip.x and (alien.x + 20) > spaceShip.x) and ((alien.y - 20) < spaceShip.y and (alien.y + 20) > spaceShip.y):
            #print(f"|Game|>>> Colision whith the alien {alien.id} in time ( {timeObject} )")
            return True
        else:
            #print(f"|Game|>>> No colision in time {timeObject}")
            return False

    def checkColisionBetweenAlienandMissil(self,aliens,missils,gc):
        for missil in missils:
            for alien in aliens:
                if self.subCheckColisionBetweenAlienAndMissil(alien,missil) :
                    alien.die()
                    missil.selfDestruction()
                    gc.incrementScore()


    def subCheckColisionBetweenAlienAndMissil(self,alien,missil):
        if ((alien.x - 20) < missil.x and (alien.x + 20) > missil.x) and ((alien.y - 20) < missil.y and (alien.y + 20) > missil.y):
            #print(f"|Game|>>> Colision whith the alien {alien.id} in time ( {timeObject} )")
            return True
        else:
            # print(f"|Game|>>> No colision in time {timeObject}")
            return False

