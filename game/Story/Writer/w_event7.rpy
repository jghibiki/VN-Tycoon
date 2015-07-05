# Event 7:
# Joan muses about purchasing.
# Summary:
# Joan thinks about the economy while making another purchase from the story. You need to have bought at least two items before.
# Scene:
label writer_event7:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    Joan scowl_closed "Ugh, another full price purchase. I mean, it's worth it to show up that smug bastard, but damn, I wish there'd be more discounts. We've got like, E-Dock and Vapor and everything, why the hell do people not understand discounts make us buy more stuff?"
    Joan "They're always jacking on and on about piracy and shit, like if there was no piracy everyone'd buy more stuff. But uh, yeah, I don't really see that happening."
    Joan scowl_open "Just look at these prices. Holy hell. If I wasn't so driven to show up this ass, I wouldn't even think twice about any of this. 'Commercial VN making is profitable' my ass. Maybe if you had enough capital to waste."
    Joan laugh_med "Or if you're a pirate. Yarr harr! Sailing them uncavorted seas of the interwebs, finding ye olde loot and programs."
    Joan laugh_big "Oh, hey, maybe that's an idea to write into this VN. Yeah, that'll totally work!"
    Joan scowl_open "Dammit, I didn't really need to buy this after all, did I?"
    $ writer_event7 = True
    jump sim
    
