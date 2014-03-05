init python:

    userNames = [
                    "guardRemarkable", "woollow",  "hardReset", 
                    "blackAndWhite", "Holy Black", "grouchyKitty",
                    "angryRabbit", "Happy_Rabit", "darkness", "tricky"
                    "moeMoeLuvr",   "sillySnake", "friendlyDragon",
                    "MahjongLuvr101", "Darling"
                 ]
    class Collaborator:
       def __init__(self):
           import random
           nameNum = len(userNames)

           self.name = userNames[random.randInt(0,nameNum-1)]
      
       def getName():
           return self.name
