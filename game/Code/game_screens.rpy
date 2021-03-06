init -2 python:
    class Time:
        def __init__(self, value=0):
            global minutes
            self.value = value
            minutes = 24*60 - self.value*60 + 8*60
        def dec(self, hours):
            global minutes
            res = eventcheck()
            if res[0] == "story":
                renpy.jump(res[1])
            
            if self.value-hours>=8:
                self.value -= hours
                minutes = 24*60 - self.value*60 + 8*60
                return True
            else:
                return False

    class ComishWork:
        import random
        def __init__(self):
            self.art = 0.0
            self.writing = 0.0
            self.coding = 0.0
            self.music = 0.0

        def increase(self, skill, hours):
            inc_by=0
            if skill == "art":
                if skills.art > 3:
                    inc_by += (hours / (12.0-skills.writing) + random.randint(0,1)) / 2
                    #for hour in xrange(hours):
                        #inc_by += (random.randint(1,round(skills.art)))/3
                        #inc_by += (random.randint(1,round(skills.art)))/10
                    if self.art + inc_by < 25.0:
                        self.art += inc_by
                    else:
                        self.art = 25.0
                        return False
                else:
                    return "fail"
            elif skill == "writing":
                if skills.writing > 3:
                    #inc_by = inc_by *(random.randint(1,round(skills.writing)))/3
                    #for hour in xrange(hours):
                    #    inc_by += (random.randint(1,round(skills.writing)))
                        
                    inc_by += (hours / (12.0-skills.writing) +random.randint(0,1)) / 2
                        
                        
                    if self.writing + inc_by < 25.0:
                        self.writing += inc_by
                    else:
                        self.writing = 25.0
                        return False
                else:
                    return "fail"
            elif skill=="coding":
                if skills.coding > 3:
                    #for hour in xrange(hours):
                        #inc_by += (random.randint(1,round(skills.coding)))/10
                    inc_by += (hours / (12.0-skills.coding) +random.randint(0,1)) / 2
                    if self.coding + inc_by < 25.0:
                        self.coding += inc_by
                    else:
                        self.coding = 25.0
                        return False
                else:
                    return "fail"
            elif skill=="music":
                if skills.music > 3:
                    #for hour in xrange(hours):
                        #inc_by += (random.randint(1,round(skills.music)))/10
                    inc_by += (hours / (12.0-skills.music) +random.randint(0,1)) / 2
                    if self.music + inc_by < 25.0:
                        self.music += inc_by
                    else:
                        self.music = 25.0
                        return False
                else:
                    return "fail"
            return True



    class Skills:
        def __init__(self):
            self.art = 0
            self.writing = 0
            self.coding = 0
            self.music = 0
        def increase(self, skill, hours):
            inc_by = hours
            if skill == "art":
                inc_by = inc_by * ((10.0-self.art)/10)/10
                if self.art + inc_by <= 10 and not self.art==10.0:
                    self.art += inc_by
                else:
                    self.art = 10.0
                    return False
            if skill == "writing":
                inc_by = inc_by * ((10.0-self.writing)/10)/10
                if self.writing + inc_by <= 10 and not self.writing==10.0:
                    self.writing += inc_by
                else:
                    self.writing = 10.0
                    return False
            if skill == "coding":
                inc_by = inc_by * ((10.0-self.coding)/10)/10
                if self.coding + inc_by <= 10 and not self.coding==10.0:
                    self.coding += inc_by
                else:
                    self.coding = 10.0
                    return False
                    
            if skill == "music":
                inc_by = inc_by * ((10.0-self.music)/10)/10
                if self.music + inc_by <= 10 and not self.music==10.0:
                    self.music += inc_by
                else:
                    self.music = 10.0
                    return False
            return True
        
init -1 python:
    points = 3
    inventory = Inventory()
    time=Time(24)
    day=0


