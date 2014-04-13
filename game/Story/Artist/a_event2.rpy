#Story Event 2:

#Requirements: Auto - Day 2 or so

init:
    style smiley:
        font "Assets/gui/smiley.ttf"
        color "#000"
        size 36
label artist_event2:
    $ config.rollback_enabled = True
    $ renpy.block_rollback()    
    scene  black
    show screen computer
    Martha sad "I let out a sigh, it was actually hard to decide just where to begin. It was so much to do it was intimidating. I honestly wondered what I was getting into, maybe I had made the wrong choice."
    "There was going to be a lot more work than I thought. Just how was I going to prove to my mother that I can do this?"
    Lazylandcat "Hey there."
    "I was just sitting in front of my computer, staring at the screen when a friend of mine sent me an instant message."
    Artgirl "Hello there, how are you?"
    Lazylandcat "Tired.{=smiley}g{/}"

#    Lazylandcat "{=smiley}QWERTZUIOP ASDFGHJKL YXCVBNM qwertzuiop asdfghjkl yxcvbnm{/}"
    
    Lazylandcat "Life is exhausting."
    Artgirl "I can get behind that."
    Lazylandcat "How about you? How u?"
    Artgirl "Busy."
    Lazylandcat "Doing what?"
    Artgirl "I've decided to become independent from my parents and enter the world of professional visual novels."
    Lazylandcat "What?"

    nvl clear
    
    Artgirl "I even found a group people who are interested in the field, so I've been making a few friends hopefully."
    Lazylandcat "Do you think that is wise?"
    Lazylandcat "Isn't it like a super tiny field? A niche of an already niche. Doesn't sound like a good move finaincally."
    Lazylandcat "* financially"
    Artgirl "You're sounding like my mom now..."
    Lazylandcat "Sorry."
    
    nvl clear
    
    Artgirl "She just doesn't understand me."
    Lazylandcat "But, she is right."
    Artgirl "NOOOOOOOOOOO!"
    Artgirl "Not you too... ;_; You've joined the dark side."
    Lazylandcat "Join us, we have cookies!{=smiley}a{/}"
    Artgirl ">_>"
    Lazylandcat "They are really good *munches on one*"
    Artgirl "That is such an old meme."
    Lazylandcat "Join.... us!{=smiley}X{/}"
    nvl clear
    Artgirl "I refuse."
    Lazylandcat "Okay, back to sreious."
    Lazylandcat "* serious"
    

    Lazylandcat "You might struggle a lot with this visual novel thing, so it might be better to just join the family business."
    Artgirl "But, I hate the business. >_<"
    Lazylandcat "Sometimes you have to do things you don't like. Do you think I like my job. -_-"
    
    Artgirl "Fine.... but I just don't want to do it {=smiley}G{/}"
    nvl clear
    Lazylandcat "I don't think you can handle this."
    Artgirl "What?"

    Lazylandcat "You are kind of easily swayed and don't try super hard at things. You kind of like the easy way. And creating an identity in a small society doesn't sound like something you can do."
    Artgirl "Ooh Yeah! Watch me!"
    Lazylandcat "I wish you the best then. But I think you should make up with your mom."
    Artgirl "Traitor, joining her side."
    nvl clear
    Lazylandcat "I couldn't resist her cookies, sry. :'("

    Martha annoyed "I closed out the chat window."
    Martha "I was going to prove my friends wrong. I can put effort into things. I can go the distance."
    
    $ artist_event2 = True
    hide screen computer
    jump sim