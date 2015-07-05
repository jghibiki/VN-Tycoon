label sim:
    $ config.rollback_enabled = False
    $showMainGui = True
    $showFarOff = False
    call screen sim
    scene black
    show room_closed
    $ action = _return
    if action == "work":
        call workingAnimation
        $ salary = max(skills.art, skills.writing, skills.coding, skills.music) * 4
        if time.dec(4):
                $ inventory.earn(salary)
                $ event = eventcheck("job")            
                if event[0]=="story":
                    $ renpy.jump(event[1])
                #"Work, work, work... You earned $[salary]."
        else:
            "You are too sleepy to work."
    if action == "computer":
        call computer

        
    if action == "draw":
        call screen select_time
        if not _return or _return=="desktop":
            $pass
        else:
            $ dur = int(_return[1])
            if _return[0] == "p":
                if time.dec(dur):
                    if skills.increase("art", dur):
                        call drawingAnimation
                    else:
                        "You are the very best. Like no one ever was."
                else:
                    "You are too sleepy to draw."
            elif _return[0] == "w":
                if time.dec(dur):
                    if comishWork.increase("art", dur):
                        call drawingAnimation
                    else:
                        "You should really turn in your work already."
                else:
                    "You are too sleepy to draw."
            else:
                if time.dec(dur):
                    $mygame.do_art(dur)
                    $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                    call drawingAnimation
                    $ event = eventcheck("art")
                    if event[0]=="story":
                        $ renpy.jump(event[1])
                else:
                    "You are too sleepy to draw."
                
    if action == "confirmSleep":
        call screen confirm_sleep
        if _return == "sleep":
            $action = "sleep"
            "Time for bed! Good night."
        else:
            "Maybe later."

    if action == "sleep":
        call sleepingAnimation
        $ time.dec(0)
        $ day += 1
        $ time = Time(24)
        $ save_name = job.title() + ", day " + str(day)# + " " + str (int(minutes/60) + ":" + str(minutes - int(minutes/60))
        $ event = eventcheck()
        if event[0]=="story":
            $ renpy.jump(event[1])

    if action == "read1":
            if time.dec(1):
                if skills.increase("art", 2):
                    call readingAnimation
                    #"You spend some time reading about drawing."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read2":
            if time.dec(1):
                if skills.increase("coding", 2):
                    call readingAnimation
                    #"You spend some time reading about programming."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read3":
            if time.dec(1):
                if skills.increase("writing", 2):
                    call readingAnimation
                    #"You spend some time reading about writing."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
    if action == "read4":
            if time.dec(1):
                if skills.increase("music", 2):
                    call readingAnimation
                    #"You spend some time reading about music."
                else:
                    "You are the very best. Like no one ever was."
            else:
                "You are too sleepy to read."
            
    if action == "compose":
        call screen select_time
        if not _return or _return=="desktop":
            $pass
        else:
            $ dur = int(_return[1])
            if _return[0] == "p":
                if time.dec(dur):
                    if skills.increase("music", dur):
                        call composingAnimation
                    else:
                        "You are the very best. Like no one ever was."
                else:
                    "You are too sleepy to compose."
            elif _return[0] == "w":
                if time.dec(dur):
                    if comishWork.increase("music", dur):
                        call composingAnimation
                    else:
                        "You should really turn in your work already."
                else:
                    "You are too sleepy to compose."
            else:
                if time.dec(dur):
                    $mygame.do_music(dur)
                    $completion = round(((mygame.music_done/mygame.music_needed)*100),2) 
                    call composingAnimation
                    $ event = eventcheck("music")
                    if event[0]=="story":
                        $ renpy.jump(event[1])
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
        call screen autoPost(323, 214, 628, 684, "Assets/gui/lsf_post_test.png", post, moveCursor=True)
        
    if action == "code_ani":
        show screen computer
        $ speed = 40 + skills.coding * 2
        $ post = random.choice(code_snippets_fixed1)
        show screen window_frame("Notepad--", "icon16_sentence", None)
        show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
        $ post = random.choice(code_snippets_typed1)
        call screen autoPost(82, 300, 0, 0, "#00000000", post, typeSpeed=speed, moveCursor=False, textSize=15)
        hide screen autoPostFixed
        hide screen window_frame
        hide screen computer
        
    if action == "cheat":
        $ inventory.money += 1000
        $ skills.music = 10.0
        $ skills.art = 10.0
        $ skills.coding = 10.0
        $ skills.writing = 10.0
        $ comishWork.writing = 25.0
        $ comishWork.coding = 25.0
        $ comishWork.music = 25.0
        $ comishWork.art = 25.0
    
    if action == "stats":
        call screen stats
        
    if action == "showWorkDone":
        call screen workDone
        
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
        (0, 0), ConditionSwitch("job=='writer' or job=='artist'", "Assets/bg/room/picture1.png", "True", "Assets/bg/room/picture2.png"),
        (0, 0), "Assets/bg/room/room_base_closed.png",
        #(0, 0), "Assets/bg/room/hand1.png",
        #(0, 0), "Assets/bg/room/hand2.png",
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

        (0, 0), ConditionSwitch("day%7>0", "Assets/bg/room/pizza1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>1", "Assets/bg/room/soda1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>2", "Assets/bg/room/pizza2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>3", "Assets/bg/room/soda2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>4", "Assets/bg/room/pizza3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/soda3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/pizza4.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/speakers2.png", "True", "Assets/bg/room/speakers1.png"),
        

    )

    image room_left = LiveComposite(
        (1366, 768),
        (0, 0), ConditionSwitch("job=='writer' or job=='artist'", "Assets/bg/room/picture1.png", "True", "Assets/bg/room/picture2.png"),
        (0, 0), "Assets/bg/room/room_base_left.png",
        #(0, 0), "Assets/bg/room/hand1.png",
        #(0, 0), "Assets/bg/room/hand2.png",
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

        (0, 0), ConditionSwitch("day%7>0", "Assets/bg/room/pizza1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>1", "Assets/bg/room/soda1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>2", "Assets/bg/room/pizza2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>3", "Assets/bg/room/soda2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>4", "Assets/bg/room/pizza3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/soda3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/pizza4.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/speakers2.png", "True", "Assets/bg/room/speakers1.png"),

    )
    
    image room_right = LiveComposite(
        (1366, 768),
        (0, 0), ConditionSwitch("job=='writer' or job=='artist'", "Assets/bg/room/picture1.png", "True", "Assets/bg/room/picture2.png"),
        (0, 0), "Assets/bg/room/room_base_right.png",
        #(0, 0), "Assets/bg/room/hand1.png",
        #(0, 0), "Assets/bg/room/hand2.png",
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

        (0, 0), ConditionSwitch("day%7>0", "Assets/bg/room/pizza1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>1", "Assets/bg/room/soda1.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>2", "Assets/bg/room/pizza2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>3", "Assets/bg/room/soda2.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>4", "Assets/bg/room/pizza3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/soda3.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("day%7>5", "Assets/bg/room/pizza4.png", "True", Solid("#00000000")),
        (0, 0), ConditionSwitch("job=='writer'", "Assets/bg/room/books.png", "True", Solid("#ffffff00")),
        (0, 0), ConditionSwitch("job=='composer'", "Assets/bg/room/speakers2.png", "True", "Assets/bg/room/speakers1.png"),

    )
    

    
    
    
screen sim:
    #add "Assets/gui/room.jpg"
    #add "Assets/bg/room/room_base_closed.png"
    add "#000"
    add "room_closed"
    
    
    
    #imagebutton idle "Assets/bg/room/room_base_closed.png" hover "Assets/bg/room/room_base_left.png" focus_mask "Assets/bg/room/left-door-mask.png" action [Return("work")] 
    imagebutton idle "#00000000" hover "room_left" focus_mask "Assets/bg/room/left_door_mask.png" action [Hide("gui_tooltip"), Return("work")] hovered [Play("sound", "Assets/sfx/door open.ogg"), Show("gui_tooltip", my_picture="tooltip_work") ] unhovered [Hide("gui_tooltip")]
    
    imagebutton idle "#00000000" hover "room_right" focus_mask "Assets/bg/room/right_door_mask.png" action [Hide("gui_tooltip"), Return("confirmSleep")] hovered [Play("sound", "Assets/sfx/door open.ogg"), Show("gui_tooltip", my_picture="tooltip_sleep") ] unhovered [Hide("gui_tooltip")]
    
    
    
    imagebutton idle "Assets/bg/room/computer_off.png" hover "Assets/bg/room/computer_on.png" focus_mask "Assets/bg/room/computer_mask.png" action [Hide("gui_tooltip"), Return("computer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_computer") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(tablet):
        imagebutton auto "Assets/bg/room/tablet_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("draw")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_draw") ] unhovered [Hide("gui_tooltip")]
    else:
        imagebutton auto "Assets/bg/room/sketchpad_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("draw")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_draw") ] unhovered [Hide("gui_tooltip")]
    
    if inventory.has_item(keyboard):
        imagebutton auto "Assets/bg/room/keyboard_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("compose")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_compose") ] unhovered [Hide("gui_tooltip")]
    
    
    if inventory.has_item(book_d):
        imagebutton auto "Assets/bg/room/book1_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("read1")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read1") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_p):
        imagebutton auto "Assets/bg/room/book2_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("read2")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read2") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_w):
        imagebutton auto "Assets/bg/room/book3_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("read3")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read3") ] unhovered [Hide("gui_tooltip")]
    if inventory.has_item(book_c):
        imagebutton auto "Assets/bg/room/book4_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("read4")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_read4") ] unhovered [Hide("gui_tooltip")]
    
    $ AClocks2(715, 203)
    
    
    if minutes > 60*20:
        add "#00000030"
    if minutes > 60*19:
        add "#00000035"
    if minutes > 60*18:
        add "#00000020"        
    if minutes > 60*17:
        add "#00000015"
    if minutes > 60*16:
        add "#00000010"
    if minutes > 60*15:
        add "#00000005"
    
    
