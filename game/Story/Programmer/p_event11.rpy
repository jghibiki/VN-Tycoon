label coder_event11:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
        
label coderEvent11:
    #coding, day 9
    t confused_glasses "ABL, why must you never work for me? Why must I sit here and code again and again the same feature? I know how you are supposed to work. I know how you should work. Why can't you just work?"
    t "I managed to get through side sprites after a lot of hard work, dedication, and some tips from forum dwellers, but I am once again in the same situation. I can't get the navigation menu to disappear when I hit return."
    t "The dent in my desk has only been growing larger as the hours tick by. I've used every trick in the book, the forum, and my brain. I'm starting to think that I'm asking for the impossible with this."
    t "There has to be something I can do to get this working. Someone in this world has had to have suffered the same problem that I am. Maybe there is something in the forums I missed, some clue that could get be back on track."
    t tense_glasses "Once again, my mind drifts back to Mark and his offer. It would be so easy to just forget this whole thing and take back up my old job. There's no complications there."
    t "It'd make Mark happy to see me back at my rented cubicle. I could have all the free soda that I can't drink all over again."
    t scared "Wait... It would be the ultimate swallowing of my pride, but Mark is a very sharp programmer. I don't know if he'd be willing to help me fix my code, but I'm out of options."
    
    t "He should have just gotten off. I doubt the first thing he wants to see when he gets home is more code... I hope he's in a good mood."
    m "Toby!"
    ts happy "Hey, Mark. How are you?"
    m "Pretty good. Got a date with the wife in an hour or so. What's up?"
    ts confused "Not much. I was just having some issues with a bit of code. I was hoping you could take a look and see what I'm missing."
    m "Oooooo! Want me to spill proprietary secrets with the runaway, huh?"
    ts confused_glasses "Something like that."
    m "Shoot me the script. I won't be able to look at it tonight, but I should be able to get you a solution quickly."
    ts "I've been at it for hours with help. You think you can do it?"
    m "I don't think I can, I know I can. You just trust old Mark."
    ts happy "I'll buy you a drink after this is all done."
    m "Why don't you come out with me and Barbara? You haven't been out of the house lately."
    ts tense_hardcore "You don't know that."
    m "..."
    ts tense "Okay, you do know that."
    m "Rachel has been asking about you. I'm sure she'd come along as well."
    ts tense_glasses "..."
    m "How about it?"
    ts confused_glasses "I-I-I-I'm sorry. I'm really busy tonight."
    m "Some other time then. I gotta go. Talk to you later, Toby."
    ts confused "See ya."
    t neutral "I put down my cell phone. Rachel was one of my fellow interns when I first started. She was kind of cute, and we had a lot of fun working together on our menial tasks."
    t tense "But that life is behind me now. I'm an independent developer. I'm probably losing all of my street credit having a company man help me with my script."
    t "My heart doesn't lie though. It doesn't believe the truths the brain tries to spin. It knows I'm scared. Scared of being nothing more than a cog in the system. Lost forever following the same path as others."
    t neutral "The only way I'll ever break out of the mold is to dedicate myself to this new frontier. Back to work."    


    $ coder_event11 = True
    jump sim