label coder_event1:

    scene bg bedroom
    #$ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)

    "The alarm clock has been going off for the last twenty minutes. It was the last thing from my old job I forgot to take care of."

    "I should get up out of bed. Sleeping in on my first day of being an independent developer isn't promising me a sound future. It might be self-employment, but I don't want to have to fire myself."

    "Sitting beside my bed is my daily breakfast of bottled water and cornucopia of medication. It's Monday, so that means my friends are Acebutolol, Furosemide, and Hydrochlorothiazide."

    "As much as I hate swallowing these horse pills, I'd rather not follow my father's footsteps and die from hypertension before my time."

    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)

    "A ringing noise shakes me out of my morning routine. For a moment, I assume I hit the snooze on my alarm instead, but I quickly deduce that the strange ringing is my phone."
    stop sound
    t "Hello?"

    m "Toby!"

    "The sound of my former boss's voice wasn't what I was expecting to hear on my first day."

    t "Hey, Mark. What's up?"

    m "Just checking on how my old prodigy was doing in his new line of work."

    t "Well-"

    m "Toby, come back to us. I'll be frank, you were the best junior programmer we had. We need you back!"

    t "No. I told you, I'm not going to spend another month of my life programming realistic box features for another soulless fantasy again. I can't do it!"

    m "But-"

    t "I want to make something special! I want to make something that will be remembered as more than pretty skyboxes and grindtastic gameplay."

    m "We all started where you are, Toby. I know, I feel ya. But you have to do those boxes before you get to advance on to having your own team."

    m "I know you want these visual novel things to become mainstream, but what happens when they aren't?"

    t "I just keep trying until I make it."

    m "You're not on the company insurance policy anymore. Who is going to pay for your drugs?"

    t "Well..."

    m "I understand trying to fight off getting your soul crushed. But it happens to everyone!"

    t "..."

    m "Look, take sometime off. I've got your job tucked away for now. Get this thing out of your system and come back home to us. I'll be waiting."

    t "...thanks, Mark."

    m "See ya, my little code monkey."

    t "..."

    "I can't give up. I'm going to make a life out of this!"

    "No more boxes... never again."
    $ coder_event1 = True
    jump sim
