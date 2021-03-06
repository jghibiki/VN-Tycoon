
label computer:
    scene computer
    python:
        computerLoop = True
        showDesktop = True
        showBrowser = False
        showSentence = False
        showMikie = False
        showNotepad = False
        showGrunge = False
        showHenPie = False
        selTime = False
    while(computerLoop):
        #show screens
        if showDesktop:
            call screen computer
        elif showBrowser and type(showBrowser) == bool:
            call screen webBrowser
        elif showBrowser == "lsf":
            call screen lsf
        elif showBrowser == "tarzan":
            call screen tarzan
        elif showBrowser == "lsf_recruitment":
            call screen lsf_recruitment
        elif showBrowser == "lsf_messages":
            call screen lsf_messages
#        elif showBrowser == "stalkmeplz":
#            call screen stalkMePlz
        elif showBrowser == "BMTMezzo":
            call screen game_list
        elif showSentence and type(showSentence) == bool:
            call screen sentence
        elif showMikie and type(showMikie) == bool:
            call screen mikie
        elif showNotepad and type(showNotepad) == bool:
            call screen notepad
        elif showGrunge and type(showGrunge) == bool:
            call screen grunge
        elif showHenPie and  type(showHenPie) == bool:
            call screen game_progress
        
        
                
        #parse returns
        if _return == "web_browser":
            $showDesktop = False
            $showBrowser = True
            $showSentence = False
            $showMikie = False
            $showNotepad = False
            $showGrunge = False
            $showHenPie = False
        if _return == "leave":
            return # or maybe jump to sim instead
        if _return == "lsf":
            $showBrowser = "lsf"
        if _return == "tarzan":
            $showBrowser = "tarzan"
        if _return == "lsf_recruitment":
            $showBrowser = "lsf_recruitment"
        if _return == "lsf_messages":
            $showBrowser = "lsf_messages"
        if _return == "stalkmeplz":
            $showBrowser = "stalkmeplz"
        if _return == "BMTMezzo":
            $showBrowser = "BMTMezzo"
        if _return == "desktop":
            $showDesktop = True
            $showBrowser = False
            $showSentence = False
            $showMikie = False
            $showNotepad = False
            $showGrunge = False
            $showHenPie = False
        if _return == "open_sentence":
            $showDesktop = False
            $showSentence = True
        if _return == "open_mikie":
            $showMikie = True
            $showDesktop = False
        if _return == "open_notepad":
            $showNotepad = True
            $showDesktop = False
        if _return == "open_grunge":
            $showGrunge = True
            $showDesktop = False
        if _return == "game_progress":
            $showHenPie = True
            $showDesktop = False
            
        if _return == "henpieNewGame":
            python:
                nameGen()
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
                mygame.recommended_price = mygame.price
                mygame.price += random.uniform(-1*(mygame.price/3), mygame.price/3)
                
                event = eventcheck("new_game")
                if event[0]=="story":
                    renpy.jump(event[1])

                showGameMake = False
                # -->Resources are determined by your selections (scope and gameplay)
                    
                # Coding: with max coding skill(10): 4 hours + 4h for every 10,000 words; add 16h for sim and 24h for RPG. With coding skill 1: everything takes 10 times longer.

                # Art: 2-4 sprites (random) + another one for every 20,000 words; if it's an RPG: add 4 more and add 2 for every 20,000 words
                # 2-4 BGs (random) + another one for every 20,000 words; if it's an RPG: add 4 more and add 2 for every 20,000 words
                # 1 CG for every 10,000 words
                # With max art skill(10): sprite takes 2h, BG/CG takes 4h. With art skill 1: everything takes 10 times longer.

                # Music: 2-4 songs (random) + another one for every 20,000 words
                # With max music skill(10): track takes 1h. With music skill 1: everything takes 10 times longer.

                # Writing: With max writing skill(10): 1,000 words/h. With writing skill 1: everything takes 10 times longer.

            
        if type(_return) == tuple:
            if _return[0] == "tarzanAdd":
                $tarzanCart.append(tarzanStore.pop(_return[1]))
            if _return[0] == "tarzanRemove":
                $tarzanStore.append(tarzanCart.pop(_return[1]))
            if _return[0] == "replyThread":
                
                $ event = eventcheck()
                if threads[_return[1]].output == "art":
                    $ event = eventcheck("hire_artist")
                if threads[_return[1]].output == "coding":
                    if threads[_return[1]].input == "money":
                        $ event = eventcheck("hire_coder_money")
                    else:
                        $ event = eventcheck("hire_coder")
                if threads[_return[1]].output == "writing":
                    $ event = eventcheck("hire_writer")
                if threads[_return[1]].output == "music":
                    $ event = eventcheck("hire_composer")
                
                $ messages.append(threads.pop(_return[1]))
                
                if event[0]=="story":
                    $ renpy.jump(event[1])
                    
            if _return[0] == "msgReply":
                #first gather work 
                $turnedIn = False
                if messages[_return[1]].input == "money":
                    if inventory.money >= messages[_return[1]].inputQuantity:
                        $inventory.money -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        $needed = messages[_return[int(1)]].inputQuantity
                        "You don't have enough money yet! (Must have $[needed])."
                elif messages[_return[1]].input == "art":
                    if comishWork.art >= messages[_return[1]].inputQuantity:
                        $comishWork.art -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        $needed = messages[_return[int(1)]].inputQuantity
                        "You don't have enough art to turn in! (Must have [needed])"
                elif messages[_return[1]].input == "coding":
                    if comishWork.coding >= messages[_return[1]].inputQuantity:
                        $comishWork.coding -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        $needed = messages[_return[int(1)]].inputQuantity
                        "You don't have enough code written to turn in! (Must have [needed])"
                elif messages[_return[1]].input == "music":
                    if comishWork.music >= messages[_return[1]].inputQuantity:
                        $comishWork.music -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        $needed = messages[_return[int(1)]].inputQuantity
                        "You don't have enough music written to turn in! (Must have [needed])"
                elif messages[_return[1]].input == "writing":
                    if comishWork.writing >= messages[_return[1]].inputQuantity:
                        $comishWork.writing -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        $needed = messages[_return[int(1)]].inputQuantity
                        "You don't have enough writing done to turn in! (Must have [needed])"
                #then provide reward
                if turnedIn:
                    $messages[_return[1]].stage = "response"
                    $ skill_tmp = (repBonus * 10)
                    if skill_tmp > 6:
                        $ skill_tmp = 6
                    $ quantity_tmp = messages[_return[1]].outputQuantity
                    
                    if messages[_return[1]].output == "money":
                        $inventory.money += quantity_tmp
                    elif messages[_return[1]].output == "art":
                        $mygame.art_done += quantity_tmp
                        $mygame.art_quality += skill_tmp * (quantity_tmp/2)
                    elif messages[_return[1]].output == "coding":
                        $mygame.coding_done += quantity_tmp
                        $mygame.coding_quality += skill_tmp * (quantity_tmp / 2)
                    elif messages[_return[1]].output == "music":
                        $mygame.music_done += quantity_tmp
                        $mygame.music_quality += skill_tmp * (quantity_tmp / 2)
                    elif messages[_return[1]].output == "writing":
                        $mygame.writing_done += quantity_tmp
                        $mygame.writing_quality += skill_tmp * (quantity_tmp / 2)
                    ###
                    $ repBonus += .1
                    ###
            if _return[0] == "msgDelete":
                $messages.pop(_return[1])
        if _return == "tarzanBuy":
            $totalPrice = 0
            $item = 0
            $rejects = []
            while(item < len(tarzanCart)):
                  #add price to total
                  $totalPrice += tarzanCart[item].price
                  
                  #check to see if this item is one of the unlockables
                  if tarzanCart[item] == keyboard:
                        if not inventory.has_item(keyboard):
                            if inventory.buy(keyboard):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased a keyboard, Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy a keyboard."
                                $rejects.append(item)
                        else:
                            "You already own this item!"
                  elif tarzanCart[item] == book_c:
                        if not inventory.has_item(book_c):
                            if inventory.buy(book_c):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased \"Composing for Morons\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Composing for Morons\". Moron. Get a job and try again."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_w:
                        if not inventory.has_item(book_w):
                            if inventory.buy(book_w):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased \"Writing for the Asinine\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Writing for the Asinine\". Shows how much of an {b}ASS{/b}inine fool you are."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_p:
                        if not inventory.has_item(book_p):
                            if inventory.buy(book_p):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased \"Programming for Idiots\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Programming for Idiots\". Come on! Only idiots read books to learn to program. I mean, \"Hello!?\", the internet was invented, what 60+ years ago?."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_d:
                        if not inventory.has_item(book_d):
                            if inventory.buy(book_d):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased \"Drawing for Losers\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Drawing for Losers\". There is only one type of person that would try to buy a book they couldn't affort. A {i}LOSER{/i}."
                                $rejects.append(item)

                  elif tarzanCart[item] == tablet:
                        if not inventory.has_item(tablet):
                            if inventory.buy(tablet):
                                $ event = eventcheck("purchase")
                                if event[0]=="story":
                                    $ renpy.jump(event[1])
                                "You have purcased \"Drawing Tablet\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy a \"Drawing Tablet\"."
                                $rejects.append(item)
                  $item += 1
            $item = 0
            while item < len(rejects):
                $tarzanStore.append(tarzanCart[item])
                $item += 1
            $tarzanCart = [] #clear the cart
            
        if type(_return) == tuple:
            if _return[0] == "select_time":
                $selTime = _return[1]
                
        if type(_return) == type(""): #string
            if _return[0] == "a" or _return[0] == "p" or _return[0] == "w":
                $selTime = None
                if showMikie:
                    $dur = int(_return[1])
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
                            $result = comishWork.increase("art", dur)
                            if type(result) == bool and result:                               
                                call drawingAnimation
                            elif result == "fail":
                                "You should try practicing before joining the big boys."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to draw."
                    else:
                        if time.dec(dur):
                            $mygame.do_art(dur)
                            call drawingAnimation
                            $ event = eventcheck("art")
                            if event[0]=="story":
                                $ renpy.jump(event[1])
                        else:
                            "You are too sleepy to draw."
                elif showSentence:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("writing", dur):
                                call  writingAnimation
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to write."

                    elif _return[0] == "w":
                        if time.dec(dur):
                            $result = comishWork.increase("writing", dur)
                            if type(result) == bool and result:                               
                                call writingAnimation
                            elif result == "fail":
                                "You should try practicing before joining the big boys."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to write."
                    else: 
                        if time.dec(dur):
                            $mygame.do_writing(dur)
                            call  writingAnimation
                            $ event = eventcheck("writing")
                            if event[0]=="story":
                                $ renpy.jump(event[1])
                        else:
                            "You are too sleepy to write."

                elif showNotepad:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("coding", dur):
                                 call codingAnimation
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to code."
                    elif _return[0] == "w":
                        if time.dec(dur):
                            $result = comishWork.increase("coding", dur)
                            if type(result) == bool and result: 
                                call codingAnimation
                            elif result == "fail":
                                "You should practice more before trying to join the big boys."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to code."
                    else:
                        if time.dec(dur):
                            $mygame.do_coding(dur)
                            call codingAnimation
                            $ event = eventcheck("coding")
                            if event[0]=="story":
                                $ renpy.jump(event[1])
                        else:
                            "You are too sleepy to code."
                elif showGrunge:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("music", dur):
                                call  composingAnimation
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to compose."
                    elif _return[0] == "w":
                        if time.dec(dur):
                            $result = comishWork.increase("music", dur)
                            if type(result) == bool and result:
                                call composingAnimation
                            elif result == "fail":
                                "You should try practicing first before joining the big boys."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to compose."
                    else:
                        if time.dec(dur):
                            $mygame.do_music(dur)
                            call composingAnimation
                            $ event = eventcheck("music")
                            if event[0]=="story":
                                $ renpy.jump(event[1])
                        else:
                            "You are too sleepy to compose."           
                            
                            
