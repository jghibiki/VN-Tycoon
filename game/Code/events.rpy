init -1 python:
    last_time = None

init python:
    #this function checks all the story events and handles all other time-sensitive events, such as replies on the forums, game downloads, etc.
    def eventcheck():
        global last_time
        event = None
                
        curr_time = minutes + day * 24
        time_passed = curr_time - last_time

        #sales and downloads
        if time_passed>59: #check every hour; also make sure events aren't checked twice in a row if no time has passed
            x = time_passed/(60)#how many hours have passed?
            for g in games:
                if g.commercial: #sales
                    for i in range(x): #do a check for every hour that has passed
                        chance = 11 - int(g.quality) #bigger game quality means bigger chance of sale
                        if chance<0:
                            chance = 1
                        if random.randint(1,chance)==2:
                            sales.sell(g)
                            event = str(x)
                else: #downloads
                    pass

        #story events:
        if day==2 and job=="artist" and not artist_event2:
            event = "artist_event2"

        last_time = curr_time
        return event

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
   

