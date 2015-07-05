label coder_event13:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black

    #Coding, day 14 or later
    t neutral_2 "My phone sits before me like an uncaring demon ready to tear out my soul. I would rather jump into a pit of boiling lava than make the phone call. I'd rather roll around on a pile of broken glass than make this call."
    t "But a painful realization has slowly formed in my mind as my experience as a visual novel developer has grown. As awesome as I am, there are things that I don't know, things I can't do."
    t happy "The road to a dream isn't a lonely one."
    ts "Hey."
    m "Toby! It's been a while! I thought you locked yourself in your apartment again."
    ts sad "I only did that once!"
    m "You also locked yourself in your closet after Terror on First Street. I remember we had to call the fire department to get you out."
    ts confused_glasses "Because I live on first street! Why did you make me watch that terrible movie?"
    m "..."
    ts confused "You're a terrible person."
    m "Yep. So, what did you need?"
    t scared "Time to swallow my pride."
    ts "Mark... I want you to teach me how to code like you do in HenPie."
    m "You want me to go back to the painful dream I abandoned?"
    ts neutral "Yes."
    m "After I talked you up to the upper management to get you that job?"
    ts "Yep."
    m "And it would have to be during the limited time I have after work. Time that I wouldn't be able to spend with my wife."
    ts tense_hardcore "I know I'm asking for a lot. You have every right in the world to laugh in my face and walk away. I wouldn't blame you."
    ts "But... I want to see this through. I want to make the best visual novel possible. Even if only twenty people download it, I want those twenty people to have the best time possible."
    ts "I'm only going to be able do it with help... so... please, Mark. Please help me."
    m "..."
    "It was a long shot. I-"
    m "Who's writing your speeches for you? I can't believe you've improve that much."
    ts "I-I-I did."
    m "Heh. Toby, all you ever had to do was ask."
    m "What happens to a dream deferred? Does it dry up like a raisin in the sun?"
    ts happy "Someone has been reading his classic literature lately."
    m "You order the pizza and I'll stop by tonight. You better be prepared to give it your all, because we are going to make one helluva game!"
    ts excited "Yeah!"
    m "We're all pulling for you. See ya tonight."
    ts "See ya."
    t "We're going to do this. We are going to make the best visual novel possible. Even if it doesn't go anywhere, even if I have to go back to that boring job... I want to make today count."
    t "Because I don't want to spend the rest of my life asking myself what could have been."

    $ coder_event13 = True
    jump sim