#######################
## Computer Screens

init:
    image icon64_browser_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_browser.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_browser.png",0.5), vertical=True))
    image icon64_browser_hover = LiveComposite((64,100), (0,0), "icon64_browser_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_browser_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_browser.png", 32, 50))
    image icon32_browser_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_browser.png", 32, 50))
    image icon16_browser = im.Crop (im.Scale("Assets/gui/desk_browser.png", 16, 25), 0, 4, 16, 16)
    
    
    
    image icon64_sentence_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_sentence.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_sentence.png",0.5), vertical=True))
    image icon64_sentence_hover = LiveComposite((64,100), (0,0), "icon64_sentence_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_sentence_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_sentence.png", 32, 50))
    image icon32_sentence_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_sentence.png", 32, 50))
    image icon16_sentence = im.Crop (im.Scale("Assets/gui/desk_sentence.png", 16, 25), 0, 4, 16, 16)
    
    image icon64_michelangelo_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_michelangelo.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_michelangelo.png",0.5), vertical=True))
    image icon64_michelangelo_hover = LiveComposite((64,100), (0,0), "icon64_michelangelo_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_michelangelo_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_michelangelo.png", 32, 50))
    image icon32_michelangelo_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_michelangelo.png", 32, 50))
    image icon16_michelangelo = im.Crop (im.Scale("Assets/gui/desk_michelangelo.png", 16, 25), 0, 4, 16, 16)

    image icon64_player_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_music_player.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_music_player.png",0.5), vertical=True))
    image icon64_player_hover = LiveComposite((64,100), (0,0), "icon64_player_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_player_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_music_player.png", 32, 50))
    image icon32_player_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_music_player.png", 32, 50))
    image icon16_player = im.Crop (im.Scale("Assets/gui/desk_music_player.png", 16, 25), 0, 4, 16, 16)
    
    image icon64_notepad_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_notepad.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_notepad.png",0.5), vertical=True))
    image icon64_notepad_hover = LiveComposite((64,100), (0,0), "icon64_notepad_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_notepad_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_notepad.png", 32, 50))
    image icon32_notepad_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_notepad.png", 32, 50))
    image icon16_notepad = im.Crop (im.Scale("Assets/gui/desk_notepad.png", 16, 25), 0, 4, 16, 16)
    
    image icon64_henpie_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_henpie.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_henpie.png",0.5), vertical=True))
    image icon64_henpie_hover = LiveComposite((64,100), (0,0), "icon64_henpie_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_henpie_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_henpie.png", 32, 50))
    image icon32_henpie_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_henpie.png", 32, 50))
    image icon16_henpie = im.Crop (im.Scale("Assets/gui/desk_henpie.png", 16, 25), 0, 4, 16, 16)
    

    image icon64_grunge_band_idle = im.Composite((64,100), (0,0), "Assets/gui/desk_grunge_band.png" , (0,64), im.Flip(im.Alpha("Assets/gui/desk_grunge_band.png",0.5), vertical=True))
    image icon64_grunge_band_hover = LiveComposite((64,100), (0,0), "icon64_grunge_band_idle" , (0,0), "Assets/gui/desk_glow.png")
    image icon32_grunge_band_idle = im.Composite((59,40), (14,-5), im.Scale("Assets/gui/desk_grunge_band.png", 32, 50))
    image icon32_grunge_band_hover = im.Composite((59,40), (0,0), "Assets/gui/desk_hover.png", (14,-5), im.Scale("Assets/gui/desk_grunge_band.png", 32, 50))
    image icon16_grunge_band = im.Crop (im.Scale("Assets/gui/desk_grunge_band.png", 16, 25), 0, 4, 16, 16)
    
    
    
