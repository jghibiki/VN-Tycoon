label sim:
    call screen sim
    $ action = _return
    if action == "work":
        $ salary = max(art, writing, coding, composing)
        if time.dec(4):
            $ inventory.earn(salary)
            "Work, work, work... You earned $[salary]."
        else:
            "You are too sleepy to work."
    if action == "computer":
        call computer
    if action == "draw":
        if time.dec(1):
            "You spend some time practicing drawing."
            $ art += 1
        else:
            "You are too sleepy to draw."
    if action == "sleep":
        $ day += 1
        $ time = Time(24)
    
    jump sim
    
screen sim:
    add "gui/room.jpg"
    use phone_button
    imagebutton auto "gui/bedroom_%s.png" focus_mask True action [Return("sleep")] 
    imagebutton auto "gui/computer_%s.png" focus_mask True action [Return("computer")] 
    imagebutton auto "gui/exit_%s.png" focus_mask True action [Return("work")] 
    imagebutton auto "gui/tablet_%s.png" focus_mask True action [Return("draw")] 
