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
        elif showMikie and type(showMikie) == bool:
            show computer michelangelo
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
            $poll()
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
        if _return[0] == "tarzanAdd":
            $tarzanCart.append(tarzanStore.pop(_return[1]))
        if _return[0] == "tarzanRemove":
            $tarzanStore.append(tarzanCart.pop(_return[1]))
        if _return == "tarzanBuy":
            $totalPrice = 0
            $item = 0
            while(item < len(tarzanCart)):
                  #add price to total
                  $totalPrice += tarzanCart[item]["price"]
                  
                  #check to see if this item is one of the unlockables
                  if tarzanCart[item]["name"] == "Keyboard":
                      $pass
                  #do elifs here for other items
                  $item += 1
            #subtract price from money
            #maybe do somthing with the stuff bought
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
                            call writingAnimation
                            "You spend some time practing writing."
                        else:
                            "You are the very best. Like no one ever was."
                    else:
                        "You are too sleepy to write."
                else:
                    if time.dec(dur):
                        $mygame.do_art(dur)
                        $completion = round(((mygame.art_done/mygame.art_needed)*100),2) 
                        call writingAnimation
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
                                                            text tarzanStore[item]["name"]
                                                            null width 20 
                                                            text str(tarzanStore[item]["price"])
                                                        hbox:
                                                            null 80
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
                                                            text tarzanCart[item]["name"]
                                                            null width 20 
                                                            text str(tarzanCart[item]["price"])
                                                        hbox:
                                                            null 80
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
        #todo: show an icon that indicates the number of messages the player has

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

label writingAnimation:
    "drawing animation"
    return
    
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

    python:
        #variables for tarzan
        showCart = False
        tarzanCart = []
        tarzanStore = []
        tarzanStore.append({"name": "Keyboard", "price" : 200})
        tarzanStore.append({"name": "Composing for Morons", "price": 10.00})
        tarzanStore.append({"name": "Writing for Retards", "price": 10.00})
        tarzanStore.append({"name": "Programming for Idiots", "price": 10.00})
        tarzanStore.append({"name": "Drawing for Losers", "price": 10.00})
        tarzanStore.append({"name": "Drawing Tablet", "price": 120.00})