screen computer:
    if job=="writer":
        add "Assets/gui/desk_bg1.jpg"
    if job=="artist":
        add "Assets/gui/desk_bg1.jpg"
    if job=="coder":
        add "Assets/gui/desk_bg1.jpg"
    if job=="composer":
        add "Assets/gui/desk_bg1.jpg"
    
    if game_os == "win":
        add "Assets/gui/desk_tray.png" yalign 1.0
        imagebutton auto "Assets/gui/desk_win_start_%s.png" focus_mask True action [Hide("gui_tooltip"), Return("leave")] xpos 0 yalign 1.0
        $ x = 60
        
        imagebutton idle "icon32_browser_idle" hover "icon32_browser_hover" action [Hide("gui_tooltip"), Return("web_browser")] xpos x yanchor 1.0 ypos 1.0 
        $ x += 60
        
        imagebutton idle "icon32_sentence_idle" hover "icon32_sentence_hover" action [Hide("gui_tooltip"), Return("open_sentence")] xpos x yanchor 1.0 ypos 1.0 
        $ x += 60
        
        #imagebutton idle "icon32_michelangelo_idle" hover "icon32_michelangelo_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 1.0 
        #$ x += 60
        
        imagebutton idle "icon32_notepad_idle" hover "icon32_notepad_hover" action [Hide("gui_tooltip"), Return("open_notepad")] xpos x yanchor 1.0 ypos 1.0 
        
        $ x += 60
        imagebutton idle "icon32_grunge_band_idle" hover "icon32_grunge_band_hover" action [Hide("gui_tooltip"), Return("open_grunge")] xpos x yanchor 1.0 ypos 1.0 

        $ x += 60
        imagebutton idle "icon32_henpie_idle" hover "icon32_henpie_hover" action [Hide("gui_tooltip"), Return("game_progress")] xpos x yanchor 1.0 ypos 1.0

        #$ x += 60
        #imagebutton idle "icon32_player_idle" hover "icon32_player_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 1.0 
        
        
        
        
        
        $ Clocks (1282, 727, 12)
    else:
        add "Assets/gui/desk_menu_top.png" yalign 0.0
        add "Assets/gui/desk_dock.png" yalign 1.0
        imagebutton auto "Assets/gui/desk_mac_start_%s.png" action [Hide("gui_tooltip"), Return("leave")] xpos 0 ypos 0
        
        
        $ x = 190
        #imagebutton auto "icon64_browser_%s" action [Hide("gui_tooltip"), Return("web_browser")] xpos 190 yanchor 1.0 ypos 764 
        imagebutton idle "icon64_browser_idle" hover "icon64_browser_hover" action [Hide("gui_tooltip"), Return("web_browser")] xpos x yanchor 1.0 ypos 764 
        #hovered [Play("sound", "Assets/sfx/click.ogg"), Show("gui_tooltip", my_picture="tooltip_writer") ] unhovered [Hide("gui_tooltip")]
        #add "icon64_browser_flip" xpos 190 yanchor 1.0 ypos 818
        $ x += 80
        
        imagebutton idle "icon64_sentence_idle" hover "icon64_sentence_hover" action [Hide("gui_tooltip"), Return("open_sentence")] xpos x yanchor 1.0 ypos 764 
        #$ x += 80
        #imagebutton idle "icon64_michelangelo_idle" hover "icon64_michelangelo_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 764 
        
        $ x += 80
        imagebutton idle "icon64_notepad_idle" hover "icon64_notepad_hover" action [Hide("gui_tooltip"), Return("open_notepad")] xpos x yanchor 1.0 ypos 764 
        
        $ x += 80
        imagebutton idle "icon64_grunge_band_idle" hover "icon64_grunge_band_hover" action [Hide("gui_tooltip"), Return("open_grunge")] xpos x yanchor 1.0 ypos 764
        
        $ x += 80
        imagebutton idle "icon64_henpie_idle" hover "icon64_henpie_hover" action [Hide("gui_tooltip"), Return("game_progress")] xpos x yanchor 1.0 ypos 764 
        
        #$ x += 80
        #imagebutton idle "icon64_player_idle" hover "icon64_player_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 764 
        
        $ Clocks (1250, -2, 14, "000")
        
        
