label writer_event1:
# Event 1:
# Opening event.
# Summary:
# Joan Gold is introduced to the player. She tries writing but it just doesn't work out.
# Scene:

    
#    In a world filled with endless water... where humanity has made an effort to eke out a living on flying islands...
    
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    
    stop music
    python:
        for song in song_list:
            renpy.music.queue(song['file'], channel='music', loop=True, clear_queue=False, fadein=2.0, tight=True)

    
    
    
    $ post = "In a world filled with endless water... where humanity has made an effort to eke out a living\non flying islands..."
    show screen sentence (showOptions=False)
    with dissolve
    show screen autoPost(278, 302, 0, 0, "#00000000", post, moveCursor=False, textSize= 16, wait=True)
    $ renpy.pause()
    Joan hat scowl_open "No! Nononono! Aaagh... that won't work at all! Urgh, I'm such a moron."
    Joan hat neutral "There was just this one thing you had to do, me. Ignore the pompous bastard. Don't listen to him. He's just provoking you."
    Joan hat scowl_open "But noooo, you just had to bite, didn't you? Had to 'prove' yourself!"
    Joan hat scowl_closed "I mean, honestly, who cares the pompous ass wrote eight Visual Novels in a year? It's still a niche. No one really cares about Visual Novels. Well, except for those idiots who do care, but they're idiots. Who cares."
    Joan hat despair  "Aaagh, but I can't back down from a dare now. Okay, Joan, okay. Calm down, you can do this. Forget about the entire 'muse' bullcrap. Inspiration isn't something that comes sporadically and suddenly, it's something you build up. Something you imagine."
    Joan hat scowl_closed "I mean, how hard can all this be? I just have to write a killer Visual Novel in 60 days. I can write, I can probably program... music can be found online... I could probably find sprites somewhere..."
    Joan hat despair  "I'm doomed. I'm friggin' doomed. My life is over. Oh god. It's never going to work out. Write a Visual Novel. Who the hell does that? Why the hell would I want to?! Aaagghhhhh... I'm a moron. Gold? More like Chengdeite."
    Joan hat neutral "H'ooookay, enough despair. Joan Gold, you're going to write a Visual Novel. Like, starting right the hell now! Show that pompous bastard just what effort can produce!"
    Joan hat laugh_med "I can't wait to wipe that arrogant smirk off of his damn face!"
    hide screen autoPost
    hide screen sentence
    with dissolve
    jump sim