label computer:
    python:
        computerLoop = True
        showDesktop = True
        showBrowser = False
        showSentence = False
        showMikie = False
        selTime = False
    while(computerLoop):
        #show screens
        if showDesktop:
            show computer
            call screen computer
        elif showBrowser and type(showBrowser) == bool:
            show computer browser
            call screen webBrowser
        elif showBrowser == "lsf":
            #poll the message genereator to see if there are any new messages
            show computer browser lsf
            call screen lsf
        elif showBrowser == "tarzan":
            show computer browser tarzan
            call screen tarzan
        elif showBrowser == "lsf_recruitment":
            show computer browser lsf recruitment
            call screen lsf_recruitment
        elif showBrowser == "lsf_messages":
            show computer browser lsf messages
            call screen lsf_messages
        elif showBrowser == "stalkmeplz":
            show computer browser stalkMePlz
            call screen stalkMePlz
        elif showSentence and type(showSentence) == bool:
            show computer sentence
            call screen sentence
            if not _return:
                $selTime = False
                call screen mikie
        elif showMikie and type(showMikie) == bool:
            show computer michelangelo
            call screen mikie
            if not _return:
                $selTime = False
                call screen mikie

        #parse returns
        if _return == "web_browser":
            $showDesktop = False
            $showBrowser = True
        if _return == "leave":
            return # or maybe jump to sim instead
        if _return == "lsf":
            $pollMessages()
            $showBrowser = "lsf"
        if _return == "tarzan":
            $showBrowser = "tarzan"
        if _return == "lsf_recruitment":
            $pollThreads()
            $showBrowser = "lsf_recruitment"
        if _return == "lsf_messages":
            $showBrowser = "lsf_messages"
        if _return == "stalkmeplz":
            $showBrowser = "stalkmeplz"
        if _return == "desktop":
            $showDesktop = True
            $showBrowser = False
            $showSentence = False
            $showMikie = False
        if _return == "open_sentence":
            $showDesktop = False
            $showSentence = True
        if _return == "open_mikie":
            $showMikie = True
            $showDesktop = False
        if type(_return) == tuple:
            if _return[0] == "tarzanAdd":
                $tarzanCart.append(tarzanStore.pop(_return[1]))
            if _return[0] == "tarzanRemove":
                $tarzanStore.append(tarzanCart.pop(_return[1]))
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
                                "You have purcased a keyboard, Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy a keyboard."
                                $rejects.append(item)
                        else:
                            "You already own this item!"
                  elif tarzanCart[item] == book_c:
                        if not inventory.has_item(book_c):
                            if inventory.buy(book_c):
                                "You have purcased \"Composing for Morons\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Composing for Morons\". Moron. Get a job and try again."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_w:
                        if not inventory.has_item(book_w):
                            if inventory.buy(book_w):
                                "You have purcased \"Writing for the Asinine\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Writing for the Asinine\". Shows how much of an {b}ASS{/b}inine fool you are."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_p:
                        if not inventory.has_item(book_p):
                            if inventory.buy(book_p):
                                "You have purcased \"Programming for Idiots\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Programming for Idiots\". Come on! Only idiots read books to learn to program. I mean, \"Hello!?\", the internet was invented, what 60+ years ago?."
                                $rejects.append(item)
                  elif tarzanCart[item] == book_d:
                        if not inventory.has_item(book_d):
                            if inventory.buy(book_d):
                                "You have purcased \"Drawing for Losers\", Tazan Droid will air lift it you you shortly."
                            else:
                                "You don't have enough money to buy this \"Drawing for Losers\". There is only one type of person that would try to buy a book they couldn't affort. A {i}LOSER{/i}."
                                $rejects.append(item)

                  elif tarzanCart[item] == tablet:
                        if not inventory.has_item(tablet):
                            if inventory.buy(tablet):
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
        if _return[0] == "select_time":
            $selTime = _return[1]
        if _return[0] == "a" or _return[0] == "p":
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
                else:
                    if time.dec(dur):
                        $mygame.do_art(dur)
                        $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                        call drawingAnimation
                        "You draw some sprites for your game.
                        [completion]\% Completed"
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
                else:
                    if time.dec(dur):
                        $mygame.do_writing(dur)
                        $completion = round(((mygame.writing_done/mygame.writing_needed)*100),2) 
                        call screen writingAnimation
                        "You write a few scenes for your game.
                        [completion]\% Completed"
                    else:
                        "You are too sleepy to draw."

                                         
#######################
## Computer Screens

screen computer:
    #if we end up using different bgs based on the job change this
    vbox: 
        xpos 0.01
        ypos 0.2
        textbutton "Open Web Browser" action Return("web_browser")
        textbutton "Open Sentence Word-processor" action Return("open_sentence")
        textbutton "Open Michelangelo" action Return("open_mikie")
        textbutton "Leave Computer" action Return("leave") 


#############################
## Word Processor (Sentence)
screen sentence:
    use window_frame("Sentence", Return("desktop"))
    vbox:
        xpos 0.01
        ypos 0.2
        if not selTime:
            text "Welcome to Word-processor Sentence!"
            textbutton "Write!" action Return(("select_time", "write"))
            textbutton "Exit program" action Return("desktop")
        else:
            use select_time


