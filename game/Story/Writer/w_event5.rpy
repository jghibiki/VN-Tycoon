# Event 5:
# How I Learned To Love The Commonfolk and Stop Angsting
# Summary:
# Joan recruits help for her Visual Novel. Happens if progress on other assets isn't working too well.
# Scene:
label writer_event5:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    show screen sentence (showOptions=False)
    with dissolve
    
    Joan hat scowl_closed "Mmm... I've got some work done. It looks good... I think... Just not feeling it. Guh, I should try to get help after all, these stock sprites look terrible. How can anyone be serious about creating a Visual Novel with stock assets anyway?"
    Joan "I mean, sure, you can use them if you absolutely can't find someone, but it's lame. How am I supposed to feel close to a guy I've seen in five different ways?! Argh."
    Joan hat scowl_open "I gotta find someone to help me out. There's got to be some artist that'd want to draw for me, right?! I mean, [mygame.title] is an amazing Visual Novel! ... Goddamn, did I really call it that?!"
    
    ###
    $ showBrowser = "lsf"
    show screen lsf(showOptions=False)

    Joan hat laugh_med "Ugh, whatever. Maybe I'll change it later. For now... let's see... this thing has a forum to go with it. A recruitment area! Brilliant, Joan, you'll find some allies yet!"
    Joan hat scowl_closed "Okay, let's see... Thread title... Looking for... and I should definitely add a summary of the story. And character descriptions, too. Should I add physical descriptions? I should. On the other hand, I kinda want to give the artist free reign... I'm really not that much of a visual type. Maybe I should just leave it open?"
    Joan "Eh, I will. Adventure, here we go! I mean, they can always ask for more character details if they need it, right? Of course they can. Don't ask stupid stuff, Joan!"
    Joan hat neutral "Right, well, I'll just post this... there!"
    ###
    Joan hat scowl_closed "..."
    Joan hat scowl_open "... Okay, it's been five minutes. Maybe I should refresh."
    Joan hat neutral "... Refresh... refresh... refresh... refresh..."
    Joan hat despair "AGH! Why isn't anyone replying?! I see the viewcount go up to 51! 52! Dammit people, I know you're reading my thread! Respond, dammit! It's not a terrible thread! I'm being super reasonable. I even showed you my samples!"
    Joan hat neutral "Dammit dammit dammit. ... One more refresh..."
    $ writer_event5 = True
    hide screen sentence
    hide screen lsf
    with dissolve
    jump sim

