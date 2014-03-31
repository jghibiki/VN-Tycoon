label coder_event12:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
        
    #coding, next day
    t excited "Just as promised, the solution to my code awaits me in my inbox. Note to self: Never doubt Mark when he promises something related to code."
    t confused "I cross-check the code to mine, but it appears to be identical. Why does his work and mine crashes the program on launch? What did he do differently?"
    t confused_glasses "Finally, I find the coder note. A space. I forgot to make properly indent things and ended up with one line of code that was out of place. How did I miss such a stupid little thing?!"
    t neutral "Before I close the script, I glance over the rest to make sure he didn't change things. Unsurprisingly, a fellow programmer decided to rewrite some of my code."
    t "I bite my lip as I review the changes. The miracles, they should be called. Almost everything has been condensed. What took me ten lines only takes him two. Everything is polished and sleek."
    t confused "He's never touched HenPie and he's a bloody pro at it. I refuse to believe it. There's no way that someone brand new could just sit down and do this sort of work in an evening."
    t "I am going to get to the bottom of this."
    m "Toby!"
    ts neutral_2 "Hey, Mark. I was looking over some of the changes you made to my script."
    m "Something wrong with them? I made sure it all worked before I sent it over."
    ts confused "That's the thing, Mark. How did you know what needed to be changed?"
    m "Well... you know how code is. Learn one language, learned them all."
    ts "Sure, to a degree. You are working far beyond that level though. This is a pro's work."
    m "Glad my buddy liked it."
    ts confused_glasses "What aren't you telling me, Mark? I want to know."
    m "Think you can handle my big secret? Think it won't crush your hopes and dreams?"
    ts "Try me."
    m "You aren't the first one who had dreams of making it big in visual novels, Toby, old chap. Five years ago, I was in your shoes. Same hopes, same dreams."
    ts confused "Really? You?"
    m "Well, I started as an indie RPG maker, but I didn't have the assets for it. I moved to visual novels because I thought it would be easier."
    m "I made five visual novels. A couple of them were garbage, but some of them were gems. Beautiful, shining gems in the barren sea."
    m "I made twenty sales. I was devastated. I had banked everything on that dream and all it panned out was pyrite."
    ts scared "Twenty... I couldn't survive on that. I wouldn't even come close to breaking even at twenty sales."
    ts "I'm sorry to hear that... why didn't you tell me?"
    m "Things are changing, Toby. I still watch the scene. Things are growing, evolving. You might have a chance to make it big where I failed. As stupid as this sounds, if I couldn't make it, I at least want my friend to make it."
    m "So... don't let my story get you down. Keep writing, keep developing. If you ever need help, just let me know. I'm not as sharp as I used to be, but I still know a couple tricks."
    t confused_glasses "A couple?! He made me look like a freshman attending their first programming course!"
    t sad "If he couldn't make it... what hope do I have?"
    ts neutral_2 "I'll let you know. Thanks for the help."
    m "Stay strong, Toby!"
    t "Stay strong... easier said than done."

    $ coder_event12 = True
    jump sim