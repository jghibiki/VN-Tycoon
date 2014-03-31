label coder_event6:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    #after Day4
    
    
    t "I thought I could get by just figuring out the code by myself, but it finally happened. I hit a stumbling block with the ABL code in HemPie. Some form of dark magic is spawning bugs every time I try to make the sprite show up on the side of the screen!"
    t "It is against my personal philosophy to accept my weakness and give up. I am going to have my little guy show up next to the textbox one way or another!"
    t "But I need help... It pains me to admit, but I've been sitting at this one problem since the second day. Today I am gonna have to brave the forums and ask for help."

    #go to the forums
    $ showBrowser = "lsf"
    show screen lsf(showOptions=False)

    t "Okay. Now, I can't just out and ask people how they make their sprites appear. I don't want to seem like I don't know what I'm doing. Mark could find out and I'd be getting calls daily."
    t "I just need to make this sound nonchalant and like I know exactly what I'm doing."
    t "Side images. How?"
    t "...too blunt."
    t "I just found out how to make the images appear at the side, but I'm curious how other people do it. Share your secrets!"
    t "...that just sounds phony."
    t "How do you make those little people images appear at the side of the textbox? I've been trying for days and they just won't appear."
    t "...that's still too blunt. I'm already showing my failings as a writer. I shouldn't even bother trying to ask."
    t "My alarm rings, reminding me to take my daily cocktail of medication. Looking at the dwindling pile of medication reminds me... I don't have the right to pride anymore. I'm a developer and I have to make sacrifices sometimes."
    t "That last one. I'll just be honest and hope that people understand."
    t "...and submit."

    
    
    #play ringing noise
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    t "My phone? Who could be calling at this hour? Then again, I'm not really sure what hour it is."
    ts "Hello?"
    m "Toby!"
    ts "How did you find out so quickly?!"
    ts "Look, just because I asked for some help on things doesn't mean that I am going to fail."
    m "I just called to ask if you wanted to go out and grab something for dinner."
    m "But you're having problems?"
    ts "Nope, everything is good. 'kay, thanks, bye! Click."
    m "..."
    t "..."
    m "When you go click, you actually have to hang up the phone, Toby."
    ts "Oh. I thought I was doing something wrong."
    m "If you are having problems, don't be afraid to ask. Dude, I want you to succeed. It'd be awesome to have you back here, but I want to see a young man fulfill his dream."
    ts "Thanks, Mark."
    m "I always got to bet on the underdog. Don't be a stranger, dude."
    ts "Thanks. I'll talk to you later."
    t "I feel a bit better. I can overcome this!"        

    hide screen lsf
    $ coder_event6 = True
    jump sim