#    vbox: 
#        xpos 0.01
#        ypos 0.2
#        textbutton "Open Web Browser" action Return("web_browser")
#        textbutton "Open Sentence Word-processor" action Return("open_sentence")
#        textbutton "Open Michelangelo" action Return("open_mikie")
#        textbutton "Leave Computer" action Return("leave") 


#############################
## Word Processor (Sentence)
screen sentence(showOptions=True):
    tag app
    use computer
    use window_frame("Sentence", "icon16_sentence", Return("desktop"))
    add "Assets/gui/sentence.png"
    if showOptions:
        use select_time

############################################
## Drawing/Painting Software (Michelangelo)
screen mikie:
    tag app
    use computer
    use window_frame("Michelangelo", "icon16_michelangelo", Return("desktop"))
    use select_time


#########################
## Notepad (for coding)
screen notepad:
    tag app
    use computer
    use window_frame("Notepad--", "icon16_notepad", Return("desktop"))
    add "Assets/gui/notepad.png"
    use select_time

screen grunge:
    tag app
    use computer
    use window_frame("GrungeBand", "icon16_grunge_band", Return("desktop"))
    add "Assets/gui/grunge_band.png"
    use select_time

            
########################
## Web Browser Screens

##################
###   Web Browser
screen webBrowser:
    tag app
    use computer
    use window_frame("Icewolf", "icon16_browser", Return("desktop"))
    
    add "Assets/gui/browser_toolbar.png" xpos 29 ypos 74
    add "Assets/gui/browser_tab_selected.png" xpos 34 ypos 49
    #add "Assets/gui/browser_tab_idle.png" xpos 284 ypos 49
    
    $ my_bg = "Assets/gui/browser_tab_idle.png"
    if showBrowser == "lsf" or showBrowser == "lsf_recruitment" or showBrowser == "lsf_messages":    
        $ my_bg = "Assets/gui/browser_tab_selected.png"
    button background my_bg focus_mask True action Return("lsf") xpos 34 ypos 49:
        text "LemmingSoft Forums" color "#000" size 18

    $ my_bg = "Assets/gui/browser_tab_idle.png"
    if showBrowser == "tarzan":
        $ my_bg = "Assets/gui/browser_tab_selected.png"        
    button background my_bg focus_mask True action Return("tarzan") xpos 284 ypos 49:
        text "Tarzan Shop" color "#000" size 18

    $ my_bg = "Assets/gui/browser_tab_idle.png"
    if showBrowser == "BMTMezzo":
        $ my_bg = "Assets/gui/browser_tab_selected.png"        
    button background my_bg focus_mask True action Return("BMTMezzo") xpos 534 ypos 49:
        text "BMTMezzo" color "#000" size 18
   
    if showBrowser == "stalkmeplz":
        $ my_bg = "Assets/gui/browser_tab_selected.png"        
        button background my_bg focus_mask True action Return("stalkmeplz") xpos 784 ypos 49:
            text "stalkmeplz" color "#000" size 18
        
        