init python:
    showMainGui = False
    showBars = False
    def mainGui():
        if showMainGui:
            ui.imagebutton("Assets/gui/stats_icon.png", "Assets/gui/stats_icon.png", clicked=Show("stats", transsition=Dissolve(1)), xpos=.95, ypos=.2, zindex=200)
            xshift = .896
            yshift = .36
            if not showBars:
                ui.textbutton("+", clicked=SetVariable("showBars", True), xpos=.95, ypos=yshift)
            else:
               
                ui.bar(range=10, value=skills.art, style="stat_bar", right_bar="Assets/gui_mini/stat_drawing_empty.png", left_bar="Assets/gui_mini/stat_drawing_full.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .03
                ui.bar(range=25, value=comishWork.art, style="stat_bar", right_bar="Assets/gui_mini/stat_drawing_empty_alt.png", left_bar="Assets/gui_mini/stat_drawing_full_alt.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)
                
                if mygame.art_needed != 1:

                    yshift += .03
                    ui.bar(range=mygame.art_needed, value=mygame.art_done, style="stat_bar", right_bar="Assets/gui_mini/stat_drawing_empty_alt2.png", left_bar="Assets/gui_mini/stat_drawing_full_alt2.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)


                yshift += .05

                ui.bar(range=10, value=skills.writing, style="stat_bar", right_bar="Assets/gui_mini/stat_writing_empty.png", left_bar="Assets/gui_mini/stat_writing_full.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .03
                ui.bar(range=25, value=comishWork.writing, style="stat_bar", right_bar="Assets/gui_mini/stat_writing_empty_alt.png", left_bar="Assets/gui_mini/stat_writing_full_alt.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)
                


                if mygame.writing_needed != 1:

                    yshift += .03

                    ui.bar(range=mygame.writing_needed, value=mygame.writing_done, style="stat_bar", right_bar="Assets/gui_mini/stat_writing_empty_alt2.png", left_bar="Assets/gui_mini/stat_writing_full_alt2.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .05

                ui.bar(range=10, value=skills.coding, style="stat_bar", right_bar="Assets/gui_mini/stat_programming_empty.png", left_bar="Assets/gui_mini/stat_programming_full.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .03
                ui.bar(range=25, value=comishWork.coding, style="stat_bar", right_bar="Assets/gui_mini/stat_programming_empty_alt.png", left_bar="Assets/gui_mini/stat_programming_full_alt.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)
                
                if mygame.coding_needed != 1:

                    yshift += .03

                    ui.bar(range=mygame.coding_needed, value=mygame.coding_done, style="stat_bar", right_bar="Assets/gui_mini/stat_programming_empty_alt2.png", left_bar="Assets/gui_mini/stat_programming_full_alt2.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .05

                ui.bar(range=10, value=skills.music, style="stat_bar", right_bar="Assets/gui_mini/stat_composing_empty.png", left_bar="Assets/gui_mini/stat_composing_full.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .03

                ui.bar(range=25, value=comishWork.music, style="stat_bar", right_bar="Assets/gui_mini/stat_composing_empty_alt.png", left_bar="Assets/gui_mini/stat_composing_full_alt.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)
                
                if mygame.music_needed != 1:

                    yshift += .03

                    ui.bar(range=mygame.music_needed, value=mygame.music_done, style="stat_bar", right_bar="Assets/gui_mini/stat_composing_empty_alt2.png", left_bar="Assets/gui_mini/stat_composing_full_alt2.png", xpos=xshift, ypos=yshift, width=150, height=20, xmaximum=150, ymaximum=20)

                yshift += .05
                if inventory.money < 10:
                    ui.text("$"+str(inventory.money), xpos=.95, ypos=yshift, color="#000", size=40)
                elif inventory.money < 100:
                    ui.text("$"+str(inventory.money), xpos=.94, ypos=yshift, color="#000", size=40) 
                elif inventory.money < 1000:
                    ui.text("$"+str(inventory.money), xpos=.92, ypos=yshift, color="#000", size=40) 
                elif inventory.money >= 1000:
                    ui.text("$"+str(inventory.money), xpos=.90, ypos=yshift, color="#000", size=40)

                yshift += .08
                ui.textbutton("-", clicked=SetVariable("showBars", False), xpos=.95, ypos=yshift) 

#                ui.bar(range=100, value=skills.writing, right_bar="Assets/gui_mini/stat_drawing

    config.overlay_functions.append(mainGui)




#bar value skills.art range 10.0 style "stat_bar" xpos 854 ypos y right_bar "Assets/gui/stat_drawing_empty.png" left_bar "Assets/gui/stat_drawing_full.png"

init python:
    writing = 0
    debug = False
    def display_stats_overlay():
        if config.developer and debug:
            text_show = ""
            text_show += "Art: " + str(skills.art)
            text_show += "\nWriting: " + str(skills.writing)
            text_show += "\nCoding: " + str(skills.coding)
            text_show += "\nComposing: " + str(skills.music)
            text_show += "\nrepBonus: " + str(repBonus)
            text_show += "\nMoney: $" + str(inventory.money)
            text_show += "\nDay:" + str(day)
            text_show += "\nTime: " + str(time.value)
            text_show += "\nComish Writing: " + str(comishWork.writing)
            text_show += "\nComish Coding: " + str(comishWork.coding)
            text_show += "\nComish Composing: " + str(comishWork.music)
            text_show += "\nComish Art: " + str(comishWork.art)
            if mygame.started:
                text_show += "\nGame progress:"
                completion = round(((mygame.writing_done/mygame.writing_needed)*100),2) 
                text_show += "\nWriting: " + str(round(mygame.writing_done, 2)) + "/" + str(mygame.writing_needed) + "(" + str(completion) + ")"
                completion = round(((mygame.coding_done/mygame.coding_needed)*100),2) 
                text_show += "\nCoding: " + str(round(mygame.coding_done, 2)) + "/" + str(mygame.coding_needed) + "(" + str(completion) + ")"
                completion = round(((mygame.music_done/mygame.music_needed)*100),2) 
                text_show += "\nMusic: " + str(round(mygame.music_done, 2)) + "/" + str(mygame.music_needed) + "(" + str(completion) + ")"
                completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                text_show += "\nArt: " + str(round(mygame.art_done, 2)) + "/" + str(mygame.art_needed) + "(" + str(completion) + ")"
                
            
            
            ui.frame(xalign=1.0, yalign=0.1)
            ui.text(text_show)
    config.overlay_functions.append(display_stats_overlay)
    
screen char_select:
    add "#000"
    add "Assets/gui/char_select_bg.png"
    
    
    imagebutton auto "Assets/gui/char_select_writer_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("writer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_writer") ] unhovered [Hide("gui_tooltip")] xpos 100
    imagebutton auto "Assets/gui/char_select_artist_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("artist")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_artist") ] unhovered [Hide("gui_tooltip")] xpos 180
    imagebutton auto "Assets/gui/char_select_coder_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("coder")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_coder") ] unhovered [Hide("gui_tooltip")] xpos 260
    #imagebutton auto "Assets/gui/char_select_composer_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("composer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_composer") ] unhovered [Hide("gui_tooltip")]

    add "Assets/gui/char_select_fore.png"
    
init:
    image tooltip_writer=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("The writer. You have mastered the art of procrastination and blocks, and being nitpicky. You'll finish your works someday...", style="tips_bottom"))
    image tooltip_artist=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("The artist. You've found a way to hide your wonky anatomy with style. When you've got flair who needs to be accurate all the time. You've learned the ancient art of redrawing a single line thousands of times.", style="tips_bottom"))
    image tooltip_coder=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("The coder. You have succeeded at developing the three great virtues of a programmer: laziness, impatience, and hubris.", style="tips_bottom"))
    image tooltip_composer=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("Select the composer class.", style="tips_bottom"))
    
    
    #imagebutton auto "Assets/gui/artist_%s.png" focus_mask True xpos 200 ypos 200 action Return("artist") #at main_effect2_var
#    imagebutton auto "Assets/gui/writer_%s.png" focus_mask True xpos 600 ypos 200 action Return("writer") #at main_effect2_var
#    imagebutton auto "Assets/gui/programmer_%s.png" focus_mask True xpos 200 ypos 400 action Return("coder") #at main_effect2_var
#    imagebutton auto "Assets/gui/composer_%s.png" focus_mask True xpos 600 ypos 400 action Return("composer") #at main_effect2_var

screen set_attributes(cclass=''):
    add "#FFF"
    if cclass=="artist":
        add "artist happy"
    if cclass=="writer":
        add "writer neutral hat"
    if cclass == "coder":
        add "coder happy"

    vbox xpos 488 ypos 195:
        #$ my_text = "Selected class: " + str(cclass)
        #text my_text
        $ my_text = "Available points: " + str(points)
        text my_text style "my_text"
        
        grid 2 1:
            $ my_text = "Writing: " + str(skills.writing)
            text my_text style "my_text"
                
            hbox xpos -90:
                textbutton "-" action If( points < 6 and skills.writing > writing_min, true = [ SetField(skills, "writing", skills.writing - 1), SetVariable("points", points + 1) ], false = None )
                bar value skills.writing range 10.0 style "stat_bar" right_bar "Assets/gui/stat_writing_empty.png" left_bar "Assets/gui/stat_writing_full.png" 
                textbutton "+" action If( points > 0 and skills.writing < 10, true = [ SetField(skills, "writing", skills.writing + 1), SetVariable("points", points - 1) ], false = None )

        grid 2 1:
            $ my_text = "Drawing: " + str(skills.art)
            text my_text style "my_text"
            hbox xpos -90:
                textbutton "-" action If( points < 6 and skills.art > art_min, true = [ SetField(skills, "art", skills.art - 1), SetVariable("points", points + 1) ], false = None )
                bar value skills.art range 10.0 style "stat_bar" right_bar "Assets/gui/stat_drawing_empty.png" left_bar "Assets/gui/stat_drawing_full.png"
                textbutton "+" action If( points > 0 and skills.art < 10, true = [ SetField(skills, "art", skills.art + 1), SetVariable("points", points - 1) ], false = None )

            
        grid 2 1:
            $ my_text = "Coding: " + str(skills.coding)
            text my_text style "my_text"
            hbox xpos -90:
                textbutton "-" action If( points < 6 and skills.coding > coding_min, true = [ SetField(skills, "coding", skills.coding - 1), SetVariable("points", points + 1) ], false = None )
                bar value skills.coding range 10.0 style "stat_bar" right_bar "Assets/gui/stat_programming_empty.png" left_bar "Assets/gui/stat_programming_full.png"
                textbutton "+" action If( points > 0 and skills.coding < 10, true = [ SetField(skills, "coding", skills.coding + 1), SetVariable("points", points - 1) ], false = None )
        
        
        grid 2 1:
            $ my_text = "Composing: " + str(skills.music)
            text my_text style "my_text"
            hbox xpos -90:
                textbutton "-" action If( points < 6 and skills.music > music_min, true = [ SetField(skills, "music", skills.music - 1), SetVariable("points", points + 1) ], false = None )            
                bar value skills.music range 10.0 style "stat_bar" right_bar "Assets/gui/stat_composing_empty.png" left_bar "Assets/gui/stat_composing_full.png"
                textbutton "+" action If( points > 0 and skills.music < 10, true = [ SetField(skills, "music", skills.music + 1), SetVariable("points", points - 1) ], false = None )

        textbutton "Continue" action Return()
            
#screen stats_button:
#    zorder 200
#    imagebutton idle "Assets/gui/stats_icon.png" hover "Assets/gui/stats_icon.png" action Show("stats") align (.93,.03)

init:
    $statScreenMode = 0
screen stats:
    modal True
    add "#ddd"
    if statScreenMode == 0:
        if job=="artist":
            add "artist happy" xpos 0  ypos 0
        elif job =="writer":
            add "writer neutral hat" xpos 0 ypos 0
        elif job == "coder":
            add "coder happy" xpos 0 ypos 0
        
        vbox:
            xpos 0.4
            ypos 0.3
            $ stat_menu_items = ["charStats", "workStats", "back"]
            for item in stat_menu_items:
                $ button_name = "m_button_" + item
                $ button_name_hover = button_name + "_hover"
                $ tip_name = "tooltip_" + item
                $ my_action = stat_menu_actions[item]
                button background None focus_mask True action my_action hovered  Play("sound", "Assets/sfx/click.ogg") unhovered [Hide("gui_tooltip")]:
                    add button_name
                    hover_child button_name_hover



init:


    $ stat_menu_actions = {"charStats" : Show("playerStats", transition=Dissolve(1)),
                        "workStats" : Show("workDone", transition=Dissolve(1)),
                        "back" : Hide("stats", transition=Dissolve(1)),
                     }

    $ button_text = "Stats"
    image m_button_charStats = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_charStats_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

    $button_text = "Work"
    image m_button_workStats = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_workStats_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff)

 
    $button_text = "Back"
    image m_button_back = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (8, 6), Text(button_text, style="main_butt")), main_eff)
    image m_button_back_hover = At(LiveComposite ((312, 80), (0,0), "Assets/gui/main_button.png", (3, 1), Text(button_text, style="main_butt_hover")), main_eff) 




