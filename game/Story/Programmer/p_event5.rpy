label coder_event5:
    #choosing sci-fi

    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    t neutral_2 "I might as well do what I know best. Of course, there are so many critical questions I need to answer first!"
    t neutral "I mean... I still haven't figured out who the better captain was. Kirk had the wild streak and kept those space ladies woo'd, but Picard had that mature sensibility that kept the crew moving forward."
    t "What sort of captain would I want for my story? More importantly, am I going to have starfighters or capital ships? Starfighters are much cooler than capital ships, but I can have more characters crammed into a destroyer."
    t "But what about mecha? What if I had a big mecha carrier full of cute girls and giant robots? I think I could get a decent market with that."
    t tense "What to do...? What to do...?"
    
    $ coder_event5 = True
    jump sim