init -9 python:
    import random

#artist:   
define Phone = Character('Phone', color="#36393D", show_two_window=True)
define Mom = Character('Mom', color="#356AA0", show_two_window=True, what_prefix="\"", what_suffix="\"")
define Martha = Character('Martha', color="#356AA0", show_two_window=True, image="artist", window_left_padding=220, who_left_padding=220)
define Marthas = Character('Martha', color="#356AA0", show_two_window=True, image="artist", window_left_padding=220, who_left_padding=220, what_prefix="\"", what_suffix="\"")
define Fancymom = Character('Fancymom', color="#FF0084", show_two_window=True, what_prefix="\"", what_suffix="\"") #Facebook
define Lazylandcat = Character('Lazylandcat', color="#FF7400", show_two_window=True, kind=nvl) #chat
define Artgirl = Character('Artgirl', color="#36393D", show_two_window=True, kind=nvl) #chat

#writer:
define Joan = Character('Joan', color="#356AA0", show_two_window=True, image="writer", window_left_padding=220, who_left_padding=220)
define Joans = Character('Joan', color="#356AA0", show_two_window=True, image="writer", window_left_padding=220, who_left_padding=220, what_prefix="\"", what_suffix="\"")
define Antagonist = Character('Antagonist', color="#356AA0", show_two_window=True, what_prefix="\"", what_suffix="\"")


#coder:
define t = Character('Toby', color="#356AA0", show_two_window=True, image="coder", window_left_padding=220, who_left_padding=220)
define ts = Character('Toby', color="#356AA0", show_two_window=True, image="coder", window_left_padding=220, who_left_padding=220, what_prefix="\"", what_suffix="\"")
define m = Character('Mark', color="#356AA0", show_two_window=True, what_prefix="\"", what_suffix="\"")





init -2 python:
    for expression in ["annoyed", "crying", "crying_less", "crying_happy", "happy", "happy_blush", "sad", "surprise", "upset"]:
            renpy.image("artist " + expression, "Assets/sprites/artist/"+expression+".png")
    for expression in ["despair", "laugh_big", "laugh_med", "neutral", "scowl_closed", "scowl_open"]:
        renpy.image("writer " + expression + " hat", "Assets/sprites/writer/hat/"+expression+".png")
        renpy.image("writer " + expression, "Assets/sprites/writer/nohat/"+expression+".png")
    for expression in ["confused", "confused_glasses", "excited", "happy", "neutral", "neutral_2", "sad", "scared", "tense", "tense_glasses", "tense_hardcore"]:
        renpy.image("coder " + expression, "Assets/sprites/coder/"+expression+".png")

    for expression in ["annoyed", "crying", "crying_less", "crying_happy", "happy", "happy_blush", "sad", "surprise", "upset"]:
            renpy.image("side artist " + expression, "Assets/sprites/artist/side/"+expression+".png")
    for expression in ["despair", "laugh_big", "laugh_med", "neutral", "scowl_closed", "scowl_open"]:
        renpy.image("side writer " + expression + " hat", "Assets/sprites/writer/hat/side/"+expression+".png")
        renpy.image("side writer " + expression, "Assets/sprites/writer/nohat/side/"+expression+".png")
    for expression in ["confused", "confused_glasses", "excited", "happy", "neutral", "neutral_2", "sad", "scared", "tense", "tense_glasses", "tense_hardcore"]:
        renpy.image("side coder " + expression, "Assets/sprites/coder/side/"+expression+".png")

init +1:
    image phone_mark_:
        LiveComposite((307, 600),
            (0,0), "Assets/phone/phone_screen_blank_green.png",
            (0,0), "Assets/sprites/phone_call.png",
            (40,137), Text("Mark", color="f7f4ef", size=32, outlines=[ (1, "#6d6d6d", 0, 0) ] ),
            (0,0), "Assets/sprites/phone_call_male.png",
            
            (0,0), "Assets/Phone/phone_reflection.png")
        yalign 0.0

    screen phone_mark:
        window:
            background None
            yalign 0.0
            xanchor 0.0
            xpos 530
            add "phone_mark_"
            $ Clocks (133, 112, 12)
        
image phone_mom:
    "Assets/sprites/phone_mom.png"
    yalign 0.0

#image bg computer = "Assets/gui/computer_bg.jpg"

image bg bedroom:
    "Assets/bg/bedroom.jpg"
    
