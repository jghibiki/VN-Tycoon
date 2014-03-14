init python:

    class Collaborator:
        def __init__(self):
            self.name = make_user()
            self.personality = self.generatePersonality()
      
        def getName():
            return self.name

        def generatePersonality():
            import random
            pType = ["happy", "stressed", "angry", "irritable", "thankful", "guilty", "lazy", "random"]

            return pType[randint(len(pType)-1)]
