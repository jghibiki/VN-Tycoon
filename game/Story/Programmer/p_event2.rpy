label coder_event2:
    #first coding attempt
    
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    t "Time to start putting that college education to use. While python isn't my primary language, one object-oriented language is just like another. Heck, I even have the engine already developed for me."
    t "But what am I supposed to be coding? I probably should have looked up what I need to do for visual novels before I just jumped head first into them."
    t "I guess that's the first step. Time to find some references to understand this engine!"
    t "Or I could just make one from scratch! If I don't make it myself, then I won't understand the intricacies of it. It won't be something that I made myself!"
    t "But that might take me longer than I am prepared to take. I don't think my medicine cabinet will last for me to make a working, viable engine from start. Dying before I see my completed might work for some developers, but it isn't for me."
    t "I really should have planned this out better... I guess my sister was right when she told me that I was too impulsive for my own good. When she finds out that I quit my job..."
    t "Oh well! Code monkey powers go! I'll start mapping out the features I want to include. It isn't a lot of progress, but one step at a time."
    
    $ coder_event2 = True
    jump sim