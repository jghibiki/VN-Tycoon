label coder_event6:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    #after Day4
    
    show screen computer
    $ speed = 40 + skills.coding * 2
    $ post = "# You can place the script of your game in this file.\n\n# Declare images below this line, using the image statement.\n\n# eg. image eileen happy = \"eileen_happy.png\"\n\n# Declare characters used by this game.\ndefine e = Character('Eileen', image=\"eileen\")\n\n"
    
    show screen window_frame("Notepad--", "icon16_sentence", None)
    show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
    $ post = "image eileen happy = \"eileen_happy.png\"\nimage side elaine happy = \"side_eileen_happy.png\"\nlabel start:\n\n    e happy \"Oh, I'm so happy!\"\n\n    return"
    show screen autoPost(82, 300, 0, 0, "#00000000", post, typeSpeed=speed, moveCursor=False, textSize=15, wait=True)
    $ renpy.pause()
    
    
    t tense "I thought I could get by just figuring out the code by myself, but it finally happened. I hit a stumbling block with the ABL code in HenPie. Some form of dark magic is spawning bugs every time I try to make the sprite show up on the side of the screen!"
    t neutral_2 "It is against my personal philosophy to accept my weakness and give up. I am going to have my little guy show up next to the textbox one way or another!"
    t scared "But I need help... It pains me to admit, but I've been sitting at this one problem since the second day. Today I am gonna have to brave the forums and ask for help."

    hide screen autoPost
    hide screen autoPostFixed
    hide screen window_frame
    hide screen computer

    
    #go to the forums
    $ showBrowser = "lsf"
    show screen lsf(showOptions=False)

    t neutral "Okay. Now, I can't just out and ask people how they make their sprites appear. I don't want to seem like I don't know what I'm doing. Mark could find out and I'd be getting calls daily."
    t "I just need to make this sound nonchalant and like I know exactly what I'm doing."
    t "Side images. How?"
    t sad "...too blunt."
    t neutral "I just found out how to make the images appear at the side, but I'm curious how other people do it. Share your secrets!"
    t sad "...that just sounds phony."
    t neutral "How do you make those little people images appear at the side of the textbox? I've been trying for days and they just won't appear."
    t sad "...that's still too blunt. I'm already showing my failings as a writer. I shouldn't even bother trying to ask."
    $ renpy.music.play ("Assets/sfx/alarm_clock.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    t confused_glasses "My alarm rings, reminding me to take my daily cocktail of medication. Looking at the dwindling pile of medication reminds me... I don't have the right to pride anymore. I'm a developer and I have to make sacrifices sometimes."
    stop sound
    t neutral_2 "That last one. I'll just be honest and hope that people understand."
    t "...and submit."

    $ post = "How do you make those little people images appear at the side of the textbox? I've been trying for days and they just won't appear."
    call screen autoPost(323, 214, 628, 684, "Assets/gui/lsf_post_test.png", post, moveCursor=True)

    
    #play ringing noise
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    t confused_glasses "My phone? Who could be calling at this hour? Then again, I'm not really sure what hour it is."
    stop sound
    ts confused "Hello?"
    m "Toby!"
    ts tense_hardcore "How did you find out so quickly?!"
    ts "Look, just because I asked for some help on things doesn't mean that I am going to fail."
    m "I just called to ask if you wanted to go out and grab something for dinner."
    m "But you're having problems?"
    ts tense "Nope, everything is good. 'kay, thanks, bye! Click."
    m "..."
    t neutral "..."
    m "When you go click, you actually have to hang up the phone, Toby."
    ts tense_glasses "Oh. I thought I was doing something wrong."
    m "If you are having problems, don't be afraid to ask. Dude, I want you to succeed. It'd be awesome to have you back here, but I want to see a young man fulfill his dream."
    ts excited "Thanks, Mark."
    m "I always got to bet on the underdog. Don't be a stranger, dude."
    ts "Thanks. I'll talk to you later."
    t happy "I feel a bit better. I can overcome this!"        

    hide screen lsf
    $ coder_event6 = True
    jump sim