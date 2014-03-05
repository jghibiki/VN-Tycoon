label sim:
    
    call screen sim
    scene black
    show room_closed
    $ action = _return
    if action == "work":
        $ salary = max(skills.art, skills.writing, skills.coding, skills.music)
        if time.dec(4):
            $ inventory.earn(salary)
            "Work, work, work... You earned $[salary]."
        else:
            "You are too sleepy to work."
    if action == "computer":
        call computer
    if action == "draw":
        if mygame.started:
            if time.dec(1):
                $ mygame.do_art(1)
                "You draw some sprites for your game. [mygame.art_done]"
            else:
                "You are too sleepy to draw."
        else:
            if time.dec(1):
                "You spend some time practicing drawing."
                $ skills.increase("art", 1)
                #$ skills.art += 1
            else:
                "You are too sleepy to draw."
    if action == "sleep":
        $ day += 1
        $ time = Time(24)
    
    jump sim
    

    
init:
    # image room_closed:
        # "Assets/bg/room/room_base_closed.png"
        # "Assets/bg/room/room_shadow1_closed.png"
        # alpha 0.4

    # image room_closed = LiveComposite(
    # (1366, 768),
    # (0, 0), "Assets/bg/room/room_base_closed.png",
    # (0, 0), im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.5))
    # )

    image room_closed = LiveComposite(
        (1366, 768),
        (0, 0), "Assets/bg/room/room_base_closed.png",
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/synth.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", im.MatrixColor("Assets/bg/room/room_shadow2_closed.png",im.matrix.opacity(1.0)),
                "minutes > 60*16", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(1.0)),
                "minutes > 60*15", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.9)),
                "minutes > 60*14", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.8)),
                "minutes > 60*13", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.7)),
                "minutes > 60*12", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.6)),
                "minutes > 60*11", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.5)),
                "minutes > 60*10", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.4)),
                "minutes > 60*9", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.3)),
                "True", im.MatrixColor("Assets/bg/room/room_shadow1_closed.png",im.matrix.opacity(0.2))),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", "Assets/bg/room/room_light1.png",
                "True", Solid("#ffffff00"))
    )

    image room_left = LiveComposite(
        (1366, 768),
        (0, 0), "Assets/bg/room/room_base_left.png",
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/synth.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", im.MatrixColor("Assets/bg/room/room_shadow2_left.png",im.matrix.opacity(1.0)),
                "minutes > 60*16", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(1.0)),
                "minutes > 60*15", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.9)),
                "minutes > 60*14", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.8)),
                "minutes > 60*13", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.7)),
                "minutes > 60*12", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.6)),
                "minutes > 60*11", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.5)),
                "minutes > 60*10", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.4)),
                "minutes > 60*9", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.3)),
                "True", im.MatrixColor("Assets/bg/room/room_shadow1_left.png",im.matrix.opacity(0.2))),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", "Assets/bg/room/room_light1.png",
                "True", Solid("#ffffff00"))
    )
    
    image room_right = LiveComposite(
        (1366, 768),
        (0, 0), "Assets/bg/room/room_base_right.png",
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/synth.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", im.MatrixColor("Assets/bg/room/room_shadow2_right.png",im.matrix.opacity(1.0)),
                "minutes > 60*16", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(1.0)),
                "minutes > 60*15", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.9)),
                "minutes > 60*14", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.8)),
                "minutes > 60*13", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.7)),
                "minutes > 60*12", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.6)),
                "minutes > 60*11", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.5)),
                "minutes > 60*10", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.4)),
                "minutes > 60*9", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.3)),
                "True", im.MatrixColor("Assets/bg/room/room_shadow1_right.png",im.matrix.opacity(0.2))),
        (0, 0), ConditionSwitch(
                "minutes > 60*17", "Assets/bg/room/room_light1.png",
                "True", Solid("#ffffff00"))
    )
    

    
    
    
screen sim:
    #add "Assets/gui/room.jpg"
    #add "Assets/bg/room/room_base_closed.png"
    add "#000"
    add "room_closed"
    
    #imagebutton idle "Assets/bg/room/room_base_closed.png" hover "Assets/bg/room/room_base_left.png" focus_mask "Assets/bg/room/left-door-mask.png" action [Return("work")] 
    imagebutton idle "#00000000" hover "room_left" focus_mask "Assets/bg/room/left_door_mask.png" action [Return("work")] 
    imagebutton idle "#00000000" hover "room_right" focus_mask "Assets/bg/room/right_door_mask.png" action [Return("sleep")] 
    
    imagebutton idle "Assets/bg/room/computer_off.png" hover "Assets/bg/room/computer_on.png" focus_mask "Assets/bg/room/computer_mask.png" action [Return("computer")]
    if inventory.has_item(tablet):
        imagebutton auto "Assets/gui/tablet_%s.png" focus_mask True action [Return("draw")] 
    else
        imagebutton auto "Assets/bg/room/sketchpad_%s.png" focus_mask True action [Return("draw")] 
    
    
    
    
#    imagebutton auto "Assets/gui/bedroom_%s.png" focus_mask True action [Return("sleep")] 
    #imagebutton auto "Assets/gui/computer_%s.png" focus_mask True action [Return("computer")] 
    #imagebutton auto "Assets/gui/exit_%s.png" focus_mask True action [Return("work")] 
    #imagebutton auto "Assets/gui/tablet_%s.png" focus_mask True action [Return("draw")] 

    use phone_button
    use game_button