init -1:
    image writingAni:
        "Assets/animations/writing/01.png"
        pause 0.2
        "Assets/animations/writing/02.png"
        pause 0.2
        "Assets/animations/writing/03.png"
        pause 0.2
        "Assets/animations/writing/04.png"
        pause 0.5
        "Assets/animations/writing/05.png"
        pause 0.5

    image codingAni:
        "Assets/animations/writing/01.png"
        pause 0.2
        "Assets/animations/writing/02.png"
        pause 0.2
        "Assets/animations/writing/03.png"
        pause 0.2
        "Assets/animations/writing/06.png"
        pause 0.5
        "Assets/animations/writing/07.png"
        pause 0.5
        
screen writingAnimation:
    zorder 1000
    add "writingAni"
    $ wait_to_hide = 2.2 # number of seconds to wait
    timer wait_to_hide action [Hide("writingAnimation"), Return()]

screen drawingAnimation:
    zorder 1000
#    add "writingAni"
    text "You spend some time drawing."
    $ wait_to_hide = 1.0 # number of seconds to wait
    timer wait_to_hide action [Hide("drawingAnimation"), Return()]

screen codingAnimation:
    zorder 1000
    add "codingAni"
    $ wait_to_hide = 2.2 # number of seconds to wait
    timer wait_to_hide action [Hide("codingAnimation"), Return()]

screen composingAnimation:    
    zorder 1000
#    add "composingAni"
    text "You spend some time composing."
    $ wait_to_hide = 1.0 # number of seconds to wait
    timer wait_to_hide action [Hide("composingAnimation"), Return()]
    