############################################
## Drawing/Painting Software (Michelangelo)
screen mikie:
    vbox:
        xpos 0.01
        ypos 0.2
        if not selTime:
            text "Welcome to Michelangelo!"
            textbutton "Draw!" action Return(("select_time", "draw"))
            textbutton "Exit program" action Return("desktop")
        else:
            use select_time
            
########################
## Web Browser Screens
screen webBrowser:
    use window_frame("Icewolf", Return("desktop"))
        
    vbox:
        xpos 0.01
        ypos 0.2
        textbutton "LemmingSoft Forums" action Return("lsf")
        textbutton "Tarzan" action Return("tarzan")
        textbutton "Exit Browser" action Return("desktop")

screen tarzan:
    vbox:
        xpos 0.01
        ypos 0.2
        hbox:
            if len(tarzanStore) != 0 or len(tarzanCart) != 0:
                vbox:
                    text "Tarzan!"
                    textbutton "Back" action Return("web_browser")
                    if not showCart:
                        frame:
                            xmaximum 810
                            ymaximum 300
                            background None
                            hbox:
                                frame:
                                    background "#fff"
                                    xmaximum 800
                                    ymaximum 300
                                    viewport id "tarzanVp":
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
                                                            null width 80
                                                            textbutton "Add to cart" action Return(("tarzanAdd", item))

                                                null height 3
                                vbar value YScrollValue("tarzanVp")
                        textbutton "My Cart" action SetVariable("showCart", True)

                    else:
                        frame:
                            xmaximum 810
                            ymaximum 300
                            background None
                            hbox:
                                frame:
                                    background "#fff"
                                    xmaximum 800
                                    ymaximum 300
                                    viewport id "tarzanCartVp":
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
                    text "Official Notice" 
                    null height 10
                    text "This website has been taken down as part of an investigation into several claims of credit card fraud against the owners. If you feel you may have fallen victim to this scheme, please contact us right away."
                    null height 30
                    textbutton "Return" action Return("web_browser")
screen stalkMePlz:
    vbox:
        xpos 0.01
        ypos 0.2
        text "Welcome to StalkMePlz!"
        #show messages here
        textbutton "Back" action Return("web_browser")

screen lsf:
    vbox:
        xpos 0.01
        ypos 0.2
        text "LemmingSoft Forums"
        textbutton "Visit Recruitment Forum" action Return("lsf_recruitment")
        textbutton "Messages" action Return("lsf_messages")
        textbutton "Back" action Return("web_browser")
    
        if len(messages) == 0:
            text "No new messages"
        else:
            $msgLen = len(messages)
            text "[msgLen] New Messages"
            $del msgLen

screen lsf_recruitment:
    vbox:
        xpos 0.01
        ypos 0.2
        text"Recruitment Forum"
        textbutton "Back" action Return("lsf")
        #todo: show randomly generated recruitment adds/offers here.

screen lsf_messages:
    hbox:
        xpos 0.01
        ypos 0.2
        vbox:
            text "Messages"
            textbutton "Back" action Return("lsf")
        vbox:
            #change this to update the list of available messages appropriately
            text "No new messages."


################################
## Computer screen animations
label drawingAnimation:
    "drawing animation"
    return

screen writingAnimation:
    $ mytext = random.choice(writing_snippets)
    $ typeSpeed = 20 + int(skills.writing*6)
    $ wait_to_hide = 1 + len(mytext) / typeSpeed
    use window_frame("Sentence", Return("desktop"))
    use autoPost(28, 84, 0, 0, "#00000000", mytext, typeSpeed = typeSpeed, moveCursor=False, textSize=24)
    timer wait_to_hide action [Hide("writingAnimation"), Return()]

############################3
## Computer Images
init:
    image computer = "#CF6800"
    image computer browser = "#B2FB69"
    image computer browser tarzan = "#C8CF00"
    image computer browser lsf = "#CF0026"
    image computer browser lsf recruitment = "#F86CA2"
    image computer browser lsf messages = "#6CF8C2" 
    image computer sentence = "#7D001B"
    image computer michelangelo = "#007D0F"
    image computer stalkMePlz = "#fff"


screen window_frame(appname, exitaction):
    if game_os == "win":
        window:
            background Frame("Assets/gui/frame_win.png", 20, 40, 110, 20)
            xalign 0.1
            yalign 0.1
            xminimum 1300
            yminimum 700
            text appname xpos 20 ypos 10 color "#000" size 16
            imagebutton auto "Assets/gui/close_win_%s.png" focus_mask True action [exitaction] xpos 1295 ypos 2            
    elif game_os == "mac":
        window:
            background Frame("Assets/gui/frame_mac.png", 70, 39, 15, 24)
            xalign 0.1
            yalign 0.1
            xminimum 1300
            yminimum 700
            text appname ypos 12 color "#000" size 16 text_align 0.5 min_width 1300
            imagebutton auto "Assets/gui/close_mac_%s.png" focus_mask True action [exitaction] xpos 7 ypos 11