screen playerStats:
    modal True
    
    add "#FFF"
    if job=="artist":
            add "artist happy" xpos 0  ypos 0
    elif job =="writer":
        add "writer neutral hat" xpos 0 ypos 0
    elif job == "coder":
        add "coder happy" xpos 0 ypos 0
        
    $ y=195
    text "Writing" xpos 488 ypos y style "my_text"
    $ mytext = str(round(skills.writing,2))
    bar value skills.writing range 10.0 style "stat_bar" right_bar "Assets/gui/stat_writing_empty.png" left_bar "Assets/gui/stat_writing_full.png" xpos 854 ypos y
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    
    $ y+=58
    text "Drawing" xpos 488 ypos y style "my_text"
    $ mytext = str(round(skills.art,2))
    bar value skills.art range 10.0 style "stat_bar" right_bar "Assets/gui/stat_drawing_empty.png" left_bar "Assets/gui/stat_drawing_full.png"  xpos 854 ypos y
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58
    text "Programming" xpos 488 ypos y style "my_text"
    $ mytext = str(round(skills.coding,2))
    bar value skills.coding range 10.0 style "stat_bar" right_bar "Assets/gui/stat_programming_empty.png" left_bar "Assets/gui/stat_programming_full.png" xpos 854 ypos y
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58
    text "Composing" xpos 488 ypos y style "my_text"
    $ mytext = str(round(skills.music,2))
    bar value skills.music range 10.0 style "stat_bar" right_bar "Assets/gui/stat_composing_empty.png" left_bar "Assets/gui/stat_composing_full.png" xpos 854 ypos y
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58*2

    text "Money" xpos 488 ypos y style "my_text"
    hbox xpos 760 ypos y:
        $ money = "$" + str(inventory.money)
        text money style "my_text"
        
    $ y+=58
    
    text "Day" xpos 488 ypos y style "my_text"
    hbox xpos 760 ypos y:
        text str(day) style "my_text"
   
    #textbutton "OK" action Return() xalign 0.1 yalign 0.9
    textbutton "OK" action Hide("playerStats", transition=Dissolve(1)) xalign 0.7 yalign 0.9 style "tbutton"
    
