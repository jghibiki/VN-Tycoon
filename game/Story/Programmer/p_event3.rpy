label coder_event3:
    #Choosing romance

    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    t happy "When I decided that I was going to make touching romance story, the only thing I could think of was how amazing my download numbers were going to be. Everyone loves a touching romance comedy. I mean, Ben Stiller manages to find work, right?"
    t neutral "It was an amazing plan at the decision making level, to be sure. Totally awesome. But when it came down to making the romance happen, the critical flaw of my plan jumped out at me."
    t tense "Except for Mari, who I went out with once when we were twelve, I've never actually had a girlfriend. Or a boyfriend. Or... friends, really."
    t happy "But I have played a ton of dating sims and RPGs! That's kind of like having a real romantic relationship. Except other people are having it. And they're fictional."
    t excited "I swore that I was going to make this a romance game. Maybe with some studying and research, I can make a sweet romance. People will be swept up in my romance and maybe fall in love with me."
    t "Heh. Maybe people will think I'm a suave guy and ignore my geeky habits. If I dream hard enough, I might be able to see that day."
    t happy "I'll find a cute otaku girl and we'll bond over our mutual love of visual novels. Together, we will make the most tender romantic story of all time!"
    t sad "I can feel my blood pumping, my heart beating. I close my eyes, and start practicing the breathing techniques that my doctor taught me. Calm down, Tobias. Calm. Peace. You are one with the universe."
    t happy "Slowly, the scare begins to subside. Love can kill me. Lovely."
    t excited "Hehe. Lovely."
    t happy "I wonder if I can get plenty of puns into this enchanting story of enchantment."
    t neutral "Okay... that was bad. I probably should get back to work so the pun maker in my head can recharge."
    
    $ coder_event3 = True
    jump sim