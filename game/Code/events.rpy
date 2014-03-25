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


##############################
## Messaging and Forum Threads 

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
            for i in range(random.randint(5,15)):
                threads.append(generateThread())
        else:
            threads.pop(0)
            threads.append(generateThread())
    
    #generates threads to be displayed for the recruitment forum
    def generateThread():
        return Thread(repBonus)


    #In essence threads will work like missions, completing the "mission" will result in an increased repBonus
    # and the gain of some asset progress for one of your games. The higher your repBonus, the greater the amount of 
    # asset progress you will recieve (as though with a higher reputation you can ask more reputable sources for help)
    class Thread:
        import random
        categories = ["art", "music", "writing", "coding", "money"]
        scalar = 20 #the base number of hours to be input
        returnScalar = 2 #the difference between the return and the input
        descInputOption = {
                            "skill" : [
                                        "Hey all! looking to hire someone to do some <*input*> for a project of mine. I need about <*inputQuantity*> <*input*> actually."
                                      ],
                            "non-skill": [
                                            "I'm looking to sell some work of mine for $<*inputQuantity*>."
                                         ]
                          }
        descOutputOption = {
                             "skill" : [
                                            "I'd be willing to trade for <*outputQuantity*> <*output*>. If your intrested let me know.",
                                       ],
                             "non-skill": [
                                            "I'd be willing to pay $<*outputQuantity*>. PM me if interested. 8)"
                                          ]
                            }
        def __init__(self, repBonus):
            self.input = Thread.categories[random.randint(0,4)]
            self.output = Thread.categories[random.randint(0,4)]
            self.inputQuantity = round(Thread.scalar - (store.repBonus + randrangef(0.2,0.6, 0.01)) * Thread.scalar) 
            self.outputQuantity =  self.inputQuantity > Thread.returnScalar+1 if  self.inputQuantity - Thread.returnScalar else Thread.returnScalar
            self.user = make_user()
            self.description = self.generateDescription()
            #todo: create a means of generating a post title that is semi-relivant, will likely use the same format for inserting info as the descriptions do

        def generateDescription(self):
            #This function should generate a formatted string to be used by the renpy text statement when displaying the thread
            #Basically this function will randomly select a format and replace statements following a format similar to this <*input*> to place the generated values into the string accordingly  
            recurse = False
            desc = ""
            if self.input == "money":
                if self.output == "money":
                    recurse = True
                    self.output = Thread.categories[random.randint(0,4)]
                    self.generateDescription()
                else:
                    desc += Thread.descInputOption["non-skill"][random.randint(0,len(Thread.descInputOption["non-skill"])-1)]
            elif not self.input == "money":
                desc += Thread.descInputOption["skill"][random.randint(0,len(Thread.descInputOption["skill"])-1)]

            if not recurse:
                desc += " " #add a space between sentences :P
                if self.output == "money":
                    desc += Thread.descOutputOption["non-skill"][random.randint(0,len(Thread.descOutputOption["non-skill"])-1)]
                else: 
                    desc += Thread.descOutputOption["skill"][random.randint(0,len(Thread.descOutputOption["skill"])-1)]

                #replace flags with values
                desc = desc.replace("<*input*>",self.input)
                desc = desc.replace("<*inputQuantity*>", str(self.inputQuantity))
                desc = desc.replace("<*output*>",self.output)
                desc = desc.replace("<*outputQuantity*>", str(self.outputQuantity))

            return desc
        
        def reply(self, index):
            #adds this instance to the message list and removes it from the threads list
            threads.pop(index)
            messages.append(self)

#A function to get a random float with a step
    def randrangef(start, stop, step):
        import random
        return round(((random.randint(0,int((stop-start)/step))*step)+start),2)



