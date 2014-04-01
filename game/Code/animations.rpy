init -1:

    image baseAni:
        "Assets/animations/base.png"

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

    image sleepingAni:
        "Assets/animations/17.png"
        pause 0.4
        "Assets/animations/18.png"
        pause 0.4
        "Assets/animations/19.png"
        pause 0.4
        "Assets/animations/17.png"
        pause 0.4
        "Assets/animations/18.png"
        pause 0.4
        "Assets/animations/19.png"
        pause 0.4
        
    image workingAni:
        "Assets/animations/20.png"
        pause 0.4
        "Assets/animations/21.png"
        pause 0.4
        "Assets/animations/22.png"
        pause 0.4
    
    image readingAni:
        "Assets/animations/23.png"
        pause 0.2
        "Assets/animations/24.png"
        pause 0.2
        "Assets/animations/25.png"
        pause 0.2
        "Assets/animations/23.png"
        pause 0.2
        "Assets/animations/24.png"
        pause 0.2
        "Assets/animations/25.png"
        pause 0.2
        
label sleepingAnimation:
    show baseAni onlayer overlay
    show sleepingAni onlayer overlay
    pause 2.4
    hide sleepingAni onlayer overlay
    hide baseAni onlayer overlay
    return
    
label workingAnimation:
    show baseAni onlayer overlay
    show workingAni onlayer overlay
    pause 1.2
    hide workingAni onlayer overlay
    hide baseAni onlayer overlay
    return

label readingAnimation:
    show baseAni onlayer overlay
    show readingAni onlayer overlay
    pause 1.2
    hide readingAni onlayer overlay
    hide baseAni onlayer overlay
    return
    
label writingAnimation:
    show baseAni onlayer overlay
    show writingAni onlayer overlay
    pause 0.6
    hide writingAni onlayer overlay
    call chibiAni
    hide baseAni onlayer overlay
    return

label drawingAnimation:
    show baseAni onlayer overlay
    if inventory.has_item(tablet):
        show tabletAni onlayer overlay
        pause 0.4
        hide tabletAni onlayer overlay
    else:
        show sketchAni onlayer overlay
        pause 0.4
        hide sketchAni onlayer overlay
    call chibiAni
    hide baseAni onlayer overlay
    return

label composingAnimation:
    show baseAni onlayer overlay
    show composingAni onlayer overlay
    pause 0.6
    hide composingAni onlayer overlay
    call chibiAni
    hide baseAni onlayer overlay
    return

label codingAnimation:
    show baseAni onlayer overlay
    show codingAni onlayer overlay
    pause 0.6
    hide codingAni onlayer overlay
    call chibiAni
    hide baseAni onlayer overlay
    return

label chibiAni:
    if job == "writer":
        show chibiWriter onlayer overlay
        pause 1.2
        hide chibiWriter onlayer overlay
    elif job == "artist":
        show chibiArtist onlayer overlay
        pause 1.2
        hide chibiArtist onlayer overlay
    elif job == "coder" or job == "programmer":
        show chibiCoder onlayer overlay
        pause 1.2
        hide chibiCoder onlayer overlay
    return

