label coder_event4:
    #choosing horror
    
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    t scared "Horror. I don't like scary movies. I don't even like dark alleys. What insane force made me even consider that genre? I want to stop now!"
    t confused "My hands are shaking at the thought of having to test out all of the code for that. Masked murderers are going to jump out at me again and again and again."
    t confused_glasses "I want to go home..."
    t tense_glasses "Wait. I am home. I want to go to a home without a horror game in development."
    t scared "What was that? I could have sworn I heard the voice of a young dead girl who send me an e-mail I didn't forward. She wants to murder me for not forwarding that message to five friends!"
    t neutral_2 "No. No. No.  Ghosts aren't real. Those are nothing but phishing scams. I'm a perfectly sane adult and perfectly sane adults aren't scared of stupid things like ghosts."
    t happy "I'm fine. I can do this. All calm."
    #play ringing sound effect
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    ts scared "I don't want to die!"
    t "I dive for the covers of my bed. I'll be safe there. Ghosts can't go through blankets."
    t sad "Maybe I'll start working on it later..."

    $ coder_event4 = True
    jump sim