 init python:
    # class EventCheck(Action):
        # __call__(self):
            # return True
            
    #this function checks all the story events and handles all other time-sensitive events, such as replies on the forums, game downloads, etc.
    def eventcheck():
        if day==1:
            return True
    
        return False

    #the players message box
    messages = []
    
    #the messages in the recruitment forum
    recruitmentPosts = []

    #the chance of getting a message
    repBounus = .04

    #rolls for messages to add to the messages list
    def pollMessages():
        import random
        if random.random() < repBonus:
            messages.append(generateMessage())

    #generates messages to populate the messages list
    def generateMessage():
        import random
        pass
   
    #screen info - stuff the recruitment page should use to display itself
    messages = []
   
    #generates posts in the recruitment forum
    def generateForumPosts():
        import random

        colabList = generateCollaborators(random.randInt(0,6)) 
        for colab in colabList:
            messages.append(colab)
        

    
    #a function ment to provide a similar interface as polling for messages
    def pollForum():
        genterateForumPosts()

    #a function that creates a list of collaborators which will be able to 
    def generateCollaborators(num):
       colabList = [] 
       for x in range(num):
            colabList.append(Collaborator())
       return collabList 
   


