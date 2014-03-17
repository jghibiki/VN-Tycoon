label writer_event1:
# Event 1:
# Opening event.
# Summary:
# Joan Gold is introduced to the player. She tries writing but it just doesn't work out.
# Scene:

#    In a world filled with endless water... where humanity has made an effort to eke out a living on flying islands...
    $ post = "In a world filled with endless water... where humanity has made an effort to eke out a living on flying islands..."
    show screen window_frame("Sentence", Return("desktop"))
    #use autoPost(28, 84, 0, 0, "#00000000", mytext, typeSpeed = typeSpeed, moveCursor=False, textSize=24)
    
    show screen autoPost(28, 84, 0, 0, "#00000000", post, moveCursor=False, textSize=24, wait=False)
    $ renpy.pause()
    
    Joan "No! Nononono! Aaagh... that won't work at all! Urgh, I'm such a moron."
    Joan "There was just this one thing you had to do, me. Ignore the pompous bastard. Don't listen to him. He's just provoking you."
    Joan "But noooo, you just had to bite, didn't you? Had to 'prove' yourself!"
    Joan "I mean, honestly, who cares the pompous ass wrote eight Visual Novels in a year? It's still a niche. No one really cares about Visual Novels. Well, except for those idiots who do care, but they're idiots. Who cares."
    Joan "Aaagh, but I can't back down from a dare now. Okay, Joan, okay. Calm down, you can do this. Forget about the entire 'muse' bullcrap. Inspiration isn't something that comes sporadically and suddenly, it's something you build up. Something you imagine."
    Joan "I mean, how hard can all this be? I just have to write a killer Visual Novel in 60 days. I can write, I can probably program... music can be found online... I could probably find sprites somewhere..."
    Joan "I'm doomed. I'm friggin' doomed. My life is over. Oh god. It's never going to work out. Write a Visual Novel. Who the hell does that? Why the hell would I want to?! Aaagghhhhh... I'm a moron. Gold? More like Chengdeite."
    Joan "H'ooookay, enough despair. Joan Gold, you're going to write a Visual Novel. Like, starting right the hell now! Show that pompous bastard just what effort can produce!"
    Joan "I can't wait to wipe that arrogant smirk off of his damn face!"
    
    jump sim