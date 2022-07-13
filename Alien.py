# -----------------------------------------------------------
# This class represents an Alien
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
from GameParameters import GameParameters
class Alien:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.alive=True
        self.gone=False
    def decrement(self):
        self.y=self.y+GameParameters.BLOCK_SIZE

    def toStringAlien(self):
        print(f"Alien positions {self.x} and  {self.y} :")
        print(self.x)
        print(self.y)
        print("Is Gone ? :")
        print(self.gone)
        print("Is Alive ? :")
        print(self.alive)
    def die(self):
        self.alive=False
    def isAlive(self):
        return self.alive
    def isGone(self):
        return self.gone