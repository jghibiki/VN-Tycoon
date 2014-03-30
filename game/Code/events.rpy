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
                        #base_chance = 22
                        repBonus_tmp = repBonus
                        if repBonus_tmp > 10:
                            repBonus_tmp=10
                        chance = 2 - int(g.quality) - int(repBonus_tmp) #bigger game quality and reputation mean bigger chance of sale
                        
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
        
        if job=="artist":
            if day==2 and not artist_event2:
                event = "story", "artist_event2"
            if day==4 and not artist_event3:
                event = "story", "artist_event3"
            if day==5 and not artist_event4:
                event = "story", "artist_event4"
            if day==6 and not artist_event5:
                event = "story", "artist_event5"
            if day==7 and not artist_event6:
                event = "story", "artist_event6"
                
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

    
        if job=="coder":
            if not coder_event2 and curr_action=="coding":#first coding attempt
                event = "story", "coder_event2"
                
            if not writer_event3 and curr_action=="new_game" and mygame.genre == "romance":
                event = "story", "coder_event3"
            if not writer_event4 and curr_action=="new_game" and mygame.genre == "horror":
                event = "story", "coder_event4"
                
                
                
        last_time = curr_time
        return event


##############################
## Messaging and Forum Threads 

    #the players message box
    #messages = []
    
    #the messages in the recruitment forum
    #threads = []

    #the chance of getting a message
    repBonus = .04

    #polls for threads  to display for the recruitment forum
    def pollThreads():
        import random
        if len(threads) < 3:
            for i in range(random.randint(5,15)):
                threads.append(generateThread())
        else:
            threads.pop(0)
            threads.append(generateThread())
    
    #generates threads to be displayed for the recruitment forum
    def generateThread():
        repBonus_tmp = repBonus
        if repBonus_tmp>0.39:
            repBonus_tmp = 0.39
        return Thread(repBonus_tmp)

    #In essence threads will work like missions, completing the "mission" will result in an increased repBonus
    # and the gain of some asset progress for one of your games. The higher your repBonus, the greater the amount of 
    # asset progress you will recieve (as though with a higher reputation you can ask more reputable sources for help)
    class Thread:
        #import random
        categories = ["art", "music", "writing", "coding", "money"]
        scalar = 20 #the base number of hours to be input
        returnScalar = 2 #the difference between the return and the input
        
        def __init__(self, repBonus):
            self.input = Thread.categories[random.randint(0,4)]
            self.output=self.input
            while self.output==self.input:
                self.output = Thread.categories[random.randint(0,4)]
            
            #self.inputQuantity = round(Thread.scalar - (store.repBonus + randrangef(0.2,0.6, 0.01)) * Thread.scalar) 
            self.inputQuantity = round(Thread.scalar - (repBonus + randrangef(0.2,0.6, 0.01)) * Thread.scalar) 
            
            #self.outputQuantity =  self.inputQuantity > Thread.returnScalar+1 if  self.inputQuantity - Thread.returnScalar else Thread.returnScalar
            
            if self.inputQuantity > Thread.returnScalar+1:
                self.outputQuantity = self.inputQuantity - Thread.returnScalar
            else:
                self.outputQuantity = Thread.returnScalar
            
            if random.randint(1,10)>1:
                if self.input=="money":
                    self.inputQuantity *= 50
                if self.output=="money":
                    self.outputQuantity *= 50

                
            self.stage = "reminder" #or response
            self.user = make_user()
            self.description  = ""
            while(self.description  == ""):
                self.description = self.generateDescription()
            
            self.title = ""
            while(self.title  == ""):
                self.title = self.generateTitle()
  
            self.reminder = ""
            self.response = ""
            while self.reminder == "" or self.response == "":
                  self.reminder, self.response = self.generateMessages()

        def generateTitle(self):
            title_type = random.choice(["input", "output"])
            title_extra2 = ""
            if self.input == "money":
                title_type = "output"
            if self.output == "money":
                title_type = "input"
                title_extra2 = random.choice(["", "", "", " [paid]", " [PAID]", " [PAID]", " ($" + str(self.outputQuantity) + ")"])
                
            if title_type=="input":
                title = random.choice(threadTitlesInput)
                title_extra = random.choice(threadTitlesInputExtras)
            if title_type=="output":
                title = random.choice(threadTitlesOutput)
                title_extra = random.choice(threadTitlesOutputExtras)
            
            title_job = ""
            
            if (self.input == "art" and title_type == "input") or (self.output == "art" and title_type == "output"):
                title_job = random.choice(["artist", "Artist", "an artist", "an Artist"])
            if (self.input == "music" and title_type == "input") or (self.output == "music" and title_type == "output"):
                title_job = random.choice(["composer", "music composer", "a composer", "Music Composer", "musician"])                
            if (self.input == "writing" and title_type == "input") or (self.output == "writing" and title_type == "output"):
                title_job = random.choice(["writer", "a writer", "Writer", "a Writer"])
            if (self.input == "coding" and title_type == "input") or (self.output == "coding" and title_type == "output"):
                title_job = random.choice(["coder", "a coder", "Coder", "a Coder", "programmer", "a programmer", "Programmer", "a Programmer"])

            title = title.replace(" <*job*>", " " + title_job)
            title = title.replace("<*job*>", title_job.title())
            title = title.replace("<*user*>", self.user)
            title = title.replace("<*output*>", self.output)
            
            title = title + title_extra + title_extra2
            return title
                  
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
                desc = desc.replace("<*user*>", self.user)

                job_in = ""
                job_out = ""
                if self.input == "art":
                    job_in = random.choice(["artist", "Artist", "an artist", "an Artist"])
                if self.input == "music":
                    job_in = random.choice(["composer", "music composer", "a composer", "Music Composer", "musician"])                
                if self.input == "writing":
                    job_in = random.choice(["writer", "a writer", "Writer", "a Writer"])
                if self.input == "coding":
                    job_in = random.choice(["coder", "a coder", "Coder", "a Coder", "programmer", "a programmer", "Programmer", "a Programmer"])
                if self.output == "art":
                    job_out = random.choice(["artist", "Artist", "an artist", "an Artist"])
                if self.output == "music":
                    job_out = random.choice(["composer", "music composer", "a composer", "Music Composer", "musician"])                
                if self.output == "writing":
                    job_out = random.choice(["writer", "a writer", "Writer", "a Writer"])
                if self.output == "coding":
                    job_out = random.choice(["coder", "a coder", "Coder", "a Coder", "programmer", "a programmer", "Programmer", "a Programmer"])
                desc = desc.replace("<*job_in*>", job_in)
                desc = desc.replace("<*job_out*>", job_out)
                
                
                
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



