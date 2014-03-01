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
    drawing = 0
    
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
    add "gui/char_select_bg.jpg"
    imagebutton auto "gui/artist_%s.png" focus_mask True xpos 200 ypos 200 action Return("artist") #at main_effect2_var
    imagebutton auto "gui/writer_%s.png" focus_mask True xpos 600 ypos 200 action Return("writer") #at main_effect2_var
    imagebutton auto "gui/programmer_%s.png" focus_mask True xpos 200 ypos 400 action Return("programmer") #at main_effect2_var
    imagebutton auto "gui/composer_%s.png" focus_mask True xpos 600 ypos 400 action Return("composer") #at main_effect2_var
    

screen set_attributes(cclass):
        
    default cclass  = ''
    default pointsPower = 10
    default drawing = 0
    default points  = 0
 
    vbox:
        text "Selected class: [cclass]"
        text "Points: [points]"
        
    hbox:
        text "Drawing: [drawing]"

        # Unsure if it works but it probably does
        textbutton "+" action If( pointsPower > 0, true = [ SetVariable("drawing", drawing + 1), SetVariable("pointsPower", pointsPower - 1) ], false = None )
        textbutton "-" action If( pointsPower > 0, true = [ SetVariable("drawing", drawing - 1), SetVariable("pointsPower", pointsPower + 1) ], false = None )

