init python:
    
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
            self.coding_needed = 0.0
            self.writing_done = 0.0
            self.writing_needed = 0.0
            self.art_done = 0.0
            self.art_needed = 0.0
            self.music_done = 0.0
            self.music_needed = 0.0
            
            self.coding_quality = 0
            self.writing_quality = 0
            self.art_quality = 0
            self.music_quality = 0
            
            self.quality = 0.0
            
            self.downloads = 0
            self.price = 0.0
            self.profits = 0.0
            
            self.bg = ""
            self.sp1 = ""
            self.sp2 = None
            
            
        def do_art(self, hours):
            if self.art_done<self.art_needed:
                self.art_done += hours / (11.0-skills.art) / 2
                self.art_quality += skills.art * (hours / 2)
                return True
            else:
                return False
        def do_writing(self, hours):
            if self.writing_done<self.writing_needed:
                self.writing_done += hours / (11.0-skills.writing) / 2
                self.writing_quality += skills.writing * (hours / 2)
                return True
            else:
                return False
        def do_coding(self, hours):
            if self.coding_done<self.coding_needed:
                self.coding_done += hours / (11.0-skills.coding) / 2
                self.coding_quality += skills.coding * (hours / 2)
                return True
            else:
                return False
        def do_music(self, hours):
            if self.music_done<self.music_needed:
                
                self.music_done += hours / (11.0-skills.music) / 2
                self.music_quality += skills.music * (hours / 2)
                return True
            else:
                return False
        
        def publish(self):
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
            textbutton "Make a game!" action Show("new_game")
        
        if mygame.started:
            textbutton "Publish the game" action Jump("publish")

screen new_game:
    tag game
    modal True
    add "#FFF"
    
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
            textbutton "Cancel" action Hide("new_game")
            textbutton "OK" action [SetField(mygame, "started", True), Hide("new_game"), Jump("new_game")]

label new_game:
    call name_gen
            
    python:
        mygame.price = 0.0
        coding_needed = random.randint(1, 3)
        coding_needed += int(mygame.scope/10000) * 4
        if mygame.gameplay=="sim":
            coding_needed += 16
            mygame.price = 5.0
        if mygame.gameplay=="rpg":
            coding_needed += 24
            mygame.price = 10.0
        #coding_needed = coding_needed * (11-coding)
        mygame.coding_needed = coding_needed

        sprites_needed = random.randint(2, 4) + int(mygame.scope/20000)
        bgs_needed = random.randint(2, 4) + int(mygame.scope/20000)
        if mygame.gameplay=="rpg":
            sprites_needed += 4 + int(mygame.scope/20000)*2
            bgs_needed += 4 + int(mygame.scope/20000)*2
        cgs_needed = int(mygame.scope/10000)
        art_needed = 2*sprites_needed + 4*bgs_needed + 4*cgs_needed
        #art_needed = art_needed * (11-art)
        mygame.art_needed = art_needed / 2
        
        music_needed = random.randint(4, 8) + int(mygame.scope/20000)
        mygame.music_needed = music_needed
        
        writing_needed = int(mygame.scope/1000)
        mygame.writing_needed = writing_needed

        mygame.price += int(mygame.scope/10000)
# -->Resources are determined by your selections (scope and gameplay)
    
# Coding: with max coding skill(10): 4 hours + 4h for every 10,000 words; add 16h for sim and 24h for RPG. With coding skill 1: everything takes 10 times longer.

# Art: 2-4 sprites (random) + another one for every 20,000 words; if it's an RPG: add 4 more and add 2 for every 20,000 words
# 2-4 BGs (random) + another one for every 20,000 words; if it's an RPG: add 4 more and add 2 for every 20,000 words
# 1 CG for every 10,000 words
# With max art skill(10): sprite takes 2h, BG/CG takes 4h. With art skill 1: everything takes 10 times longer.

# Music: 2-4 songs (random) + another one for every 20,000 words
# With max music skill(10): track takes 1h. With music skill 1: everything takes 10 times longer.

# Writing: With max writing skill(10): 1,000 words/h. With writing skill 1: everything takes 10 times longer.


    jump sim
    
label publish:
    if mygame.publish():
        $ make_cover(mygame)
        $ games.append(mygame)
        $ mygame = Game()
    else:
        "It's not finished!"
        
        "But let's go ahead and cheat."
        # $ self.coding_done = self.coding_needed
        # $ self.writing_done = self.writing_needed
        # $ self.art_done = self.art_needed
        # $ self.music_done = self.music_needed
        
        $ mygame.publish()
        $ make_cover(mygame)
        $ games.append(mygame)
        
        $ mygame = Game()
    jump sim
    
screen game_progress(curr_game = mygame):
    tag game
    modal True
    add "#FFF"
    
    vbox:
        hbox:
            for g in games:
                textbutton g.title action Show("game_progress", curr_game = g)

    
        hbox:
            text "Title: " style "my_text"
            text curr_game.title style "my_text"
            #Title could be automatically generated based on your choices and maybe editable. Just for flavor.
            #textbutton "Change" action Show("change_game_name")
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

            

            