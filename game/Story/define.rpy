define Phone = Character('Phone', color="#36393D", show_two_window=True)
define Mom = Character('Mom', color="#356AA0", show_two_window=True)
define Martha = Character('Martha', color="#356AA0", show_two_window=True, image="artist", window_left_padding=410, who_left_padding=410)
 
define Fancymom = Character('Fancymom', color="#FF0084", show_two_window=True) #Facebook
define Lazylandcat = Character('Lazylandcat', color="#FF7400", show_two_window=True, kind=nvl) #chat
define Artgirl = Character('Artgirl', color="#36393D", show_two_window=True, kind=nvl) #chat

init -2 python:
    for expression in ["happy", "surprised"]:
        for pose in ["pose1"]:
            renpy.image("artist " + pose + " " + expression, im.Composite (None, 
                (0,0), "Assets/sprites/artist_"+pose+"_base.png",
                (0,0), "Assets/sprites/artist_"+expression+".png"
            ))

image side artist happy:
    "artist pose1 happy"
    crop (0, 0, 613, 426) size (392, 272)
    
image side artist surprised:
    "artist pose1 surprised"
    crop (0, 0, 613, 426) size (392, 272)

image phone_mom:
    "Assets/sprites/phone_mom.png"
    yalign 0.0

image bg computer = "Assets/gui/computer_bg.jpg"
image bg bedroom:
    "Assets/bg/bedroom.jpg"
    
