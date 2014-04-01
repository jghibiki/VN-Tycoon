label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    
    scene black with fade

    show cred at Move((0.5, 3.8), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    with fade
    return
    
label the_end:
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    with dissolve
    
    call credits
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks

    return
    
init python:
    credits = ('Writing (the artist path)', 'Maelstrom-Fenrir'), ('Writing (the writer path)', 'Applegate'), ('Writing (the programmer path)', 'KomiTsuku'), ('Character Art & Animations', 'chocojax'), ('Programming, Background & GUI Art', 'Leon Zavsek'), ('Programming & GUI art', 'jghibiki'), ('Programming', 'DragoonHP'), ('Composer & stunt double', 'Marc Straight'), ('Special thanks', 'Omnificent'), ('Special thanks', 'The Zerglinator'), ('Special thanks', '15385bic (free character art)'),  ('Special thanks ', 'mugenjohncel (free character art and backgrounds)'), ('Special thanks', 'TrickWithAKnife (smartphone code)')


    
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()
    
init:
    image cred = Text(credits_s, text_align=0.5, font="Assets/gui/animeace.ttf", color="FFF" )
    image theend = Text("{size=80}The end", text_align=0.5, color="FFF" )
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5, color="FFF" )