# -----------------------------------------------------------
# This class give the ability in a future evolution to
# have a luch menu and store all of the parametters that the user give.
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

class GameCharacteristics:

    def __init__(self,numberOfAliens,timeOfAlienMouvement):
        self.numberOfAliens=numberOfAliens
        self.timeOfAlienMouvement=timeOfAlienMouvement
        self.score=0

    def incrementScore(self):
        self.score+=1


