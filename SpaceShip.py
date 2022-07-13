# -----------------------------------------------------------
# This class represents a Spaceship
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
from GameParameters import GameParameters
class SapaceShip :
    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.name=name
        self.life=3

    def decrementX(self):
        self.x=self.x-GameParameters.BLOCK_SIZE

    def incrementX(self):
        self.x=self.x+GameParameters.BLOCK_SIZE

    def decrementY(self):
        self.y = self.y-GameParameters.BLOCK_SIZE

    def incrementY(self):
        self.y = self.y+GameParameters.BLOCK_SIZE

    def decrementLifes(self):
        self.life=self.life-1
        print("Your life now:")
        print(self.life)
    def isDead(self):
        if self.life == 0 :
            return True
        else:
            return False
    def toString(self):
        print("Aircraft positions X and Y :")
        print(self.x)
        print(self.y)
        ##print("Position x="+{self.x}+" y="+{self.y}+" name="+{self.name)