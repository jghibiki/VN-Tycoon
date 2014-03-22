init -1 python:
    last_time = None

init python:
    #this function checks all the story events and handles all other time-sensitive events, such as replies on the forums, game downloads, etc.
    def eventcheck():
        global last_time
        event = None, None
                
        curr_time = minutes + day * 24 * 60
        time_passed = curr_time - last_time

        #sales and downloads
        if time_passed>59: #check every hour; also make sure events aren't checked twice in a row if no time has passed
            x = time_passed/(60)#how many hours have passed?
            for i in range(x): #do a check for every hour that has passed
                for g in games:
                    if g.commercial: #sales
                        chance = 12 - int(g.quality) #bigger game quality means bigger chance of sale
                        if chance<2:
                            chance = 2
                        if random.randint(1,chance)==1:
                            sales.sell(g, day=day+i/24,minutes=i%24*60)###
                            event = "sales", str(x)
                    else: #downloads
                        pass
        if time_passed>45:
            x = time_passed/(45) #should allow for polling of threads once for every 45 minutes that have passed
            for i in range(x):
                pollThreads()

        #story events:
        if day==2 and job=="artist" and not artist_event2:
            event = "story", "artist_event2"
        if day==4 and job=="artist" and not artist_event3:
            event = "story", "artist_event3"
            
        last_time = curr_time
        return event

    #the players message box
    messages = []
    
    #the messages in the recruitment forum
    threads = []

    #the chance of getting a message
    repBounus = .04

    #polls for threads  to display for the recruitment forum
    def pollThreads():
        import random
        if len(threads) == 0:
            for i in range(random.randInt(5,15):
                threads.append(generateThread())
        else:
            threads.remove(0)
            threads.append(generateThread)
    
    #generates threads to be displayed for the recruitment forum
    def generateThread():
        return Thread(repBonus)


    #In essence threads will work like missions, completing the "mission" will result in an increased repBonus
    # and the gain of some asset progress for one of your games. The higher your repBonus, the greater the amount of 
    # asset progress you will recieve (as though with a higher reputation you can ask more reputable sources for help)
    class Thread:
        categories = ["art", "music", "writing", "coding"]
        def __init__(self, repBonus):
            import random
            self.in = Thread.categories[randint(3)]
            self.out = Thread.categories[randint(3)]

            

  
