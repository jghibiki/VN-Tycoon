# Event 6:
# Holy Shit, It Took Six Scenes For Interaction To Appear?!
# Summary:
# Joan finally interacts with someone. Happens after some time has passed automatically irrespective of choices.
# Scene:
label writer_event6:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()

    scene bg bedroom
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    Joan scowl_open "Hnngg... buh, what? Who the hell's callin' me? What time is it anyway? ... Aww man... did I really sleep in 'till 2 o' again?"
    Joan "Ah, dammit, where's my phone?!"
    stop sound
    Joan neutral "\"Hoy, yeah, me here.\""
    Antagonist "\"Heheh, you sound as groggy as always!\""
    Joan scowl_open "\"... What are you calling me for?\""
    Antagonist "\"Wow, grumpy. Were you sleeping again?\""
    Joan "\"Shut up.\""
    Antagonist "\"Man, you're such a lazybones.\""
    Joan "\"I'm going to hang up.\""
    Joan scowl_closed "Damn, did that ass really have to call me?"
    $ renpy.music.play ("Assets/sfx/phone ring.ogg", channel="sound", loop=True, fadeout=1.0, fadein=1.0)
    Joan "... You're calling me again, aren't you?"
    Joan scowl_open "\"What?\""
    stop sound
    Antagonist "\"Whoah, calm down, man! I just wanted to have a nice chat wi'ya.\""
    Antagonist "\"Was just looking at my Play Store stats for downloads, y'know. There's like, I just passed 80 thou on Terrible Day Redux!\""
    Antagonist "\"I mean, you write VNs too now, right? So you gotta understand! It's great!\""
    Antagonist "\"Oh, wait. You haven't actually written a VN.\""
    Joan "\"... You just callin' to be an ass?\""
    Antagonist "\"Hey, who's the one who told me, 'Writing VNs is cake, stop bragging'?\""
    Antagonist "\"And who was all, 'Challenge accepted' when I said, 'Nah man, it's pretty difficult'?\""
    Joan "\"... Shut up.\""
    Antagonist "\"So didya write that 'damn killer' VN yet?\""
    Joan "\"I said shut up! Don't call me again, you damn prick!\""
    Joan "... AGH, I hate that guy so much. So so so so so SO MUCH!"
    Joan scowl_closed "Dammit, this is no time to laze around! I have to write that damn VN and show up that damn idiot. It's not hard. Holy hell, how can it even be considered hard?!"
    Joan neutral "You can do this, Joan. Writer time!"
    $ writer_event6 = True
    jump sim
    
