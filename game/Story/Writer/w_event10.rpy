# Event 10:
# You got a programmer.
# Summary:
# Joan's managed to snag the programmer for her project, and considers him for a bit. Must have attempted to recruit and gotten a programmer, must be paying him.
# Scene:
label writer_event10:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    Joan laugh_med "Awright! I got one! A programmer, at that. Finally. I mean, I could probably figure out all of this myself, but that'd take too long anyway. It's fine if I hire someone, right?"
    Joan scowl_closed "This pay is outrageous, though. What's he need it for anyway? Izzit really all for medicine? What's he running, a pharmacy?"
    Joan "Well, I guess it doesn't matter. I mean, I can afford him. Probably. Maybe. I think. Man, if you weren't all sadface on me I wouldn't have bothered. You're lucky I'm so generous."
    Joan scowl_open "And stupid. I need to see if I can work double shifts somewhere. Or maybe hit up that site again for the work."
    Joan laugh_big "Yeah, this'll work out. No problem. I've got a programmer, he's ace, I'm ace, we're all ace. This is gonna be just fine, Joan! It'll be fine!"
    Joan despair "... I'm so doomed."
    $ writer_event10 = True
    jump sim