label artist_event8:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    scene black
    
    #Event 8: Conditions: Day 10
    Martha annoyed "My procastination kept continuing, things just seemed impossible."
    Martha "I wanted to do stuff, but when I tried I'd think about how behind I was and that would make me stop. I was stuck in an endless loop of doing nothing!"
    
    $ pen_kind = "drawing"
    if inventory.has_item(tablet):
        $ pen_kind = "stylus"

    
    Martha sad "I let out a sigh as I once again put down my [pen_kind] pen. I couldn't seem to get anywhere. If it wasn't the feeling that something was off, it was being distracted by my mother or something else, there just seemed no motivation to draw anymore..."
    Martha "What was I going to do...?"
    Martha "If I couldn't find any motivation to draw I was never going to complete a visual novel. I was going to be stuck following my mother like a little lost puppy for my whole life. And yet... that didn't cause me to want draw even... I was blocked, completely and utterly stuck."
    Martha upset "I needed help..."
    Martha sad "I found myself once again procrastinating and just lazing around on the internet and social media."
    Martha happy "And then I saw it."
    Martha "A private message from someone at Lemmming Soft."
    Martha happy_blush "They were asking how I was doing. Someone... was worried about me."
    Martha "It was a strange feeling. One I don't think I've ever experienced before."
    Martha "It made me feel all warm inside."
    Martha crying_happy "I read the message, I don't know how many times. Each time my happiness kept coming back more and more, and I felt slightly motivated."
    Martha happy "I typed up a response and sent it off."
    Martha "I finally had a renewed vigor."

    $ artist_event8 = True    
    jump sim