##############
###    Tarzan
screen tarzan:
    use webBrowser
    vbox:
        xpos 29 
        ypos 111
        hbox:
            if len(tarzanStore) != 0 or len(tarzanCart) != 0:
                vbox:
                    add "Assets/gui/logo_tarzan.png" xpos 50 ypos 20
                    #text "Tarzan!" color "#000"
                    #textbutton "Back" action Return("web_browser")
                    if not showCart:
                        frame ypos 20:
                            #xmaximum 810
                            ymaximum 450
                            background None
                            hbox:
                                frame:
                                    background "#fff"
                                    xmaximum 1200
                                    xminimum 1200
                                    ymaximum 450
                                    viewport id "tarzanVp":
                                        mousewheel True
                                        vbox:
                                            for item in range(len(tarzanStore)):
                                                frame:
                                                    background "#ccc"
                                                    vbox:
                                                        hbox:
                                                            text tarzanStore[item].name
                                                            null width 20 
                                                            text str(tarzanStore[item].price)
                                                        hbox:
                                                            add tarzanStore[item].pic
                                                            
                                                            null width 80
                                                            textbutton "Add to cart" action Return(("tarzanAdd", item)) ypos 80

                                                null height 3
                                vbar value YScrollValue("tarzanVp")
                        textbutton "My Cart" action SetVariable("showCart", True)

                    else:
                        frame ypos 20:
                            #xmaximum 810
                            ymaximum 450
                            background None
                            hbox:
                                frame:
                                    background "#fff"
                                    xmaximum 1200
                                    xminimum 1200
                                    ymaximum 450
                                    viewport id "tarzanCartVp":
                                        mousewheel True
                                        vbox:
                                            for item in range(len(tarzanCart)):
                                                frame:
                                                    background "#ccc"
                                                    vbox:
                                                        hbox:
                                                            text tarzanCart[item].name
                                                            null width 20 
                                                            text str(tarzanCart[item].price)
                                                        hbox:
                                                            null width 80
                                                            textbutton "Remove from cart" action Return(("tarzanRemove", item))

                                                null height 3
                                vbar value YScrollValue("tarzanCartVp")
                        hbox:
                            textbutton "Hide Cart" action SetVariable("showCart", False)
                            null width 50
                            textbutton "Check Out" action Return("tarzanBuy")
            else:
                frame:
                    xmaximum 1200
                    xminimum 1200
                    ymaximum 450
                    vbox:
                        text "Official Notice" style "stdTxt"
                        null height 10
                        text "This website has been taken down as part of an investigation into several claims of credit card fraud against the owners. If you feel you may have fallen victim to this scheme, please contact us right away." style "stdTxt"
                        null height 30
                        textbutton "Return" action Return("web_browser")

