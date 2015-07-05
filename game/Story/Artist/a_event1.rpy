label artist_event1:
    #Story Event one:  Requirements:  None
    #hide screen phone_button
    
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    
    scene bg bedroom
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    Phone "Ring ring ring ring ring ring phone call phone call! Ring ring ring ring ring ring phone call!"
    stop sound
    
    Martha annoyed "I could hear the phone going off which cause a groan to escape my lips. I had no interest whatsoever in answering call. I knew exactly what the person on the other end wanted. She just wanted to yell at me and I had no interest in getting it was as simple as that. Sure eventually I would have pick up one of the phone calls, and get the whole big speech about 'why don't you ever answer my calls, don't you love your mother.' Those thoughts caused another groan."
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    Phone "Ring ring ring ring ring ring ring phone call phone call!"
    stop sound
    Martha "But still the infernal thing continue going off, refusing to let me sleep even a wink. I could almost swear my mother didn't want me to have a regular sleeping schedule."
    Martha "Finally I gave up all the idea of ever getting to sleep and answered the phone, regretfully."
    show phone_mom with dissolve
    Mom "Finally you pick up I thought something bad happened to you I was about to call the police!"
    Marthas surprise "Hello mom."
    Martha happy "I said in a completely casual tone ignoring her idea that I just been kidnapped."
    Mom "Honey you should really pick up the phone when people call, After all it could be someone on the other end wanting a date with you, maybe."
    Martha sad "I didn't like how she I did the maybe at the end, I couldn't get a date or something. did she honestly think her daughter was so ugly that no one wanted to date her. Anyway it is what is on the inside that counts!"
    Marthas "I know mom. I know."
    Mom "And you should really start taking other people's advice be early it will help you in life. I'm only saying these things because I'm your mother, and I love you."
    Martha happy "Yeah right, I almost scoffed."
    Martha "Still I listen to my mother, would only cause problems to raise a fuss now, or ever."
    Mom "You doing Deary? I used to doing those fake boring movies in which you read all the time? And those not real people pictures?"
    Martha annoyed "Those were how my mom referred to the things I liked. Visual novels were referred to as 'fake movies in which you read all the time,' and Cartoons and Anime were for two as 'those things with not real people.'"
    Marthas "Yes mother I'm still doing those."
    Mom "If you want to write movies or books you should do instead of that instead of this fake thing."
    Marthas sad "Mother I like visual novels!"
    Mom "Honestly I don't know where you get this stubborn streak. You seem to just have no common sense whatsoever you possibly going to live off this thing? And what about grandchildren? How are you ever going to have grandchildren when you're spending all this time with that thing? Martha I want to have grandchildren before I die!"
    Martha "Of course, those were the things my mother always worried about, how it was going to possibly live off of visual novels and that I was never going to produce her grandchildren. she constantly stressed over how much time I was spending doing 'this,'  saying I was wasting my time when I could be out dating some guy, or building a career for myself and for my future family. She would stress her woes to anyone who would listen saying that I was going to be old and wrinkly and not have a date because no guy would even want to get close to me."
    Mom "You know you can't only think of yourself here, you have to think about your future; your family's future. I'm only trying to help you really should come  and join the family business. You won't get anywhere with this."
    Martha "That's it! I had it! I couldn't take it anymore!"
    Marthas upset "Mother it is my life! You may think I can't make it with visual novels alone, but I can! Not only that, I will prove it to you. I'll stand on my own two feet with just visual novels. I'll make a life for myself! I won't need the family business or you or dad! And if I can't, I'll accept it and join the business. But you have to give me a chance! That's all I'm asking!"
    Mom "Goodness don't talk to your mother like that! I brought you into this world; do you know how long I was in labor with you!? No respect! You have no respect at all! Why can't you be more like your brothers?! Fine, if you want to go into this nonsense I won't stop you any longer. you can screw your life for all I care!"
    Martha annoyed "And the line went dead."
    Martha "I let out a sigh as I set the phone down. My mother would have to get over it this was my life, my choices, and I was going to make visual novels."
    Marthas "Well, time to get to work! I only have so long before mother will call about the deadline." 
    
    $ minutes = 8*60 + 15 #set time to 8:15AM
    
    jump sim