screen workDone:
    
    add "#FFF"

    add "#FFF"
    if job=="artist":
            add "artist happy" xpos 0  ypos 0
    elif job =="writer":
        add "writer neutral hat" xpos 0 ypos 0
    elif job == "coder":
        add "coder happy" xpos 0 ypos 0
        
    $ y=195
    text "Comission Work" style "my_text"

    $ y=195
    text "Writing" xpos 488 ypos y style "my_text"
    bar value comishWork.writing range 10.0 style "stat_bar" xpos 854 ypos y right_bar "Assets/gui/stat_writing_empty.png" left_bar "Assets/gui/stat_writing_full.png"
    $ mytext = str (round(comishWork.writing ,2))
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58
    text "Drawing" xpos 488 ypos y style "my_text"
    bar value comishWork.art range 10.0 style "stat_bar" xpos 854 ypos y right_bar "Assets/gui/stat_drawing_empty.png" left_bar "Assets/gui/stat_drawing_full.png"
    $ mytext = str (round(comishWork.art ,2))
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58
    text "Programming" xpos 488 ypos y style "my_text"
    bar value comishWork.coding range 10.0 style "stat_bar" xpos 854 ypos y right_bar "Assets/gui/stat_programming_empty.png" left_bar "Assets/gui/stat_programming_full.png"
    $ mytext = str (round(comishWork.coding ,2))
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    $ y+=58
    text "Composing" xpos 488 ypos y style "my_text"
    bar value comishWork.music range 10.0 style "stat_bar" xpos 854 ypos y right_bar "Assets/gui/stat_composing_empty.png" left_bar "Assets/gui/stat_composing_full.png"
    $ mytext = str (round(comishWork.music ,2))
    text mytext style "my_text" xpos 910 ypos y color "CECECE"
    
    textbutton "OK" action Hide("workDone", transition=Dissolve(1)) xalign 0.7 yalign 0.9 style "tbutton"

init:
    style my_text:
        size 38
        font "Assets/gui/animeace.ttf"
        color "000"
                
    style stat_bar is bar:
        thumb None
        ymaximum 50        
        xmaximum 350
        right_bar "Assets/gui/stat_empty.png"
        left_bar "Assets/gui/stat_full.png"
        
    $style.tbutton = Style(style.button)
