# -----------------------------------------------------------
# This class represents a Missil
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

from GameParameters import GameParameters
#This class represents a missile
class Missil:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.destroyed=False
        self.gone=False
    def isDestroyed(self):
        return self.destroyed
    def selfDestruction(self):
        self.destroyed=True
    def decrementationY(self):
        self.y=self.y-GameParameters.BLOCK_SIZE
    def isGone(self):
        return self.gone