#################
###    StalkMePlz
# screen stalkMePlz:
    # use webBrowser
    # vbox:
        # xpos 0.01
        # ypos 0.2
        # text "Welcome to StalkMePlz!" style "stdTxt"
        # textbutton "Back" action Return("web_browser")


#########################
###    LemmingSoft Forums
screen lsf(showOptions=True):
    use webBrowser
    add "Assets/gui/lsf_back.png" #xpos 29 ypos 111
    if showOptions:
        vbox:
            xpos 0.4
            ypos 0.4
            #xpos 0.01
            #ypos 0.2
            #text "LemmingSoft Forums"
            textbutton "Visit Recruitment Forum" action Return("lsf_recruitment") size_group "lsf"
            $msgLen = len(messages)
            textbutton "Messages ([msgLen] New)" action Return("lsf_messages") size_group "lsf"
            #textbutton "Back" action Return("web_browser") size_group "lsf"
        
            # if len(messages) == 0:
                # text "No new messages" style "stdTxt"
            # else:
                # $msgLen = len(messages)
                # text "[msgLen] New Messages" style "stdTxt"
                # $del msgLen

####################################
###    LemmingSoft Recruitment Page
screen lsf_recruitment:
    use webBrowser
                                        #Working Back button ???
    frame:
        xpos 28#28 #75
        ypos 110 #125
