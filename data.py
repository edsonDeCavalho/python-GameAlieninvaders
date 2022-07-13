import time
import pygame
import random
import array as myarray
from SpaceShip import Veseaux
from colour import Color
#EXO5

#verifie si tout les modules sont charges
module_charge=pygame.init()
print(module_charge)

v=Veseaux()
print(v.x)


#cree une fenetre
#plein ecran
#ecran = pygame .display.set_mode((0,0,pygame.FULLSCREEN)
#petit ecran
ecran=pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Fighter 3000")
"""
image=pygame.image.load("logo.php").convert()
pygame.display.set_icon(image)
print(image)
"""

#boucle de jeu
loop=True
i=0
#positions
x=250
z=450

#positionObstacle
x1=random.randint(0, 250)
z1=1

ObstaclesX = myarray.array('d' , [random.randint(0, 500),random.randint(0, 500),random.randint(0, 500)])
ObstaclesZ = myarray.array('d', [1,1,1])

def colision(x1,z1,x,z):

    if ((x1-10) < x and  (x1+10) > x ) and ((z1-10) < z and (z1+10) > z) :
        print("colision")
        return True
    else :
        print("pas colision")
        return False

while loop:
    ecran.fill((0, 0, 0))
    #for ramdom object

    pygame.draw.circle(ecran, (0, 0, 100), (x1, z1), 10)

    timeObject = pygame.time.get_ticks()
    if timeObject % 400 == 0:
        z1=z1+40
        print("Hola")

    circle =pygame.draw.circle(ecran, (0,0,255), (x, z), 20)

   #control of key
    for event in pygame.event.get():
        #event input clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop=False
            if event.key == pygame.QUIT:
                loop=False
            if event.key == pygame.K_d:
                x=x+40
            if event.key == pygame.K_q:
                x=x-40
            if event.key == pygame.K_z:
                z=z-40
            if event.key == pygame.K_s:
                z=z+40
    #calcul colision
    colision(x1,z1,x,z)


    #affichage ecran
    pygame.display.flip()

#vide le cache
pygame.quit()




import time
import pygame

# TP de python 3/01/2022
#exo1 TP1
"""
EXO1
x=int(input("x: "))
for i in range(x):
    print(i)
"""


"""
EXO2
print("X+Y")
x=int(input("x: "))
y=int(input("y: "))
c=x+y
print(c)
"""

"""
EXO3
name =input("Enter a name:")
print(f"bonjour {name} comment va?")
"""

"""
EXO4
password =input("Type de password please: ")
p="1234"
if password==p :
    print("Password correcte")
else :
    print("Password incorrecte")

"""

#EXO5

#verifie si tout les modules sont charges
module_charge=pygame.init()
print(module_charge)

#cree une fenetre
#plein ecran
#ecran = pygame .display.set_mode((0,0,pygame.FULLSCREEN)
#petit ecran
ecran=pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Invader 3000")
"""
image=pygame.image.load("logo.php").convert()
pygame.display.set_icon(image)
print(image)
"""

#boucle de jeu
loop=True
i=0
while loop:
    #ecran.blit(image,(250,250))
    #pyga event
    ecran.fill((0,0,0))
    i=i+1
    circle =pygame.draw.circle(ecran,(0,0,255),(i,250),20)
    if i==615:
        i=0
    for event in pygame.event.get():
        #event input clavier
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_j:
                loop=False
        if event.type==pygame.QUIT:
                loop=False
    #affichage ecran
    pygame.display.flip()

#vide le cache
pygame.quit()




import time
import pygame

# TP de python 3/01/2022
#exo1 TP1
"""
EXO1
x=int(input("x: "))
for i in range(x):
    print(i)
"""


"""
EXO2
print("X+Y")
x=int(input("x: "))
y=int(input("y: "))
c=x+y
print(c)
"""

"""x
EXO3
name =input("Enter a name:")
print(f"bonjour {name} comment va?")
"""

"""
EXO4
password =input("Type de password please: ")
p="1234"
if password==p :
    print("Password correcte")
else :
    print("Password incorrecte")

"""

#EXO5

#verifie si tout les modules sont charges
module_charge=pygame.init()
print(module_charge)

#cree une fenetre
#plein ecran
#ecran = pygame .display.set_mode((0,0,pygame.FULLSCREEN)
#petit ecran
ecran=pygame.display.set_mode((500,500))
pygame.display.set_caption("Space Invader 3000")
"""
image=pygame.image.load("logo.php").convert()
pygame.display.set_icon(image)
print(image)
"""

#boucle de jeu
loop=True
i=0
while loop:
    #ecran.blit(image,(250,250))
    #pyga event
    ecran.fill((0,0,0))
    i=i+1
    circle =pygame.draw.circle(ecran,(0,0,255),(i,250),20)
    if i==615:
        i=0
    for event in pygame.event.get():
        #event input clavier
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_j:
                loop=False
        if event.type==pygame.QUIT:
                loop=False
    #affichage ecran
    pygame.display.flip()

#vide le cache
pygame.quit()










