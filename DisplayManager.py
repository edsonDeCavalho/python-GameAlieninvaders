# -----------------------------------------------------------
# This class is made to display elemnt (I diden not complete this class)
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

from GameParameters import GameParameters
from GameCharacteristics import GameCharacteristics
import pygame


class DisplayManager:
    #Displays the title
    def displayTitle(self,screen,background):
        font = pygame.font.SysFont(None, 50)
        img = font.render('Alien Invaders', True, GameParameters.WHITE)
        screen.blit(img, (390, 20))

    def displayScore(self,screen,aircraft,gc):
        font = pygame.font.SysFont(None, 40)
        img = font.render(f' Dead aliens : {gc.score}', True, GameParameters.WHITE)
        screen.blit(img, (20, 20))
        img2 = font.render(f' Lifes : {aircraft.life}', True, GameParameters.WHITE)
        screen.blit(img2, (20,70 ))

    def displayWelcome(self,screen):
        font = pygame.font.SysFont(None, 20)
        img = font.render('Welcome to <br> Aliens Attack ', True, GameParameters.WHITE)
        screen.blit(img, (1, 1))
