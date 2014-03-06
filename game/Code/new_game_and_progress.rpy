init python:
    import random
    class Game:
        def __init__(self):
            self.started = False
            self.scope = 10000
            self.gameplay = None
            self.relationship = None
            self.genre = None
            self.title = "YAOELVN"
            self.commercial = False

            self.coding_done = 0
            self.coding_needed = None
            self.writing_done = 0
            self.writing_needed = None
            self.art_done = 0
            self.art_needed = None
            self.music_done = 0
            self.music_needed = None
        def do_art(self, hours):
            if self.art_done<self.art_needed:
                self.art_done += hours / (11.0-skills.art) / 2
                return True
            else:
                return False
        def do_writing(self, hours):
            if self.writing_done<self.writing_needed:
                self.writing_done += hours / (11.0-skills.writing) / 2
                return True
            else:
                return False
        def do_coding(self, hours):
            if self.coding_done<self.coding_needed:
                self.coding_done += hours / (11.0-skills.coding) / 2
                return True
            else:
                return False
        def do_music(self, hours):
            if self.music_done<self.music_needed:
                self.music_done += hours / (11.0-skills.music) / 2
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
    add "#000"
    
    vbox:
        hbox:
            text "Gameplay:"    
            textbutton "Visual Novel" action SetField(mygame, "gameplay", "vn")
            textbutton "Kinetic Novel" action SetField(mygame, "gameplay", "kn")
            textbutton "Role-Playing Game" action SetField(mygame, "gameplay", "rpg")
            textbutton "Simulation" action SetField(mygame, "gameplay", "sim")
        hbox:
            text "Relationship:"
            textbutton "Boy pursues Girl" action SetField(mygame, "relationship", "bxg")
            textbutton "Boy pursues Boy" action SetField(mygame, "relationship", "bxb")
            textbutton "Girl pursues Boy" action SetField(mygame, "relationship", "gxb")
            textbutton "Girl pursues Girl" action SetField(mygame, "relationship", "gxg")
            textbutton "None" action SetField(mygame, "relationship", "none")
        hbox:
            text "Genre:"
            textbutton "Mystery" action SetField(mygame, "genre", "mystery")
            textbutton "Comedy" action SetField(mygame, "genre", "comedy")
            textbutton "Horror" action SetField(mygame, "genre", "horror")
            textbutton "Sci-Fi" action SetField(mygame, "genre", "sci-fi")
            textbutton "Romance" action SetField(mygame, "genre", "romance")
            textbutton "Fantasy" action SetField(mygame, "genre", "fantasy")
            textbutton "Drama" action SetField(mygame, "genre", "drama")
            
    
        hbox:
            text "Scope / wordcount:"
            $ my_text = str(mygame.scope)
            text my_text
            textbutton "+" action If( mygame.scope < 200000, true = [ SetField(mygame, "scope", mygame.scope + 10000)], false = None )
            textbutton "-" action If( mygame.scope > 10000, true = [ SetField(mygame, "scope", mygame.scope - 10000)], false = None )

        hbox:
            text "Commercial:"
            textbutton "Yes" action SetField(mygame, "commercial", True)
            textbutton "No" action SetField(mygame, "commercial", False)

        hbox:
            textbutton "Cancel" action Hide("new_game")
            textbutton "OK" action [SetField(mygame, "started", True), Hide("new_game"), Jump("new_game")]
    
label new_game:
    call name_gen
            
    python:
        coding_needed = random.randint(1, 3)
        coding_needed += int(mygame.scope/10000) * 4
        if mygame.gameplay=="sim":
            coding_needed += 16
        if mygame.gameplay=="rpg":
            coding_needed += 24
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
        mygame.art_needed = art_needed
        
        music_needed = random.randint(4, 8) + int(mygame.scope/20000)
        mygame.music_needed = music_needed
        
        writing_needed = int(mygame.scope/1000)
        mygame.writing_needed = writing_needed

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
    $ all_resources_done = True
    if mygame.writing_needed > mygame.writing_done:
        $ all_resources_done = False
    if mygame.coding_needed > mygame.coding_done:
        $ all_resources_done = False
    if mygame.music_needed > mygame.music_done:
        $ all_resources_done = False
    if mygame.art_needed > mygame.art_done:
        $ all_resources_done = False
    if all_resources_done:
        $ games.append(mygame)
        $ mygame = Game()
    else:
        "It's not finished!"
    
    jump sim
    
screen game_progress(curr_game = mygame):
    tag game
    modal True
    add "#000"
    
    
    vbox:
        hbox:
            for g in games:
                textbutton g.title action Show("game_progress", curr_game = g)

    
        hbox:
            text "Name:"
            text curr_game.title
            #Title could be automatically generated based on your choices and maybe editable. Just for flavor.
            #textbutton "Change" action Show("change_game_name")
        hbox:
            text str(curr_game.scope)
        hbox:
            text str(curr_game.gameplay)
        hbox:
            text str(curr_game.relationship)
        hbox:
            text str(curr_game.genre)
            
        hbox:
            text "Commercial"
            if curr_game.commercial:
                text "Yes"
            else:
                text "No"
        if curr_game==mygame:
            hbox:
                text "Writing:"
                text str(mygame.writing_done)
                text "/"
                text str(mygame.writing_needed)
                #bar value mygame.writing_done range mygame.writing_needed
            hbox:
                text "Art:"
                text str(mygame.art_done)
                text "/"
                text str(mygame.art_needed)
                #bar value mygame.art_done range mygame.art_needed
            hbox:
                text "Music:"
                text str(mygame.music_done)
                text "/"
                text str(mygame.music_needed)
                #bar value mygame.music_done range mygame.music_needed            
            hbox:
                text "Coding:"
                text str(mygame.coding_done)
                text "/"
                text str(mygame.coding_needed)
                #bar value mygame.coding_done range mygame.coding_needed

        hbox:
            textbutton "Back" action Hide("game_progress")

            

            