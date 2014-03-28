
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
        elif showBrowser == "stalkmeplz":
            #show computer browser stalkMePlz
            call screen stalkMePlz
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
            
        if type(_return) == tuple:
            if _return[0] == "tarzanAdd":
                $tarzanCart.append(tarzanStore.pop(_return[1]))
            if _return[0] == "tarzanRemove":
                $tarzanStore.append(tarzanCart.pop(_return[1]))
            if _return[0] == "replyThread":
                $messages.append(threads.pop(_return[1]))
            if _return[0] == "msgReply":
                #first gather work 
                $turnedIn = False
                if messages[_return[1]].input == "money":
                    if inventory.money >= messages[_return[1]].inputQuantity:
                        $inventory.money -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        "You don't have enough money yet! (Must have $[messages[_return[1]].inputQuantity])."
                elif messages[_return[1]].input == "art":
                    if comishWork.art >= messages[_return[1]].inputQuantity:
                        $comishWork.art -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        "You don't have enough art to turn in! (Must have [messages[_return[1]].inputQuantity])"
                elif messages[_return[1]].input == "coding":
                    if comishWork.coding >= messages[_return[1]].inputQuantity:
                        $comishWork.coding -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                    else:
                        "You don't have enough code written to turn in! (Must have [messages[_return[1]].inputQuantity])"
                elif messages[_return[1]].input == "music":
                    if comishWork.music >= messages[_return[1]].inputQuantity:
                        $comishWork.music -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                elif messages[_return[1]].input == "writing":
                    if comishWork.writing >= messages[_return[1]].inputQuantity:
                        $comishWork.writing -= messages[_return[1]].inputQuantity
                        $turnedIn = True
                #then provide reward
                if turnedIn:
                    $messages[_return[1]].stage = "response"
                    if messages[_return[1]].output == "money":
                        $inventory.money += messages[_return[1]].outputQuantity
                    elif messages[_return[1]].output == "art":
                        $mygame.art_done += messages[_return[1]].outputQuantity
                    elif messages[_return[1]].output == "coding":
                        $mygame.coding_done += messages[_return[1]].outputQuantity
                    elif messages[_return[1]].output == "music":
                        $mygame.music_done += messages[_return[1]].outputQuantity
                    elif messages[_return[1]].output == "writing":
                        $mygame.writing_done += messages[_return[1]].outputQuantity
                    ###
                    $ repBonus += .01
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
                
        if type(_return) == type(''): #string
            if _return[0] == "a" or _return[0] == "p" or _return[0] == "w":
                $selTime = None
                if showMikie:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("art", dur):
                                call drawingAnimation
                                "You spend some time practing drawing."
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to draw."
                    elif _return[0] == "w":
                        if time.dec(dur):
                            if comishWork.increase("art", dur):
                                call drawingAnimation
                                "You spend some time working on comissions."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to draw."
                    else:
                        if time.dec(dur):
                            $mygame.do_art(dur)
                            $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                            call drawingAnimation
                            "You draw some sprites for your game. [completion]\% Completed"
                        else:
                            "You are too sleepy to draw."
                elif showSentence:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("writing", dur):
                                call screen writingAnimation
                                "You spend some time practing writing."
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to write."

                    elif _return[0] == "w":
                        if time.dec(dur):
                            if comishWork.increase("writing", dur):
                                call screen writingAnimation
                                "You spend some time working on comissions."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to write."
                    else: 
                        if time.dec(dur):
                            $mygame.do_writing(dur)
                            $completion = round(((mygame.writing_done/mygame.writing_needed)*100),2) 
                            call screen writingAnimation
                            "You write a few scenes for your game. [completion]\% Completed"
                        else:
                            "You are too sleepy to write."

                elif showNotepad:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("coding", dur):
                            
                                show screen computer
                                $ speed = 40 + skills.coding * 2
                                $ post = random.choice(code_snippets_fixed1)
                                show screen window_frame("Notepad--", "icon16_notepad", None)
                                show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
                                $ post = random.choice(code_snippets_typed1)
                                call screen autoPost(82, 300, 0, 0, "#00000000", post, typeSpeed=speed, moveCursor=False, textSize=15)
                                hide screen autoPostFixed
                                hide screen window_frame
                                hide screen computer


                                
                                "You spend some time practing coding."
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to code."
                    elif _return[0] == "w":
                        if time.dec(dur):
                            if comishWork.increase("coding", dur):

                                show screen computer
                                $ speed = 40 + skills.coding * 2
                                $ post = random.choice(code_snippets_fixed1)
                                show screen window_frame("Notepad--", "icon16_notepad", None)
                                show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
                                $ post = random.choice(code_snippets_typed1)
                                call screen autoPost(82, 300, 0, 0, "#00000000", post, typeSpeed=speed, moveCursor=False, textSize=15)
                                hide screen autoPostFixed
                                hide screen window_frame
                                hide screen computer

                                "You spend some time working on comissions."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to code."
                    else:
                        if time.dec(dur):
                            $mygame.do_coding(dur)
                            $completion = round(((mygame.coding_done/mygame.coding_needed)*100),2) 
                            
                            show screen computer
                            $ speed = 40 + skills.coding * 2
                            $ post = random.choice(code_snippets_fixed1)
                            show screen window_frame("Notepad--", "icon16_notepad", None)
                            show screen autoPostFixed(82, 122, "Assets/gui/notepad.png", post, textSize=15)
                            $ post = random.choice(code_snippets_typed1)
                            call screen autoPost(82, 300, 0, 0, "#00000000", post, typeSpeed=speed, moveCursor=False, textSize=15)
                            hide screen autoPostFixed
                            hide screen window_frame
                            hide screen computer


                                                          
                            "You code a few scenes for your game. [completion]\% Completed"
                        else:
                            "You are too sleepy to code."
                elif showGrunge:
                    $dur = int(_return[1])
                    if _return[0] == "p":
                        if time.dec(dur):
                            if skills.increase("music", dur):
                                #call screen composingAnimation
                                "You spend some time practing composing music."
                            else:
                                "You are the very best. Like no one ever was."
                        else:
                            "You are too sleepy to compose."
                    elif _return[0] == "w":
                        if time.dec(dur):
                            if comishWork.increase("music", dur):
                                #call composingAnimation
                                "You spend some time working on comissions."
                            else:
                                "You should really turn in your work already."
                        else:
                            "You are too sleepy to compose."
                    else:
                        if time.dec(dur):
                            $mygame.do_music(dur)
                            $completion = round(((mygame.music_done/mygame.music_needed)*100),2) 
                            #call screen composingAnimation
                            "You make some music for your game.
                            [completion]\% Completed"
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
        imagebutton idle "icon32_michelangelo_idle" hover "icon32_michelangelo_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 1.0 
        $ x += 60
        imagebutton idle "icon32_notepad_idle" hover "icon32_notepad_hover" action [Hide("gui_tooltip"), Return("open_notepad")] xpos x yanchor 1.0 ypos 1.0 
        
        $ x += 60
        imagebutton idle "icon32_grunge_band_idle" hover "icon32_grunge_band_hover" action [Hide("gui_tooltip"), Return("open_grunge")] xpos x yanchor 1.0 ypos 1.0 

        $ x += 60
        imagebutton idle "icon32_henpie_idle" hover "icon32_henpie_hover" action [Hide("gui_tooltip"), Return("game_progress")] xpos x yanchor 1.0 ypos 1.0

        $ x += 60
        imagebutton idle "icon32_player_idle" hover "icon32_player_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 1.0 
        
        $ x += 60
        
        
        
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
        $ x += 80
        imagebutton idle "icon64_michelangelo_idle" hover "icon64_michelangelo_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 764 
        
        $ x += 80
        imagebutton idle "icon64_notepad_idle" hover "icon64_notepad_hover" action [Hide("gui_tooltip"), Return("open_notepad")] xpos x yanchor 1.0 ypos 764 
        
        $ x += 80
        imagebutton idle "icon64_grunge_band_idle" hover "icon64_grunge_band_hover" action [Hide("gui_tooltip"), Return("open_grunge")] xpos x yanchor 1.0 ypos 764
        
        $ x += 80
        imagebutton idle "icon64_henpie_idle" hover "icon64_henpie_hover" action [Hide("gui_tooltip"), Return("game_progress")] xpos x yanchor 1.0 ypos 764 
        
        $ x += 80
        imagebutton idle "icon64_player_idle" hover "icon64_player_hover" action [Hide("gui_tooltip"), Return("open_mikie")] xpos x yanchor 1.0 ypos 764 
        
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
    if showBrowser == "lsf":
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
            textbutton "Visit Recruitment Forum" action Return("lsf_recruitment")
            textbutton "Messages" action Return("lsf_messages")
            textbutton "Back" action Return("web_browser")
        
            if len(messages) == 0:
                text "No new messages" style "stdTxt"
            else:
                $msgLen = len(messages)
                text "[msgLen] New Messages" style "stdTxt"
                $del msgLen

