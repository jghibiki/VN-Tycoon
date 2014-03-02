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

init -1 python:
    points = 5
    #drawing = 0
    
    art = 0
    writing = 0
    coding = 0
    composing = 0
    
    inventory = Inventory()
    time=Time(24)
    day=0
    
init python:
    writing = 0
    def display_stats_overlay():
        if config.developer:
            text_show = ""
            text_show += "Art: " + str(art)
            text_show += "\nWriting: " + str(writing)
            text_show += "\nCoding: " + str(coding)
            text_show += "\nComposing: " + str(composing)
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
            $ my_text = "Art: " + str(art)
            text my_text
            textbutton "+" action If( points > 0 and art < 10, true = [ SetVariable("art", art + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and art > art_min, true = [ SetVariable("art", art - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Writing: " + str(writing)
            text my_text
            textbutton "+" action If( points > 0 and writing < 10, true = [ SetVariable("writing", writing + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and writing > writing_min, true = [ SetVariable("writing", writing - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Coding: " + str(coding)
            text my_text
            textbutton "+" action If( points > 0 and coding < 10, true = [ SetVariable("coding", coding + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and coding > coding_min, true = [ SetVariable("coding", coding - 1), SetVariable("points", points + 1) ], false = None )
            
        hbox:
            $ my_text = "Composing: " + str(composing)
            text my_text
            textbutton "+" action If( points > 0 and composing < 10, true = [ SetVariable("composing", composing + 1), SetVariable("points", points - 1) ], false = None )
            textbutton "-" action If( points < 6 and composing > composing_min, true = [ SetVariable("composing", composing - 1), SetVariable("points", points + 1) ], false = None )

        textbutton "OK" action Return()
            
