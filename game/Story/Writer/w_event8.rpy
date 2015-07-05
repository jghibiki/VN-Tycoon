# Event 8:
# "Girl chases Boy"? As if.
# Summary:
# Joan writes a Girl x Boy story. Unfortunately, she has a strong opinion about this as well. Doesn't need to be a Romance.
# Scene:
label writer_event8:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    show screen sentence (showOptions=False)
    with dissolve
    
    Joan hat despair "It's impossible. It's totally impossible. There's no way this is gonna work. Ugghh... how am I supposed to write a Girl meets Boy story when I've never even experienced a love like that?!"
    Joan hat scowl_open "I mean, sure, I could've chased people but, that's so lame, man. I mean, even if you're really keen on dating someone as a Girl, all the guys will just feel 'intimidated' and their 'manliness' is threatened."
    Joan "Bunch of friggin' pansy-ass wuss-shits. Yeah, just try doing it once, and they'll just gossip behind your back. Well, or in front of you. Damn asses. 'Wah, Joan tried to hit on me, did she really think I'd want to date her?' YES, YOU ASS. I REALLY THOUGHT THAT."
    Joan "God, and I thought we were friends. That we could get along. And then a week later, suddenly I'm a girl who keeps chasing a gazillion men. Because girls aren't supposed to hit on guys, right? Bullshit. "
    Joan hat scowl_closed "It's called emancipation! Girls can do everything guys can! Girls don't need to wear cute clothes or use make-up to be pretty and cute! I mean, I don't even want to be cute, but I'm pretty sure I look good enough without any of that bull."
    Joan hat scowl_open "Ugh, why did I decide to write a Girl meets Boy story? Well, I guess it'd be nice if he'd just accepted my feelings. Man... maybe I'll go with that angle. From the start, the two get together, and from there..."

    hide screen sentence    
    $ writer_event8 = True
    $ event = eventcheck("new_game")
    if event[0]=="story":
        $ renpy.jump(event[1])
    jump sim
    
