label artist_event10:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    #Event 10: Conditions: Day 15
    Martha happy "This time when my mom called I was excited. I could tell her all about the fabulous person I had made friends with."
    Mom "But they aren't real."
    Martha upset "That was her response."
    Martha annoyed "I was so furious."
    Mom "You don't know if anything they say is the truth. They are probably deceiving you. You have to watch out for predators."
    Martha "I couldn't believe it. My mom was accusing my new friend of being a lie. Like I couldn't make friends on my own. Like good things couldn't happen to me."
    Martha "He isn't a lie.... someone getting along with me isn't a lie...."
    Martha "I can have people like me. I can get along with people."
    Martha "They aren't always deceiving me."
    Martha "Someone can care about me......"
    Martha "They can.... really...."
    Martha sad "I sat on my bed staring at the wall. All my energy that had been built up deflated like a balloon."
    Martha "Someone... can care about me............."

    $ artist_event10 = True    
    jump sim