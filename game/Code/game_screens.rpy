init -2 python:
    class Time:
        def __init__(self, value=0):
            global minutes
            self.value = value
            minutes = 24*60 - self.value*60 + 8*60
        def dec(self, hours):
            global minutes
            
            if self.value-hours>=8:
                self.value -= hours
                minutes = 24*60 - self.value*60 + 8*60
                return True
            else:
                return False

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
    points = 5
    inventory = Inventory()
    time=Time(24)
    day=0
    
init python:
    writing = 0
    def display_stats_overlay():
        if config.developer:
            text_show = ""
            text_show += "Art: " + str(skills.art)
            text_show += "\nWriting: " + str(skills.writing)
            text_show += "\nCoding: " + str(skills.coding)
            text_show += "\nComposing: " + str(skills.music)
            text_show += "\nMoney: $" + str(inventory.money)
            text_show += "\nDay:" + str(day)
            text_show += "\nTime: " + str(time.value)
     
            ui.frame(xalign=1.0, yalign=0.1)
            ui.text(text_show)
    config.overlay_functions.append(display_stats_overlay)
    
screen char_select:
    add "#000"
    add "Assets/gui/char_select_bg.png"
    
    
    imagebutton auto "Assets/gui/char_select_writer_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("writer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_writer") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "Assets/gui/char_select_artist_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("artist")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_artist") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "Assets/gui/char_select_coder_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("coder")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_coder") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "Assets/gui/char_select_composer_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("composer")] hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_composer") ] unhovered [Hide("gui_tooltip")]

init:
    image tooltip_writer=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("Select the writer class.", style="tips_bottom"))
    image tooltip_artist=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("Select the artist class.", style="tips_bottom"))
    image tooltip_coder=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("The coder. Congratulations! You have succeeded at developing the three great virtues of a programmer: laziness, impatience, and hubris.", style="tips_bottom"))
    image tooltip_composer=LiveComposite((1300, 73), (3,0), ImageReference("information"), (3,30), Text("Select the composer class.", style="tips_bottom"))
    
    
    #imagebutton auto "Assets/gui/artist_%s.png" focus_mask True xpos 200 ypos 200 action Return("artist") #at main_effect2_var
#    imagebutton auto "Assets/gui/writer_%s.png" focus_mask True xpos 600 ypos 200 action Return("writer") #at main_effect2_var
#    imagebutton auto "Assets/gui/programmer_%s.png" focus_mask True xpos 200 ypos 400 action Return("coder") #at main_effect2_var
#    imagebutton auto "Assets/gui/composer_%s.png" focus_mask True xpos 600 ypos 400 action Return("composer") #at main_effect2_var
        
screen set_attributes(cclass=''):

    vbox:
        $ my_text = "Selected class: " + str(cclass)
        text my_text
        $ my_text = "Points: " + str(points)
        text my_text
        
        hbox:
            $ my_text = "Art: " + str(skills.art)
            text my_text
            textbutton "+" action If( points > 0 and skills.art < 10, true = [ SetField(skills, "art", skills.art + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and skills.art > art_min, true = [ SetField(skills, "art", skills.art - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Writing: " + str(skills.writing)
            text my_text
            textbutton "+" action If( points > 0 and skills.writing < 10, true = [ SetField(skills, "writing", skills.writing + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and skills.writing > writing_min, true = [ SetField(skills, "writing", skills.writing - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Coding: " + str(skills.coding)
            text my_text
            textbutton "+" action If( points > 0 and skills.coding < 10, true = [ SetField(skills, "coding", skills.coding + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and skills.coding > coding_min, true = [ SetField(skills, "coding", skills.coding - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Music: " + str(skills.music)
            text my_text
            textbutton "+" action If( points > 0 and skills.music < 10, true = [ SetField(skills, "music", skills.music + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and skills.music > music_min, true = [ SetField(skills, "music", skills.music - 1), SetVariable("points", points + 1) ], false = None )

        textbutton "OK" action Return()
            
