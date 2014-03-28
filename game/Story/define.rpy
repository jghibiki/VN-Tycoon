init -9 python:
    import random

#artist:   
define Phone = Character('Phone', color="#36393D", show_two_window=True)
define Mom = Character('Mom', color="#356AA0", show_two_window=True)
define Martha = Character('Martha', color="#356AA0", show_two_window=True, image="artist", window_left_padding=210, who_left_padding=210)
 
define Fancymom = Character('Fancymom', color="#FF0084", show_two_window=True) #Facebook
define Lazylandcat = Character('Lazylandcat', color="#FF7400", show_two_window=True, kind=nvl) #chat
define Artgirl = Character('Artgirl', color="#36393D", show_two_window=True, kind=nvl) #chat

#writer:
define Joan = Character('Joan', color="#356AA0", show_two_window=True, image="writer", window_left_padding=210, who_left_padding=210)
define Antagonist = Character('Antagonist', color="#356AA0", show_two_window=True)


#coder:
define t = Character('Toby', color="#356AA0", show_two_window=True)#, image="coder", window_left_padding=210, who_left_padding=210)
define m = Character('Mark', color="#356AA0", show_two_window=True)





init -2 python:
    for expression in ["annoyed", "crying", "crying_less", "happy", "happy_blush", "sad", "surprise", "upset"]:
            renpy.image("artist " + expression, "Assets/sprites/artist/"+expression+".png")

    for expression in ["despair", "laugh_big", "laugh_med", "neutral", "scowl_closed", "scowl_open"]:
        renpy.image("writer " + expression + " hat", "Assets/sprites/writer/hat/"+expression+".png")
        renpy.image("writer " + expression, "Assets/sprites/writer/nohat/"+expression+".png")
            
image side writer despair:
    "writer despair"
    crop (0, 0, 613, 426) size (392, 272)
image side writer despair hat:
    "writer despair hat"
    crop (0, 0, 613, 426) size (392, 272)
image side writer laugh_big:
    "writer laugh_big"
    crop (0, 0, 613, 426) size (392, 272)
image side writer laugh_big hat:
    "writer laugh_big hat"
    crop (0, 0, 613, 426) size (392, 272)
image side writer laugh_med:
    "writer laugh_med"
    crop (0, 0, 613, 426) size (392, 272)
image side writer laugh_med hat:
    "writer laugh_med hat"
    crop (0, 0, 613, 426) size (392, 272)
image side writer neutral:
    "writer neutral"
    crop (0, 0, 613, 426) size (392, 272)
image side writer neutral hat:
    "writer neutral hat"
    crop (0, 0, 613, 426) size (392, 272)
image side writer scowl_closed:
    "writer scowl_closed"
    crop (0, 0, 613, 426) size (392, 272)
image side writer scowl_closed hat:
    "writer scowl_closed hat"
    crop (0, 0, 613, 426) size (392, 272)
image side writer scowl_open:
    "writer scowl_open"
    crop (0, 0, 613, 426) size (392, 272)
image side writer scowl_open hat:
    "writer scowl_open hat"
    crop (0, 0, 613, 426) size (392, 272)

image side artist annoyed:
    "artist annoyed"
    crop (0, 0, 613, 426) size (392, 272)
image side artist crying:
    "artist crying"
    crop (0, 0, 613, 426) size (392, 272)
image side artist crying_less:
    "artist crying_less"
    crop (0, 0, 613, 426) size (392, 272)    
image side artist happy:
    "artist happy"
    crop (0, 0, 613, 426) size (392, 272)
image side artist happy_blush:
    "artist happy_blush"
    crop (0, 0, 613, 426) size (392, 272)
image side artist sad:
    "artist sad"
    crop (0, 0, 613, 426) size (392, 272)
image side artist surprise:
    "artist surprise"
    crop (0, 0, 613, 426) size (392, 272)
image side artist upset:
    "artist upset"
    crop (0, 0, 613, 426) size (392, 272)
    
image phone_mom:
    "Assets/sprites/phone_mom.png"
    yalign 0.0

image bg computer = "Assets/gui/computer_bg.jpg"

image bg bedroom:
    "Assets/bg/bedroom.jpg"
    
