init python:
    showGameMaker = False # a flag that toggles visibility of the henpie game maker

    class Game:
        def __init__(self):
            self.started = False
            self.scope = 10000
            self.gameplay = None
            self.relationship = None
            self.genre = None
            self.title = ""
            self.commercial = False

            self.coding_done = 0.0
            self.coding_needed = 1.0
            self.writing_done = 0.0
            self.writing_needed = 1.0
            self.art_done = 0.0
            self.art_needed = 1.0
            self.music_done = 0.0
            self.music_needed = 1.0
            
            self.coding_quality = 0
            self.writing_quality = 0
            self.art_quality = 0
            self.music_quality = 0
            
            self.quality = 0.0
            
            self.downloads = 0
            self.sales = 0
            self.price = 0.0
            self.recommended_price = 0.0
            self.profits = 0.0
            
            self.bg = ""
            self.sp1 = ""
            self.sp2 = None
            
            
        def do_art(self, hours):
            # event = eventcheck("art")
            # if event[0]=="story":
                # renpy.jump(event[1])
            if self.art_done<self.art_needed:
                self.art_done += hours / (12.0-skills.art+random.randint(0,1))
                super_power_bonus = 0
                if skills.art>9:
                    super_power_bonus = int((skills.art-9)*10)
                self.art_done += super_power_bonus * hours / 8
                self.art_quality += skills.art * (hours / 2)
                return True
            else:
                return False
        def do_writing(self, hours):
            # event = eventcheck("writing")
            # if event[0]=="story":
                # renpy.jump(event[1])
            if self.writing_done<self.writing_needed:
                self.writing_done += hours / (12.0-skills.writing+random.randint(0,1))
                super_power_bonus = 0
                if skills.writing>9:
                    super_power_bonus = int((skills.writing-9)*10)
                self.art_done += super_power_bonus * hours / 8
                self.writing_quality += skills.writing * (hours / 2)
                return True
            else:
                return False
        def do_coding(self, hours):
            # event = eventcheck("coding")
            # if event[0]=="story":
                # renpy.jump(event[1])
            if self.coding_done<self.coding_needed:
                self.coding_done += hours / (12.0-skills.coding+random.randint(0,1))
                
                super_power_bonus = 0
                if skills.coding>9:
                    super_power_bonus = int((skills.coding-9)*10)
                self.art_done += super_power_bonus * hours / 8
                
                self.coding_quality += skills.coding * (hours / 2)
                return True
            else:
                return False
        def do_music(self, hours):
            # event = eventcheck("music")
            # if event[0]=="story":
                # renpy.jump(event[1])
            if self.music_done<self.music_needed:
                self.music_done += hours / (12.0-skills.music+random.randint(0,1))
                super_power_bonus = 0
                if skills.music>9:
                    super_power_bonus = int((skills.music-9)*10)
                self.art_done += super_power_bonus * hours / 8
                self.music_quality += skills.music * (hours / 2)
                return True
            else:
                return False
        
        def publish(self):
            event = eventcheck("publish")
            if event[0]=="story":
                renpy.jump(event[1])
            all_resources_done = True
            if self.writing_needed > self.writing_done:
                all_resources_done = False
            if self.coding_needed > self.coding_done:
                all_resources_done = False
            if self.music_needed > self.music_done:
                all_resources_done = False
            if self.art_needed > self.art_done:
                all_resources_done = False
            if all_resources_done:
                self.quality = (self.art_quality + self.writing_quality + self.coding_quality + self.music_quality) / (self.art_done + self.writing_done + self.coding_done + self.music_done)
                return True
            else:
                return False

screen game_button:
    hbox:
        if mygame.started: # game_in_progress:
            textbutton "Game stats" action Show("game_progress")
        else:
            textbutton "Game stats" action Show("game_progress")
            textbutton "Make a game!" action Show("new_game")
        
        if mygame.started:
            textbutton "Publish the game" action Jump("publish")