####################################
###    LemmingSoft Recruitment Page
screen lsf_recruitment:
    use webBrowser
                                        #Working Back button ???
    vbox:
        xpos 1
        ypos 1
        frame:
            xpos 75
            ypos 125
            ymaximum 450
            background None
            hbox:
                frame:
                    background "#fff"
                    xmaximum 1000
                    xminimum 1000
                    ymaximum 450
                    viewport id "lsfThreads":
                        mousewheel True
                        vbox:
                            $threadCount = 0
                            for item in threads:
                                frame:
                                    background "#ccc"
                                    xmaximum 1000
                                    xminimum 1000
                                    vbox:
                                        hbox:
                                            #make this line a different color than the main post
                                            text "Post Title: XXXXXXX" style "stdTxt"
                                            null width 20
                                            text "[item.user]" style "stdTxt"

                                        hbox:
                                            text "[item.description]" style "stdTxt"
                                        hbox:
                                            textbutton "PM" action Return(("replyThread", threadCount))
                                        $threadCount += 1
                                null height 3
                null width 10
                vbar value YScrollValue("lsfThreads")

#################################
###    LemmingSofe Messages Page

screen lsf_messages:
    use webBrowser
    
    vbox:
        if len(messages) == 0:
            frame:
                xpos 75
                ypos 125
                ymaximum 450
                background None
                
                vbox:
                    text "Messages:" style "stdTxt"
                    hbox:
                        null width 5
                        text "No new messages." style "stdTxt"
        else:
            frame:
                xpos 75
                ypos 125
                ymaximum 450
                background None
                vbox:
                    hbox:
                        frame:
                            background "#fff"
                            xmaximum 1200
                            xminimum 1200
                            ymaximum 450
                            viewport id "lsfMessages":
                                mousewheel True
                                vbox:
                                    $msgCounter = 0
                                    for item in messages:
                                        frame:
                                            background "#ccc"
                                            vbox:
                                                text "User: [item.user]" style "stdTxt"
                                                if item.stage == "reminder":
                                                    text "[item.reminder]" style "stdTxt"
                                                    hbox:
                                                        textbutton "Reply" action Return(("msgReply", msgCounter))#turn in work if it is done
                                                        null width 5
                                                        textbutton "Delete" action Return(("msgDelete", msgCounter)) #delete a messege 

                                                elif item.stage == "response":
                                                    text "[item.response]" style "stdTxt"
                                                    hbox:
                                                        textbutton "Reply"
                                                        null width 5
                                                        textbutton "Delete" action Return(("msgDelete", msgCounter)) # delete message
                                                $msgCounter += 1
                                        null height 3
                        vbar value YScrollValue("lsfMessages")
                    textbutton "Back" action Return("lsf")


################################
## Computer screen animations
label drawingAnimation:
    "drawing animation"
    return

screen writingAnimation:
    text "writing animation"
    $ wait_to_hide = 1
    
    # $ mytext = random.choice(writing_snippets)
    # $ typeSpeed = 20 + int(skills.writing*6)
    # $ wait_to_hide = 1 + len(mytext) / typeSpeed
    # use window_frame("Sentence", "icon16_sentence", Return("desktop"))
    # use autoPost(28, 84, 0, 0, "#00000000", mytext, typeSpeed = typeSpeed, moveCursor=False, textSize=24)
    timer wait_to_hide action [Hide("writingAnimation"), Return()]

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

