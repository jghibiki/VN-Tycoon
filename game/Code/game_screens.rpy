init -2 python:
    class Time:
        def __init__(self, value=0):
            global minutes
            self.value = value
            minutes = 24*60 - self.value*60 + 8*60
        def dec(self, hours):
            global minutes
            if self.value>8:
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
                self.art += inc_by
            if skill == "writing":
                inc_by = inc_by * ((10.0-self.writing)/10)/10
                self.writing += inc_by
            if skill == "coding":
                inc_by = inc_by * ((10.0-self.coding)/10)/10
                self.coding += inc_by
            if skill == "music":
                inc_by = inc_by * ((10.0-self.music)/10)/10
                self.music += inc_by
                
    
        
init -1 python:
    points = 5
    #drawing = 0
    
    # art = 0
    # writing = 0
    # coding = 0
    # composing = 0
    
    
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
     
            ui.frame(xalign=1.0)
            ui.text(text_show)
    config.overlay_functions.append(display_stats_overlay)
    
screen char_select:
    add "Assets/gui/char_select_bg.jpg"
    imagebutton auto "Assets/gui/artist_%s.png" focus_mask True xpos 200 ypos 200 action Return("artist") #at main_effect2_var
    imagebutton auto "Assets/gui/writer_%s.png" focus_mask True xpos 600 ypos 200 action Return("writer") #at main_effect2_var
    imagebutton auto "Assets/gui/programmer_%s.png" focus_mask True xpos 200 ypos 400 action Return("coder") #at main_effect2_var
    imagebutton auto "Assets/gui/composer_%s.png" focus_mask True xpos 600 ypos 400 action Return("composer") #at main_effect2_var
        
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
            textbutton "-" action If( points < 6 and skills.music > composing_min, true = [ SetField(skills, "music", skills.music - 1), SetVariable("points", points + 1) ], false = None )

        textbutton "OK" action Return()
            