#    imagebutton auto "Assets/gui/bedroom_%s.png" focus_mask True action [Return("confirmSleep")] 
    #imagebutton auto "Assets/gui/computer_%s.png" focus_mask True action [Return("computer")] 
    #imagebutton auto "Assets/gui/exit_%s.png" focus_mask True action [Return("work")] 
    #imagebutton auto "Assets/gui/tablet_%s.png" focus_mask True action [Return("draw")] 

    #use phone_button
    #use game_button
    
    if config.developer:
        frame:
            top_margin 150
            hbox:
                textbutton "debug" action ToggleVariable("debug", true_value=True, false_value=False)
                if debug:
                    textbutton "cheat" action Return("cheat")            
                    #textbutton "Write" action Return("write")
                    #textbutton "Compose" action Return("compose")
                    #textbutton "Code" action Return("code")
                    
                    #textbutton "Sales" action Return("sales")
                    #textbutton "List" action Return("list")
                    #textbutton "Event" action Return("event")
                    #textbutton "Pic" action Return("pic")
                    #textbutton "Post" action Return("post")
                    textbutton "stats" action Return("stats")
                    textbutton "Comish" action Return("showWorkDone")
                    #textbutton "Code ani" action Return("code_ani")

                    #textbutton "G. stats" action Show("game_progress")
                    #textbutton "New game!" action Show("new_game")
                
                    #if mygame.started:
                    #    textbutton "Release" action Jump("publish")
            
            
