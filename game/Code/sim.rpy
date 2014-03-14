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
        call screen select_time
        $ duration = int(_return[1])
        if _return[0]=="p":
            if time.dec(duration):
                if skills.increase("art", duration):
                    "You spend some time practicing drawing."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to draw."
        else:
            if time.dec(duration):
                $ mygame.do_art(duration)
                $ completion = round((mygame.art_done/mygame.art_needed)*100, 2)
                "You draw some sprites for your game.[completion]\% Completed"
            else:
                "You are too sleepy to draw."
                
    if action == "sleep":
        $ day += 1
        $ time = Time(24)
    
    if action == "read1":
            if time.dec(1):
                if skills.increase("art", 2):
                    "You spend some time reading about drawing."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read2":
            if time.dec(1):
                if skills.increase("coding", 2):
                    "You spend some time reading about programming."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read3":
            if time.dec(1):
                if skills.increase("writing", 2):
                    "You spend some time reading about writing."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read4":
            if time.dec(1):
                if skills.increase("music", 2):
                    "You spend some time reading about music."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    
    if action == "write":
        call screen select_time
        if not _return:
            $pass
        else:
            $ duration = int(_return[1])
            if _return[0]=="p":
                if time.dec(duration):
                    if skills.increase("writing", duration):
                        "You spend some time practicing writing."
                    else:
                        "You are the very best. Like no one ever was."
                else:
                    "You are too sleepy to write."
            else:
                if time.dec(duration):
                    $ mygame.do_writing(duration)
                    $ completion = round((mygame.writing_done/mygame.writing_needed)*100, 2)
                    "You write for a while for your game.[completion]\% Completed"
                else:
                    "You are too sleepy to write."
                    
    if action == "code":
        call screen select_time
        if not _return:
            $pass
        else:
            $ duration = int(_return[1])
            if _return[0]=="p":
                if time.dec(duration):
                    if skills.increase("coding", duration):
                        "You spend some time practicing coding."
                    else:
                        "You are the very best. Like no one ever was."
                else:
                    "You are too sleepy to code."
            else:
                if time.dec(duration):
                    $ mygame.do_coding(duration)
                    $ completion = round((mygame.coding_done/mygame.coding_needed)*100, 2)
                    "You work on some code for your game.[completion]\% Completed"
                else:
                    "You are too sleepy to code."
            
    if action == "compose":
        call screen select_time
        if not _return:
            $pass
        else:
            $ duration = int(_return[1])
            if _return[0]=="p":
                if time.dec(duration):
                    $ skills.increase("music", duration)
                    "You spend some time practicing composing."
                else:
                    "You are too sleepy to compose."
            elif _return[0] == "a":
                if time.dec(duration):
                    $ mygame.do_music(duration)
                    $ completion = round((mygame.music_done/mygame.music_needed)*100, 2)
                    "You work on composing some music for your game.[completion]\% Completed"            
                else:
                    "You are too sleepy to compose."

    if action == "sales":
        call screen sales
    
    if action == "list":
        call screen game_list
    
    if action == "event":
        $ a = eventcheck()
        "[a]"
        
    if action == "pic":
        call screen show_cover(game=mygame)

    if action == "post":
        $ post = random.choice(posts_list)
        call screen autoPost(323, 214, 628, 684, "Assets/gui/lsf_post_test.png", post)
        
    if action == "cheat":
        $ inventory.money += 100
        $ skills.music = 10.0
        $ skills.drawing = 10.0
        $ skills.coding = 10.0
        $ skills.writing = 10.0
        
        
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
    imagebutton idle "#00000000" hover "room_left" focus_mask "Assets/bg/room/left_door_mask.png" action [Return("work")] hovered [Play("sound", "Assets/sfx/door open.ogg"), Show("gui_tooltip", my_picture="tooltip_work") ] unhovered [Hide("gui_tooltip")]
    
    imagebutton idle "#00000000" hover "room_right" focus_mask "Assets/bg/room/right_door_mask.png" action [Return("sleep")] hovered [Play("sound", "Assets/sfx/door open.ogg"), Show("gui_tooltip", my_picture="tooltip_sleep") ] unhovered [Hide("gui_tooltip")]
    
    imagebutton idle "Assets/bg/room/computer_off.png" hover "Assets/bg/room/computer_on.png" focus_mask "Assets/bg/room/computer_mask.png" action [Return("computer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_computer") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(tablet):
        imagebutton auto "Assets/gui/tablet_%s.png" focus_mask True action [Return("draw")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_draw") ] unhovered [Hide("gui_tooltip")]
    else
        imagebutton auto "Assets/bg/room/sketchpad_%s.png" focus_mask True action [Return("draw")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_draw") ] unhovered [Hide("gui_tooltip")]
    
    
    if inventory.has_item(book_d):
        imagebutton auto "Assets/bg/room/book1_%s.png" focus_mask True action [Return("read1")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read1") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_p):
        imagebutton auto "Assets/bg/room/book2_%s.png" focus_mask True action [Return("read2")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read2") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_w):
        imagebutton auto "Assets/bg/room/book3_%s.png" focus_mask True action [Return("read3")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read3") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_c):
        imagebutton auto "Assets/bg/room/book4_%s.png" focus_mask True action [Return("read4")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read4") ] unhovered [Hide("gui_tooltip")]
    
    
    
#    imagebutton auto "Assets/gui/bedroom_%s.png" focus_mask True action [Return("sleep")] 
    #imagebutton auto "Assets/gui/computer_%s.png" focus_mask True action [Return("computer")] 
    #imagebutton auto "Assets/gui/exit_%s.png" focus_mask True action [Return("work")] 
    #imagebutton auto "Assets/gui/tablet_%s.png" focus_mask True action [Return("draw")] 

    use phone_button
    use game_button
    
    frame:
        top_margin 150
        hbox:
            textbutton "Write" action Return("write")
            textbutton "Compose" action Return("compose")
            textbutton "Code" action Return("code")
            textbutton "Sales" action Return("sales")
            textbutton "List" action Return("list")
            textbutton "Event" action Return("event")
            textbutton "Pic" action Return("pic")
            textbutton "Post" action Return("post")
            textbutton "cheat" action Return("cheat")
            
            
            
init:
    image tooltip_work=LiveComposite((665, 73), (3,56), Text("Go to work.", style="tips_bottom"))
    image tooltip_sleep=LiveComposite((665, 73), (3,56), Text("Go to sleep.", style="tips_bottom"))
    image tooltip_computer=LiveComposite((665, 73), (3,56), Text("Turn on the computer.", style="tips_bottom"))
    image tooltip_draw=LiveComposite((665, 73), (3,56), Text("Draw.", style="tips_bottom"))
    
    
    
    image tooltip_read1=LiveComposite((665, 73), (3,56), Text("Read Drawing for Losers. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read2=LiveComposite((665, 73), (3,56), Text("Read Programming for Idiots. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read3=LiveComposite((665, 73), (3,56), Text("Read Writing for Retards. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read4=LiveComposite((665, 73), (3,56), Text("Read Composing for Morons. Time needed: 1 hour.", style="tips_bottom"))
    
    

screen select_time:
    modal False
    vbox: 
        xpos 0.01
        ypos 0.2
        text "Practice:"
        hbox:
            textbutton "1h" action Return("p1")
            textbutton "4h" action Return("p4")
            textbutton "8h" action Return("p8")
        text "Make assets:"
        hbox:
            textbutton "1h" action Return("a1")
            textbutton "4h" action Return("a4")
            textbutton "8h" action Return("a8")
        textbutton "Back" action Return(False) # a lazy work around to make
                                                    #back work 
