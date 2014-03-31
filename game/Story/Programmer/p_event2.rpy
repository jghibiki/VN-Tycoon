label coder_event2:
    #first coding attempt
    
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black

    show screen computer
    $ speed = 40 + skills.coding * 2
    $ post = "# You can place the script of your game in this file.\n\n# Declare images below this line, using the image statement.\n\n# eg. image eileen happy = \"eileen_happy.png\"\n\n# Declare characters used by this game.\ndefine e = Character('Eileen')\n\n# The game starts here.\nlabel start:\n\n    e \"You've created a new HenPie game.\"\n\n    e \"Once you add a story, pictures, and music, you can release it to the world!\"\n\nreturn"
    show screen window_frame("Notepad--", "icon16_sentence", None)
    show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
    $ post = random.choice(code_snippets_typed1)
    
    t happy "Time to start putting that college education to use. While python isn't my primary language, one object-oriented language is just like another. Heck, I even have the engine already developed for me."
    t confused "But what am I supposed to be coding? I probably should have looked up what I need to do for visual novels before I just jumped head first into them."
    t neutral_2 "I guess that's the first step. Time to find some references to understand this engine!"
    t neutral "Or I could just make one from scratch! If I don't make it myself, then I won't understand the intricacies of it. It won't be something that I made myself!"
    t tense "But that might take me longer than I am prepared to take. I don't think my medicine cabinet will last for me to make a working, viable engine from start. Dying before I see my completed might work for some developers, but it isn't for me."
    t "I really should have planned this out better... I guess my sister was right when she told me that I was too impulsive for my own good. When she finds out that I quit my job..."
    t happy "Oh well! Code monkey powers go! I'll start mapping out the features I want to include. It isn't a lot of progress, but one step at a time."
    
    hide screen autoPostFixed
    hide screen window_frame
    hide screen computer
    
    $ coder_event2 = True
    jump sim