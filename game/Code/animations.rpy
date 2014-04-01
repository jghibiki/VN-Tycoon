init -1:

    image chibiWriter:
        "Assets/animations/04.png"
        pause 0.5
        "Assets/animations/05.png"
        pause 0.5

    image chibiCoder:
        "Assets/animations/06.png"
        pause 0.5
        "Assets/animations/07.png"
        pause 0.5       

    image chibiArtist:
        "Assets/animations/08.png"
        pause 0.5
        "Assets/animations/09.png"
        pause 0.5 

    image writingAni:
        "Assets/animations/01.png"
        pause 0.2
        "Assets/animations/02.png"
        pause 0.2
        "Assets/animations/03.png"
        pause 0.2

    image codingAni:
        "Assets/animations/01.png"
        pause 0.2
        "Assets/animations/02.png"
        pause 0.2
        "Assets/animations/03.png"
        pause 0.2
   
    image sketchAni:
        "Assets/animations/10.png"
        pause 0.2
        "Assets/animations/11.png"
        pause 0.2
       
    image tabletAni:
        "Assets/animations/12.png"
        pause 0.2
        "Assets/animations/13.png"
        pause 0.2
   
    image composingAni:
        "Assets/animations/14.png"
        pause 0.2
        "Assets/animations/14.png"
        pause 0.2
        "Assets/animations/16.png"
        pause 0.2

label writingAnimation:
    show writingAni
    pause 0.6
    hide writingAni
    call chibiAni
    
    return

label drawingAnimation:
    if inventory.has_item(tablet):
        show tabletAni
        pause 0.4
        hide tabletAni
    else:
        show sketchAni
        pause 0.4
        hide sketchAni
    call chibiAni
    return

label composingAnimation:
    show composingAni
    pause 0.6
    show composingAni
    call chibiAni
    return

label codingAnimation:
    show codingAni
    pause 0.6
    hide codingAni
    call chibiAni
    return

label chibiAni:
    if job == "writer":
        show chibiWriter
        pause 1.2
        hide chibiWriter
    elif job == "artist":
        show chibiArtist
        pause 1.2
        hide chiviArtist
    elif job == "coder" or job == "programmer":
        show chibiCoder
        pause 1.2
        hide chibiCoder
    return



#screen writingAnimation:
#    zorder 1000
#    add "writingAni"
#    $ wait_to_hide = 2.2 # number of seconds to wait
#    timer wait_to_hide action [Hide("writingAnimation"), Return()]

#screen drawingAnimation:
#    zorder 1000
#    add "writingAni"
#    text "You spend some time drawing."
#    $ wait_to_hide = 1.0 # number of seconds to wait
#    timer wait_to_hide action [Hide("drawingAnimation"), Return()]

#screen codingAnimation:
#    zorder 1000
#    add "codingAni"
#    $ wait_to_hide = 2.2 # number of seconds to wait
#    timer wait_to_hide action [Hide("codingAnimation"), Return()]

#screen composingAnimation:    
#    zorder 1000
#    add "composingAni"
#    text "You spend some time composing."
#    $ wait_to_hide = 1.0 # number of seconds to wait
#    timer wait_to_hide action [Hide("composingAnimation"), Return()]
    
