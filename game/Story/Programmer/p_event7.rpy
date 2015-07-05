label coder_event7:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    #after hiring an artist
    t sad "The feeling of success is fickle as the breeze. One minute I'm hammering out killer code and halfway decent story plots, the next I'm hammering a new dent in my desk using nothing but my head."
    t "I don't even want to think about how the art and music are going. If I keep trying to draw, all I am going to have is stick figures. Squiggly line stick figures that breed nothing but hate and contempt in my broken heart."
    t scared "Nobody is going to buy something with my cruddy art. I see the projects that are successful and nobody uses art at the level I draw. The 'Keep Toby from Dying Fund' is going to be empty soon."
    t tense "I've been talking with an artist on Lemming, but I'm a bit unsure. I don't like leaving my fate in the hands of someone else, but I really don't have a choice. She seems like a nice girl though. I can only hope she's as dedicated as I'm forced to be."
    t tense_hardcore "...maybe I should check to see if I could get my old job back. Soulless work might kill me slowly, but a heart attack might end my life tragically short."
    t happy "I have to stay strong... She can do it. I can do it. I'm gonna take a short break, blow up some stuff in WarSpear, and then come back rejuvenated and ready to win!"

        
    $ coder_event7 = True
    jump sim