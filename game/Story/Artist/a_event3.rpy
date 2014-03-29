screen stalkmeplz_mom:
    use webBrowser
    add "Assets/bg/stalkmeplz.png"

label artist_event3:
#Story Event 3:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
#Requirements: Auto - Day 4 or so
    show screen computer
    "I started my day checking my email to see if anything important appeared. Sadly the only important thing was notifications for stalkmepls."
    $ showBrowser = "stalkmeplz"
    show screen stalkmeplz_mom
    
    
    
    Martha "It is a status update from my mom."

    Martha "I read it aloud to myself."

    Fancymom "My daughter has lost her mind. She is caught up in a cult of like website, that is warping her brain, it is like cancer I tell you. Cancersoft, someone save her from it! Where did I go wrong in raising her?"

    Martha "I let out a groan, Mom was as usual causing trouble. Why couldn't she just leave me alone? It wasn't enough that she wanted me to join the family business when I didn't want to. It wasn't enough that  she kept making fun of the things I liked to do. She constantly had to make fun of my choices and act like I was some kind of problem child."

    Martha "I looked at the post, it seemed lots of people were starting to rally around my mother. Lots of comments saying a word they were from my will be in doing cult. Honestly where did she get such a silly idea."

    Martha "Why couldn't she be like other mothers who supported their child!"

    Martha "This just gave me all the more desire to want to prove myself to her and get far away from her!"
    
    hide screen computer
    hide screen stalkmeplz_mom
    
    $ artist_event3 = True    
    jump sim