#Event 5A, Conditions: Day 5 "Event 4A" 
label artist_event5:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    $ showBrowser = "lsf"
    show screen lsf(showOptions=False)
    
    Martha "Upon waking in the morning I decided to check the thread to see if anyone had reply to my rant."
    Martha "And I was surprised to find how supportive people were. It made me want to burst out in tears."
    Martha sad "Why are there so many nice people in this world and how come I was only finding out this now. Growing up around my mother all the time twisted the way I saw people."
    Martha "People will always look at you like a failure or waste of space."
    Martha "That's what I thought."
    Martha "I had never gotten real sympathy from anyone before. So I thought the idea of people carring about someone else's problem was just something found in fiction."
    Martha "Maybe that was what attracted me to drawing. I could draw up these wonderful images of people carring for each other, something I could only imagine in my head."
    Martha crying_less "To see people care about my problem I was having... it was overwhelming."
    if not writing_fail:
        Marthas "Haha, look at me right now, bursting into tears by reading some random words on the internet. I'd probably get called pathetic if anyone saw this."
        "I decided to write up a reply to all the wonderful strangers I had just encountered. They were all so concered for me..."
        Martha crying_happy "Ah.... no... stop crying..."
        Martha "But it was no good. I just couldn't stop."
        Martha "This is just too much..."
        Martha "I was crying but beaming."
        Martha "Thank you everyone. Thank you so much. I was starting to feel discouraged and now I feel recharged. I'm ready to tackle the world one more time!"
    else:
        Martha "And then my hope was crushed."
        Martha "Someone had commented about how poorly my post was written."
        Martha "I didn't need to be told how awful I was at writing stuff. I knew that already."
        Martha "I wanted to retreat into my little box and never come out."
        Martha "This person just kept attacking me throughout their post. It was disheartening."
        Martha "Why was life so cruel."
        Martha "I shut down my computer and decided to return to my dreams for just a little longer..."
    hide screen lsf
    $ artist_event5 = True    
    jump sim