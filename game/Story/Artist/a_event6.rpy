#Event 6: Conditions: Day 7
label artist_event6:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    Martha annoyed "I felt like I was making good progress but then everything just stopped."
    Martha "Something felt missing, but I didn't know what it was."
    Marthas sad "Hmm... something is just off."
    Martha "I started over again trying a different approach to the piece, but still it felt off."
    Marthas "What could be the issue? Is it the concept? The composition? The colors?"
    Martha "I continued listing possible problems and checked everything I could think of but still I seemed to make no progress."
    Martha "I let out a sigh and decided to take a break."
    $ pen_kind = "drawing"
    if inventory.has_item(tablet):
        $ pen_kind = "stylus"
    Martha annoyed "I fingered the [pen_kind] pen as I tried to think about what was wrong."
    Martha "I just can't figure it out."
    Martha "It keeps looking wrong, but I don't know why."
    Martha "This was one of the challenges of creative fields, you constantly ran into points where something looked or felt off. But not always could you put your finger on it."
    Martha "Oh well, I'll give it a day and see how things look tomorrow."

    $ artist_event6 = True    
    jump sim