screen new_game:
    tag app
    modal True
    add "#FFF"
    
    default checkOptions = 0
    
    vbox xalign 0.5:
        null height 30
        text "Gameplay:" xalign 0.5 style "my_text"
        hbox xalign 0.5:
            textbutton "Visual Novel" action SetField(mygame, "gameplay", "vn")
            textbutton "Kinetic Novel" action SetField(mygame, "gameplay", "kn")
            textbutton "Role-Playing Game" action SetField(mygame, "gameplay", "rpg")
            textbutton "Simulation" action SetField(mygame, "gameplay", "sim")
        null height 30
        text "Relationship:" xalign 0.5 style "my_text"
        hbox xalign 0.5:
            textbutton "Boy pursues Girl" action SetField(mygame, "relationship", "bxg")
            textbutton "Boy pursues Boy" action SetField(mygame, "relationship", "bxb")
            textbutton "Girl pursues Boy" action SetField(mygame, "relationship", "gxb")
            textbutton "Girl pursues Girl" action SetField(mygame, "relationship", "gxg")
            textbutton "None" action SetField(mygame, "relationship", "none")
        null height 30
        text "Genre:" xalign 0.5 style "my_text"
        hbox xalign 0.5:
            textbutton "Mystery" action SetField(mygame, "genre", "mystery")
            textbutton "Comedy" action SetField(mygame, "genre", "comedy")
            textbutton "Horror" action SetField(mygame, "genre", "horror")
            textbutton "Sci-Fi" action SetField(mygame, "genre", "sci-fi")
            textbutton "Romance" action SetField(mygame, "genre", "romance")
            textbutton "Fantasy" action SetField(mygame, "genre", "fantasy")
            textbutton "Slice of life" action SetField(mygame, "genre", "slice")
        null height 30
        text "Word count:" xalign 0.5 style "my_text"
        hbox xalign 0.5:
            textbutton "-" action If( mygame.scope > 10000, true = [ SetField(mygame, "scope", mygame.scope - 10000)], false = None )
            #$ my_text = str(mygame.scope)
            #$ my_text = "{:,.2d}".format(mygame.scope)
            $ my_text = "{:8,d}".format(mygame.scope)
            text my_text style "my_text"
            textbutton "+" action If( mygame.scope < 200000, true = [ SetField(mygame, "scope", mygame.scope + 10000)], false = None )
        null height 30
        text "Commercial?" xalign 0.5 style "my_text"
        hbox xalign 0.5:
            textbutton "Yes" action SetField(mygame, "commercial", True)
            textbutton "No" action SetField(mygame, "commercial", False)
        null height 30
        hbox xalign 0.5:
            textbutton "Cancel" action SetVariable("showGameMaker", False)
            if mygame.gameplay and mygame.relationship and mygame.genre and mygame.scope:
                textbutton "OK" action [SetField(mygame, "started", True), SetVariable("showGameMaker", False), Return("henpieNewGame")]
            else:
                textbutton "OK" action [[]]

label publish:
    if mygame.publish():
        $ make_cover(mygame)
        $ games.append(mygame)
        if mygame.commercial:
            $ repBonus += 0.1
        else:
            $ repBonus += 1.0
        #$ oldgame = mygame
        $ mygame = Game()
        # show screen show_cover(game=oldgame)
        
        $ event = eventcheck("release")
        if event[0]=="story":
            $ renpy.jump(event[1])
        
        
    else:
        "It's not finished!"
        if debug:
            "But let's go ahead and cheat."
            $ mygame.publish()
            $ make_cover(mygame)
            $ games.append(mygame)
            $ mygame = Game()
    jump sim
    
init:
    style henpie:
        size 18
        font "Assets/gui/labtop_secundo_superwide.ttf"
        color "#4d6c83"
        
    style henpy_button:
        background None
        xmargin 0
        #ymargin 0
        xpadding 0
        ypadding 0
        
        ysize 10
        #ymaximum 10
        
    style henpy_button_text is henpie:
        selected_color "#fff"
        selected_background "#78a5c5"
        hover_color "#d86c46"
        
        
label edit_name:
    call screen edit_name(mygame.title)
    $ mygame.title = _return
    return
        
screen edit_name(game_name=""):
    add "#000"
    window:
        has vbox
        text "Enter a new name:"
        input default game_name