#        xanchor 0.0
#        yanchor 0.0
#        xsize 1150
        ymaximum 580
        background None
        hbox:
            frame:
                xmaximum 1150
                xminimum 1150
                ymaximum 580
                background None
                viewport id "lsfThreads":
                        mousewheel True
                        vbox:
                            $threadCount = 0
                            add "Assets/gui/LSF_threads_head.png"
                            for item in threads:
                                frame:
                                    background "#fff"
                                    xsize 1150
                                    vbox:
                                        hbox:
                                            add "Assets/gui/lsf_unread.png"
                                            
                                            window:
                                                ysize 39
                                                background Frame("Assets/gui/lsf_title_frame.png", 2, 2, 2, 2)
                                        text "[item.title]" style "stdTxt" color "006597" size 18 xpos 61 ypos -30
                                        text "[item.user]" style "stdTxt" xpos 961 size 14 ypos -40
                                        text "[item.description]" style "stdTxt" ypos -30

                                        imagebutton auto "Assets/gui/lsf_pm_%s.png" focus_mask True action Return(("replyThread", threadCount))
                                            #textbutton "PM" action Return(("replyThread", threadCount))
                                        $threadCount += 1
                                null height 3
            null width 10
            vbar value YScrollValue("lsfThreads")
    textbutton "Back" action Return("lsf") ypos 640 xpos 1100
    
#################################
###    LemmingSofe Messages Page

screen lsf_messages:
    
    use webBrowser
    add "Assets/gui/lsf_messages_top.png"
    window:
        background Frame("Assets/gui/lsf_messages_bg.png", 2, 1, 2, 1)
        xpos 0#
        ypos 135
        xanchor 0.0
        yanchor 0.0
        ymaximum 500
        yminimum 500
        viewport id "lsfMessages":
            mousewheel True
            vbox:
                $msgCounter = 0
                for item in messages: 
                        window:
                            xpos 52
                            xanchor 0.0
                            xsize 1246
                            ysize 123
                            background "Assets/gui/lsf_messages_post.png"
                        text "[item.user]" style "stdTxt" size 14 xpos 80 ypos -80 #ypos 50
                        if item.stage == "reminder":
                            text "[item.reminder]" style "stdTxt" size 18 xpos 330 xsize 900 ypos -110
                            imagebutton auto "Assets/gui/lsf_reply_%s.png" focus_mask True action Return(("msgReply", msgCounter)) xpos 1126 ypos -81#turn in work if it is done
                        elif item.stage == "response":
                            text "[item.response]" style "stdTxt" size 18 xpos 330 xsize 900 ypos -110
                        imagebutton auto "Assets/gui/lsf_delete_%s.png" focus_mask True action Return(("msgDelete", msgCounter)) xpos 1012 ypos -100 #delete a messege 
                        $msgCounter += 1
                        
        vbar value YScrollValue("lsfMessages") xpos 1250
    
    add "Assets/gui/lsf_messages_bottom.png" ypos 640
    textbutton "Back" action Return("lsf") ypos 640 xpos 1100
                        
                        
    #lsf_messages_post
    
