init -1 python:
    last_time = None

init python:
    #this function checks all the story events and handles all other time-sensitive events, such as replies on the forums, game downloads, etc.
    def eventcheck(curr_action=None):
        global last_time
        event = None, None

        curr_time = minutes + day * 24 * 60
        time_passed = curr_time - last_time

        #sales and downloads
        if time_passed>59: #check every hour; also make sure events aren't checked twice in a row if no time has passed
            x = time_passed/(60)#how many hours have passed?
            for i in range(x): #do a check for every hour that has passed
                for g in games:
#                    if g.commercial: #sales
                        chance = 12 - int(g.quality) #bigger game quality means bigger chance of sale
                        if chance<2:
                            chance = 2
                        diff = g.price - g.recommended_price
                        if diff > 0:
                            chance = int(chance+diff)
                        if random.randint(1,chance)==1:
                            if g.commercial:
                                sales.sell(g, day=day+i/24,minutes=i%24*60)###
                                event = "sales", str(x)
                            else:
                                g.downloads += random.randint(30,50)
#                    else: #downloads
#                        pass
        if time_passed>45:
            x = time_passed/(45) #should allow for polling of threads once for every 45 minutes that have passed
            for i in range(x):
                pollThreads()

        #story events:
        
        
        if day==2 and job=="artist" and not artist_event2:
            event = "story", "artist_event2"
        if day==4 and job=="artist" and not artist_event3:
            event = "story", "artist_event3"
        

        if job=="writer": 
            if not writer_event2 and curr_action=="writing" and day>2:
                event = "story", "writer_event2"
            if not writer_event3 and curr_action=="new_game" and mygame.genre == "romance" and mygame.relationship == "bxg":
                event = "story", "writer_event3"
            if not writer_event4 and curr_action=="new_game" and mygame.genre == "horror":
                event = "story", "writer_event4"
#            if not writer_event5 and ... : # Joan recruits help for her Visual Novel. Happens if progress on other assets isn't working too well.
#                event = "story", "writer_event5"
            if not writer_event6  and day>10:# Joan finally interacts with someone. Happens after some time has passed automatically irrespective of choices.
                event = "story", "writer_event6"
            if not writer_event7 and len(inventory.items)>2 and curr_action=="purchase":# Joan thinks about the economy while making another purchase from the story. You need to have bought at least two items before.
                event = "story", "writer_event7"
            if not writer_event8 and curr_action=="new_game" and mygame.relationship == "gxb":# Joan writes a Girl x Boy story. Unfortunately, she has a strong opinion about this as well. Doesn't need to be a Romance.
                event = "story", "writer_event8"
            if not writer_event9 and curr_action=="job":# Joan goes out to work, but she hasn't had stable employment in a while. She earns money in a different way instead: Odd jobs.
                event = "story", "writer_event9"
#            if not writer_event10:# Joan's managed to snag the programmer for her project, and considers him for a bit. Must have attempted to recruit and gotten a programmer, must be paying him.
#                event = "story", "writer_event10"

    
                
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
        
        def __init__(self, repBonus):
            self.input = Thread.categories[random.randint(0,4)]
            self.output = Thread.categories[random.randint(0,4)]
            self.inputQuantity = round(Thread.scalar - (store.repBonus + randrangef(0.2,0.6, 0.01)) * Thread.scalar) 
            self.outputQuantity =  self.inputQuantity > Thread.returnScalar+1 if  self.inputQuantity - Thread.returnScalar else Thread.returnScalar
            self.stage = "reminder" #or response
            self.user = make_user()
            self.description  = ""
            while(self.description  == ""):
                self.description = self.generateDescription()
            #todo: create a means of generating a post title that is semi-relivant, will likely use the same format for inserting info as the descriptions do
            self.reminder  = ""
            self.response = ""
            while self.reminder == "" or self.response == "":
                  self.reminder, self.response = self.generateMessages()

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
                    desc += descInputOption["non-skill"][random.randint(0,len(descInputOption["non-skill"])-1)]
            elif not self.input == "money":
                desc += descInputOption["skill"][random.randint(0,len(descInputOption["skill"])-1)]

            if not recurse:
                desc += " " #add a space between sentences 
                if self.output == "money":
                    desc += descOutputOption["non-skill"][random.randint(0,len(descOutputOption["non-skill"])-1)]
                else: 
                    desc += descOutputOption["skill"][random.randint(0,len(descOutputOption["skill"])-1)]

                #replace flags with values
                desc = desc.replace("<*input*>",self.input)
                desc = desc.replace("<*inputQuantity*>", str(self.inputQuantity))
                desc = desc.replace("<*output*>",self.output)
                desc = desc.replace("<*outputQuantity*>", str(self.outputQuantity))
                desc = desc.replace("True ", "")

            return desc
        
        def generateMessages(self):
            if self.input == "money":
                reminder = msgReminderOptions["non-skill"]["in"][random.randint(0,len(msgReminderOptions["non-skill"]["in"])-1)]
            elif self.output == "money":
                reminder = msgReminderOptions["non-skill"]["out"][random.randint(0,len(msgReminderOptions["non-skill"]["out"])-1)]
            else:
                reminder = msgReminderOptions["skill"][random.randint(0,len(msgReminderOptions["skill"])-1)]

            reminder = reminder.replace("<*input*>",str(self.input))
            reminder = reminder.replace("<*inputQuantity*>", str(self.inputQuantity))
            reminder = reminder.replace("<*output*>",str(self.output))
            reminder = reminder.replace("<*outputQuantity*>", str(self.outputQuantity))
            reminder = reminder.replace("True " , "")

            response = msgResponseOptions[random.randint(0, len(msgResponseOptions)-1)]

            return reminder, response

        def reply(self, index):
            #adds this instance to the message list and removes it from the threads list
            threads.pop(index)
            messages.append(self)

#A function to get a random float with a step
    def randrangef(start, stop, step):
        import random
        return round(((random.randint(0,int((stop-start)/step))*step)+start),2)