screen game_progress(curr_game = mygame):
    tag app
    modal True
    if not showGameMaker:
        use computer
        use window_frame("HenPie", "icon16_henpie", Return("desktop"), width=800, height=600)
        $ win_x=27
        $ win_y=47
        #add "Assets/gui/henpie.png" xpos win_x ypos win_y
        
        window background "Assets/gui/henpie.png" xmaximum 800 xminimum 800 ymaximum 600 yminimum 600 anchor(0.0, 0.0) xpos 27 ypos 47:
            hbox:
                text curr_game.title style "henpie" size 22 color "#565656" xpos 318 ypos 65
                if mygame.started and curr_game == mygame:
                    textbutton "- change" action ui.callsinnewcontext("edit_name") style "henpy_button" xpos 330 ypos 65
            
            window background None xmaximum 290 xminimum 290 ymaximum 250 yminimum 250 anchor(0.0, 0.0) xpos 10 ypos 156:
                viewport id "vp_games":
                    mousewheel True             
                    vbox:
                        spacing 0
                        if mygame.started:
                            textbutton mygame.title action Show("game_progress") style "henpy_button" size_group "games_list" left_margin 20
                        for g in games:
                            textbutton g.title action Show("game_progress", curr_game = g) style "henpy_button" size_group "games_list" left_margin 20
                vbar value YScrollValue("vp_games")

            if not mygame.started:
                textbutton "+ Create New Project" action SetVariable("showGameMaker", True) style "henpy_button" xpos 5 ypos 415
            
            if 1==1:
                window background None xmaximum 215 xminimum 215 ymaximum 100 yminimum 100 anchor(0.0, 0.0) xpos 323 ypos 148:
                    vbox:
                        hbox:
                            $ my_text = "{:8,d}".format(mygame.scope)
                            text "word count: [my_text]" style "henpie"
                        hbox:
                            text "gameplay: " style "henpie"
                            $ my_text = curr_game.gameplay
                            if my_text == "sim":
                                $ my_text = my_text.title()
                            else:
                                if my_text:
                                    $ my_text = my_text.upper()
                            text str(my_text) style "henpie"
                        hbox:
                            text "relationship: " style "henpie"
                            $ my_text = curr_game.relationship
                            if my_text:
                                $ my_text = my_text[0].upper() + my_text[1] + my_text[2].upper()
                            
                            text str(my_text) style "henpie"
                        hbox:
                            text "genre: " style "henpie"
                            
                            text str(curr_game.genre) style "henpie"
                        hbox:
                            text "commercial: " style "henpie"
                            if curr_game.commercial:
                                text "yes" style "henpie"
                            else:
                                text "no" style "henpie"

                        
                        
                window background None xmaximum 215 xminimum 215 ymaximum 100 yminimum 100 anchor(0.0, 0.0) xpos 568 ypos 148:
                    if curr_game==mygame and mygame.started:
                        grid 3 4:
                            text "writing:" style "henpie"
                            #bar value mygame.writing_done range mygame.writing_needed style "stat_bar" xpos -100
                            hbox:
                                text str(round(mygame.writing_done, 2)) style "henpie"
                                text "/" style "henpie"
                                text str(mygame.writing_needed) style "henpie"
                            $completion = round(((mygame.writing_done/mygame.writing_needed)*100),2) 
                            text " ([completion] %)" style "henpie"
                            
                            text "art:" style "henpie"
                            #bar value mygame.art_done range mygame.art_needed style "stat_bar" xpos -100
                            hbox:
                                text str(round(mygame.art_done, 2)) style "henpie"
                                text "/" style "henpie"
                                text str(mygame.art_needed) style "henpie"
                            $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                            text " ([completion] %)" style "henpie"
                            
                        
                            text "music:" style "henpie"
                            #bar value mygame.music_done range mygame.music_needed style "stat_bar" xpos -100
                            hbox:
                                text str(round(mygame.music_done, 2)) style "henpie"
                                text "/" style "henpie"
                                text str(mygame.music_needed) style "henpie"
                            $completion = round(((mygame.music_done/mygame.music_needed)*100),2) 
                            text " ([completion] %)" style "henpie"  
                        
                            text "coding:" style "henpie"
                            #bar value mygame.coding_done range mygame.coding_needed style "stat_bar" xpos -100
                            hbox:
                                text str(round(mygame.coding_done, 2)) style "henpie"
                                text "/" style "henpie"
                                text str(mygame.coding_needed) style "henpie"
                            $completion = round(((mygame.coding_done/mygame.coding_needed)*100),2) 
                            text " ([completion] %)" style "henpie"  
                    else:
                        hbox:
                            text "Quality:" style "henpie"
                            $ quality = round(curr_game.quality,2)
                            text str(quality) style "henpie"
                            
                            
                
                            
                if mygame.started:
                    textbutton "Release the Game" action [Hide("game_progress"), Jump("publish")] xpos 550 ypos 490 style "henpy_button" text_size 24
                    
                textbutton "quit" action Return("desktop") xpos 725 ypos 530 style "henpy_button" text_size 12






                            
        if 1==2:
            vbox:
                hbox:
                    for g in games:
                        textbutton g.title action Show("game_progress", curr_game = g)
            
                hbox:
                    text "Title: " style "my_text"
                    text curr_game.title style "my_text"
                    ##Title could be automatically generated based on your choices and maybe editable. Just for flavor.
                    ##textbutton "Change" action Show("change_game_name")
                hbox:
                    $ my_text = "{:8,d}".format(mygame.scope)
                    text "Word count: [my_text]" style "my_text"
                hbox:
                    text "gameplay: " style "my_text"
                    text str(curr_game.gameplay) style "my_text"
                hbox:
                    text "relationship: " style "my_text"
                    text str(curr_game.relationship) style "my_text"
                hbox:
                    text "genre: " style "my_text"
                    text str(curr_game.genre) style "my_text"
                    
                hbox:
                    text "Commercial: " style "my_text"
                    if curr_game.commercial:
                        text "Yes" style "my_text"
                    else:
                        text "No" style "my_text"
                if curr_game==mygame:
                    #hbox:
                    grid 4 4:
                        text "Writing:" style "my_text"
                        bar value mygame.writing_done range mygame.writing_needed style "stat_bar" xpos -100
                        hbox:
                            text str(round(mygame.writing_done, 2)) style "my_text"
                            text "/" style "my_text"
                            text str(mygame.writing_needed) style "my_text"
                        $completion = round(((mygame.writing_done/mygame.writing_needed)*100),2) 
                        text " ([completion] %)" style "my_text"
                        
                        
                        #bar value mygame.writing_done range mygame.writing_needed
                    
                        text "Art:" style "my_text"
                        bar value mygame.art_done range mygame.art_needed style "stat_bar" xpos -100
                        hbox:
                            text str(round(mygame.art_done, 2)) style "my_text"
                            text "/" style "my_text"
                            text str(mygame.art_needed) style "my_text"
                        $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                        text " ([completion] %)" style "my_text"
                        
                    
                        text "Music:" style "my_text"
                        bar value mygame.music_done range mygame.music_needed style "stat_bar" xpos -100
                        hbox:
                            text str(round(mygame.music_done, 2)) style "my_text"
                            text "/" style "my_text"
                            text str(mygame.music_needed) style "my_text"
                        $completion = round(((mygame.music_done/mygame.music_needed)*100),2) 
                        text " ([completion] %)" style "my_text"  
                    
                        text "Coding:" style "my_text"
                        bar value mygame.coding_done range mygame.coding_needed style "stat_bar" xpos -100
                        hbox:
                            text str(round(mygame.coding_done, 2)) style "my_text"
                            text "/" style "my_text"
                            text str(mygame.coding_needed) style "my_text"
                        $completion = round(((mygame.coding_done/mygame.coding_needed)*100),2) 
                        text " ([completion] %)" style "my_text"  
                else:
                    hbox:
                        text "Quality:"
                        text str(curr_game.quality)
                hbox:
                    textbutton "Back" action Hide("game_progress")

    else:
        use new_game