#    vbox:
        # if len(messages) == 0:
            # frame:
                # xpos 75
                # ypos 125
                # ymaximum 450
                # background None
                
                # vbox:
                    # text "Messages:" style "stdTxt"
                    # hbox:
                        # null width 5
                        # text "No new messages." style "stdTxt"
        # else:
            # frame:
                # xpos 75
                # ypos 125
                # ymaximum 450
                # background None
                # vbox:
                    # hbox:
                        # frame:
                            # background "#fff"
                            # xmaximum 1200
                            # xminimum 1200
                            # ymaximum 450
                            # viewport id "lsfMessages":
                                # mousewheel True
                                # vbox:
                                    # $msgCounter = 0
                                    
                                    
                                    
                                    # for item in messages:
                                        # frame:
                                            # background "#ccc"
                                            # vbox:
                                                # text "User: [item.user]" style "stdTxt"
                                                # if item.stage == "reminder":
                                                    # text "[item.reminder]" style "stdTxt"
                                                    # hbox:
                                                        # textbutton "Reply" action Return(("msgReply", msgCounter))#turn in work if it is done
                                                        # null width 5
                                                        # textbutton "Delete" action Return(("msgDelete", msgCounter)) #delete a messege 

                                                # elif item.stage == "response":
                                                    # text "[item.response]" style "stdTxt"
                                                    # hbox:
                                                        # textbutton "Reply"
                                                        # null width 5
                                                        # textbutton "Delete" action Return(("msgDelete", msgCounter)) # delete message
                                                # $msgCounter += 1
                                        # null height 3
                        # vbar value YScrollValue("lsfMessages")
                    # textbutton "Back" action Return("lsf")


############################
## Computer Images 
init:
    image computer = "Assets/gui/desk_bg1.jpg"

############################
# Window Frame - Used to show a winodows/mac style window manager simulation

screen window_frame(appname, icon, exitaction=None, width=1266, height=648):
    zorder 10
    
    if game_os == "win":
        $ full_width = width + 34
        $ full_height = height + 52
        $ exit_button_xpos = full_width - 70
        window:
            background Frame("Assets/gui/frame_win.png", 20, 40, 110, 20)
            xanchor 0.0
            yanchor 0.0
            xpos 10
            ypos 10
            
            xminimum full_width
            yminimum full_height
            xmaximum full_width
            ymaximum full_height
            add icon xpos 20 ypos 10
            text appname xpos 40 ypos 10 color "#000" size 16
            imagebutton auto "Assets/gui/close_win_%s.png" focus_mask True action [exitaction] xpos exit_button_xpos ypos 2            
    elif game_os == "mac":
        $ full_width = width + 20
        $ full_height = height + 66

        window:
            background Frame("Assets/gui/frame_mac.png", 70, 39, 15, 24)
            xanchor 0.0
            yanchor 0.0
            xpos 18
            ypos 8
            
            xminimum full_width
            yminimum full_height
            xmaximum full_width
            ymaximum full_height
            
            # xminimum 1286
            # xmaximum 1286
            # yminimum 714
            # ymaximum 714
            

            #add icon ypos 12
            $ icon_pos = full_width - 40
            add icon ypos 12 xpos icon_pos
            text appname xpos 20 ypos 12 color "#000" size 16 text_align 0.5 min_width full_width
            imagebutton auto "Assets/gui/close_mac_%s.png" focus_mask True action [exitaction] xpos 7 ypos 11

###################
# Computer Styles
init:
    style stdTxt is text:
        color "#000"
