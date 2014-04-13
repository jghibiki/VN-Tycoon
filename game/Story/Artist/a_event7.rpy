label artist_event7:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    #Event 7: Conditions: Day 8
    Martha upset "It was nerve wracking. I kept getting called by my mother, constantly telling me to abandon what I wanted to do in favor of what she wanted to do."
    Martha "This was something I was used to, so it didn't matter a whole lot to me."
    Martha sad "However, coupled with my block in my art, it was taking a toll on me."
    Martha "I just laid on my bed wrapped in my cacoon of blankets waiting to transform into a competent person."
    Martha "I just wanted to sleep and escape from this world."
    Martha "Nothing I did seemed to work out."
    Martha surprise "I pulled up my phone and looked at all the calls, they were all from my mother."
    Martha annoyed "This is depressing."

    $ artist_event7 = True    
    jump sim