init:
    image tooltip_work=LiveComposite((665, 73), (3,56), Text("Go to work.", style="tips_bottom"))
    image tooltip_sleep=LiveComposite((665, 73), (3,56), Text("Go to sleep.", style="tips_bottom"))
    image tooltip_computer=LiveComposite((665, 73), (3,56), Text("Turn on the computer.", style="tips_bottom"))
    image tooltip_draw=LiveComposite((665, 73), (3,56), Text("Draw.", style="tips_bottom"))
    
    image tooltip_compose=LiveComposite((665, 73), (3,56), Text("Compose music.", style="tips_bottom"))
    
    image tooltip_read1=LiveComposite((665, 73), (3,56), Text("Read Drawing for Losers. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read2=LiveComposite((665, 73), (3,56), Text("Read Programming for Idiots. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read3=LiveComposite((665, 73), (3,56), Text("Read Writing for Retards. Time needed: 1 hour.", style="tips_bottom"))
    image tooltip_read4=LiveComposite((665, 73), (3,56), Text("Read Composing for Morons. Time needed: 1 hour.", style="tips_bottom"))
    
    

screen confirm_sleep:
    modal False
    frame:
        xpos 0.35
        ypos 0.35
        background "#000"
        frame:
            background "#fff"
            vbox:
                text "Are you sure you want to go to bed?" style "stdTxt"
                hbox:
                    textbutton "Yes" action Return ("sleep")
                    textbutton "No" action Return("")
    

screen select_time:
    modal False
    frame:
        xpos 0.35
        ypos 0.35
        background "#000"
        frame:
            background "#fff"
            vbox: 
                text "Practice:" style "stdTxt"
                hbox:
                    textbutton "1h" action Return("p1")
                    textbutton "4h" action Return("p4")
                    textbutton "8h" action Return("p8")
                text "Work on Comissions:" style "stdTxt"
                hbox:
                    textbutton "1h" action Return("w1")
                    textbutton "4h" action Return("w4")
                    textbutton "8h" action Return("w8")

                if mygame.started:
                    text "Make assets:" style "stdTxt"
                    hbox:
                        textbutton "1h" action Return("a1")
                        textbutton "4h" action Return("a4")
                        textbutton "8h" action Return("a8")
                textbutton "Back" action Return("desktop") # a lazy work around to make
                                                            #back work 

init python:
    def AClocks2(x=.5, y=.5):
#            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
#            ui.add("clock_2")
           


            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
            ui.at(RotoZoom ((minutes*0.5), (minutes*0.5), 5.0, 1, 1, 1, rot_bounce= False, rot_anim_timebase=False, opaque=False))
            ui.add("Assets/gui/c_hand1.png")
                                                            
            ui.at(Position(xpos=x, ypos=y, xanchor="center", yanchor="center"))
            ui.at(RotoZoom((minutes*6), (minutes*6), 5.0, 1, 1, 1, rot_bounce= False, rot_anim_timebase=False, opaque=False), )
            ui.add("Assets/gui/c_hand2.png")
