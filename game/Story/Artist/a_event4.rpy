#Event 4A, Conditions: Day 4 "Writing level 2 Pass"
label artist_event4:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    Martha annoyed "I awoke to yet another frustrating stalkmepls notification from my mother. She just didn't seem to want to stop."    
    Martha surprise "And if that wasn't enough I check my phone and an actual message from her."
    Martha upset "I couldn't stand it anymore."
    Martha "I needed to vent, bad!"
    $ showBrowser = "lsf"
    show screen lsf(showOptions=False)
    Martha "I needed to take my mind off my problems so I began scanning through Lemming Soft Forums, and then I noticed it. A forum called 'Rant about your problems.'"
    Martha "It was perfect. Like some kind of miracle had called me to this place. It was just want I needed a place where people talked about their issues and other people helped them out by just talking with them. A place to rant and vent."
    if skills.writing>=1:
        Martha happy "I found out I had more issues than I thought. They just kept flowing out and the post began more paragraphs than I had originally wanted."
        Martha "They are probably going to think I'm some kind of whiny babby...."
        Martha "I let out a sigh and just to push myself out there, like I did in my art. I couldn't stay holded up never showing myself to anyone."
        Marthas "Post."
        #$ post = "lalala"
        #call screen autoPost(323, 214, 628, 684, "Assets/gui/lsf_post_test.png", post, moveCursor=True)
    else: #Event 4B, Conditions: Day 4 "Writing level 2 Fail"
    
        Martha annoyed "Putting the words together proved to be very difficult. More difficult than I ever imagined."
        Marthas "This.... is...."
        Martha "Garbage..."
        Martha sad "I smacked my head on the keyboard in front of me. Why was writing so difficult, it was just stupid words."
        Martha "I glanced at my phone and let out a sigh."
        Martha "Maybe Mom was right. This is so littered with typos and horridness I could never show my writing to someone."
        #$ post = "This.... is....Garbage..."
        #call screen autoPost(323, 214, 628, 684, "Assets/gui/lsf_post_test.png", post, moveCursor=True)
        Martha surprise "I glanced up at the screen. Writen on it was 'Post Sucessful.'"
        Martha "Ah.......AH!!!!"
        Martha annoyed "I cursed my luck, and my head for smacking the keyboard and posting."
    hide screen lsf
    $ artist_event4 = True    
    jump sim