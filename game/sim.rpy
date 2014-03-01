image room="gui/main_bg.jpg"

label sim:
    scene room
    menu:
        "go to work":
            #$ inventory.work()
            $ salary = max(art, writing, coding, composing)
            if time.dec(4):
                $ inventory.earn(salary)
                "Work, work, work... You earned $[salary]."
            else:
                "You are too sleepy to work."
        "turn on the computer":
            call computer
        "draw":
            if time.dec(1):
                "You spend some time practicing drawing."
                $ art += 1
            else:
                "You are too sleepy to draw."
        "sleep":
            $ day += 1
            $ time = Time(24)
            
    jump sim

