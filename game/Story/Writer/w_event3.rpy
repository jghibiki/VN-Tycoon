#Event 3:
#You chose: 'Romance'
#Summary:
#The player chose to write romance. Unfortunately, Joan can't into romance. You also have to have Boy x Girl selected.
#Scene:
label writer_event3:
    $ post = "Shall I compare thee to a summer's day? Thou art..."
    show screen sentence (showOptions=False)
    with dissolve
    show screen autoPost(278, 302, 0, 0, "#00000000", post, moveCursor=False, textSize= 16, wait=True)
    $ renpy.pause()
    
    Joan neutral "Well, to be honest, she's not more temperate, is she? I mean, she's shy. That hardly constitutes temper. That just exudes boring."
    Joan neutral "... Oh god, I'm one of those, aren't I? Those hackjob authors who believe the only kind of girl is the meek, innocent and shy girl. GOD. DAMMIT. Look at yourself, Joan. Do you look girly to you? Well, sure, I mean, I'm not utterly manly, but... Despite not being a guy, I don't have to be innocent, meek and shy, right?"
    Joan neutral "It's such a cliché Why can't we have woman in upstanding roles? Why don't we write more badass tomboys? Right, because every-friggin'-body writes tomboys these days. Because we're like those idiot drivers who leave work five minutes early to beat traffic, just like all the other one thousand gazillion people who want to beat traffic."
    Joan neutral "Man, I think everyone's already tried every romance in the book. Or books, as it is. I kinda wish these kind of guys existed, anyway. Argumentative, playful, not afraid to try new things... Maaan, why can't I find a boyfriend? I'm not asking for a lot, am I?"
    Joan neutral "Well, I guess they're all scared. It's not like you're the nicest person, Joan. Maybe if you fixed that damn scowl and dressed up a little, but that's so much effort... I just want them to take me as I am."
    Joan neutral "That's not a whole lot asked. It isn't, honest. It's just a tiny bit, in the grand scheme of things. Aaaagh... why isn't there a guy who can match wits with me?! It's not like I'm actually a genius, right?! So why, whenever we talk... Why the hell do you ALWAYS agree with me?! I can be wrong, you know! Just because I don't smile doesn't mean I want you to buzz off! I get lonely too sometimes, you know!"
    Joan neutral "Screw all you bastards! SCREW ALL OF YOU! Why do you always just go for the sluts?! Why?! Have you seen their faces?! It just screams 'slut'! They've slept with a gazillion guys! They dump you and then have a new boytoy the next week!"
    Joan neutral "Why won't you look at me?!"
    Joan neutral "..."
    Joan neutral "Oh god. I need to lie down."

    hide screen sentence
    hide screen autoPost
    with dissolve
    $ writer_event3 = True