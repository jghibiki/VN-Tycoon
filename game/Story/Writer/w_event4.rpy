

# Event 4:
# You chose: 'Horror'
# Summary:
# Joan has absolutely no affinity for horror stories. Happens if you select to write Horror.
# Scene:
label writer_event4:
    show screen sentence (showOptions=False)
    with dissolve
    Joan neutral "Horror. Horror. Horror. God, even the word sounds stupid. Horror. Hoar roar. Whore roar. Roaring whores. That might work. A whore that roars is obviously not a regular whore."
    Joan neutral "Wait, maybe that isn't suitable for younger children. Er, wait, this is horror. It's probably not good horror if it's suited to younger children."
    Joan neutral "So like, why would the whores be roaring. Because they're whores? Because they're sluts that like to take men away from others? God, I hate those sluts. Yeah, let's turn them into monsters."
    Joan neutral "Like, succubi or something. Because clearly anyone who sleeps with a different guy each week is just sex-obsessed. Friggin' lust-starved whores."
    Joan neutral "Wait, are those actually scary? Wouldn't the guys just be lusting after it anyway? I mean, considering their tastes in women, I wouldn't be surprised if this turned from horror into their newest fantasies."
    Joan neutral "Dammit, Joan! You're writing a horror story, not the Lonely Guy's Ultimate Fantasy! Get a grip! Okay, okay, you know what? Screw it. These succubi... will... friggin' eat it. They'll chow down on it."
    Joan neutral "If that doesn't horrify those guys, I don't know what will."
    Joan neutral "Dammit, why do you have to be into sluts?"

    hide screen sentence
    with dissolve
    $ writer_event4 = True
    $ event = eventcheck("new_game")
    if event[0]=="story":
        $ renpy.jump(event[1])
    jump sim    