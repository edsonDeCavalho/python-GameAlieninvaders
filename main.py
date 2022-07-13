# -----------------------------------------------------------
# Project for Phython class "Aliens Attack"
#
# Edson De Carvalho, Paris, France
#
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

import time
import pygame
import random
import array as myarray
from SpaceShip import SapaceShip
from MovementManager import MouvementManager
from Alien import Alien
from AliensManager import AliensManager
from GameCharacteristics import GameCharacteristics
from GameParameters import GameParameters
from Utils import Utils
from SapaceShipManager import SapaceShipManager
from Missil import Missil
from MissilsManager import MissilsManager
from DisplayManager import DisplayManager




#Window variables:

#verifie si tout les modules sont charges
module_charge=pygame.init()
print(module_charge)
loop=True
pygame.display.set_caption("Space Fighter 3000")

#Game Characteristics : is the oject who stores the parameters of the actual round
gameCharacteristics=GameCharacteristics(GameParameters.DEFAULT_NUMBER_OF_ALIENS,GameParameters.DEFAULT_TIME_OF_ALIENS_MOUVEMENT);


#Game objects variables
aircraft=SapaceShip(GameParameters.DEFAULT_POSITION_X,GameParameters.DEFAULT_POSITION_Y,"Edson")
movementManager=MouvementManager(gameCharacteristics.timeOfAlienMouvement)

#Storage of aliens and Missils
aliens = []
missils = []
actualAlienId=0

#Creation of the classes who manage evry data object

spaceShipManager=SapaceShipManager()
utils=Utils()
aliensMananager=AliensManager()
missilsManager=MissilsManager()
displayManager=DisplayManager()

#Charge of images
alienImage = pygame.image.load(GameParameters.ALIEN_IMAGE_PATH)
spaceShipImage = pygame.image.load(GameParameters.SPACESHIP_IMAGE_PATH)
missilImage=pygame.image.load(GameParameters.MISSIL_IMAGE_PATH)
background=pygame.image.load(GameParameters.WiNDOW_BACKGROUND_IMAGE_PATH)

#Booleans to control the diffrent lunch of the game
step1=True



#Drawing Missils
def drawMissils():
    for i in range(len(missils)):
        #pygame.draw.circle(screen, GameParameters.BROWN, (missils[i].x, missils[i].y), 10)
        screen.blit(missilImage, (missils[i].x, missils[i].y))
#Drawing Aliens
def drawAliens():
    for i in range(len(aliens)):
        screen.blit(alienImage, (aliens[i].x, aliens[i].y))
        #pygame.draw.circle(screen, GameParameters.BROWN, (aliens[i].x, aliens[i].y), GameParameters.ALIEN_SIZE)
#Draw the spaceship
def drawSpaceShip():
    screen.blit(spaceShipImage, (aircraft.x, aircraft.y))
    #pygame.draw.circle(screen, GameParameters.WHITE, (aircraft.x, aircraft.y), GameParameters.SAPACESHIP_SIZE)
#Draw the grid in the screen
def drawGrid():
    screen.fill(GameParameters.BLACK)
    for x in range(0, GameParameters.WINDOW_WIDTH, GameParameters.BLOCK_SIZE):
        for y in range(0,GameParameters.WINDOW_HEIGHT, GameParameters.BLOCK_SIZE):
            rect = pygame.Rect(x, y, GameParameters.BLOCK_SIZE, GameParameters.BLOCK_SIZE)
            pygame.draw.rect(screen, GameParameters.BLACK, rect, 1)

#Initialises the screen
def init(ndAliens):
    global screen,clock,actualAlienId
    pygame.init()
    screen = pygame.display.set_mode((GameParameters.WINDOW_WIDTH,GameParameters.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(GameParameters.BLACK)
    for i in range(ndAliens):
        #creation of an alien :
        alien = Alien(actualAlienId,utils.getRandomNuMberForXPosition(), 1)
        aliens.append(alien)
        actualAlienId += 1

#drawAliens()
init(gameCharacteristics.numberOfAliens)
drawGrid()
while loop:
    #Call of the drawing fonctions:

    drawGrid()
    screen.blit(background, [0, 0])
    #Display of text
    displayManager.displayTitle(screen, background)
    displayManager.displayScore(screen,aircraft,gameCharacteristics)
    drawAliens()
    drawSpaceShip()
    drawMissils()

    for event in pygame.event.get():
        #event input Keyboard and call for mouvement or another action
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
            if event.key == pygame.QUIT:
                loop = False
            if event.key == pygame.K_d:
                spaceShipManager.moveToRightSpaceSHip(aircraft)
            if event.key == pygame.K_q:
                spaceShipManager.moveToLeftSpaceSHip(aircraft)
            if event.key == pygame.K_z:
                spaceShipManager.moveToUpSpaceSHip(aircraft)
            if event.key == pygame.K_s:
                spaceShipManager.moveToDownSpaceSHip(aircraft)
            if event.key == pygame.K_g:
                missilsManager.creationOfAMissil(aircraft,missils)


    #creation of Aliens
    aliensMananager.createAliens(aliens,actualAlienId)
    #Check aliens colision
    movementManager.checkColisionBetweenAlienAndSapaceShip(aircraft, aliens)
    #Check collision between aliens and missils
    movementManager.checkColisionBetweenAlienandMissil(aliens,missils,gameCharacteristics)
    #check if a alien is gone or dead
    aliensMananager.checkIfAlienIsGone(aliens)
    #Checking if a lien is gone
    missilsManager.checkIfMissilsIsGone(missils)
    #removing aliens who are dead or are gone
    aliensMananager.removeAliens(aliens)
    #removing missils who are dead
    missilsManager.removeMissils(missils)
    #Call of no player mouvements
    aliensMananager.mouveAliens(aliens)
    #Calling the mouvement of the missils
    missilsManager.moveMissil(missils)
    #print stats of the last Frame
    #utils.printStats(aliens,aircraft)
    pygame.display.flip()
    #Settig the frame clock
    clock.tick(GameParameters.DEFAULT_FRAME_BY_SECOND)

    if aircraft.isDead():
        pygame.quit()


#vide le cache

pygame.quit()


