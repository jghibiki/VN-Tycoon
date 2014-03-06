
label computer:
    python:
        computerLoop = True
        showDesktop = True
        showBrowser = False
        showSentence = False
        showMikie = False
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
        elif showBrowser == "amazon":
            show computer browser amazon
            call screen amazon
        elif showBrowser == "lsf_recruitment":
            show computer browser lsf recruitment
            call screen lsf_recruitment
        elif showBrowser == "lsf_messages":
            show computer browser lsf messages
            call screen lsf_messages
        elif showSentence and type(showSentence) == bool:
            show computer sentence
            call screen sentence
        elif showMikie and type(showMikie) == bool:
            show computer michelangelo
            call screen michelangelo

        #parse returns
        if _return == "web_browser":
            $showDesktop = False
            $showBrowser = True
        if _return == "leave":
            return # or maybe jump to sim instead
        if _return == "lsf":
            $showBrowser = "lsf"
        if _return == "amazon":
            $showBrowser = "amazon"
        if _return == "lsf_recruitment":
            $showBrowser = "lsf_recruitment"
        if _return == "lsf_messages":
            $showBrowser = "lsf_messages"
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
        text "Welcome to Word-processor Sentence!"
        textbutton "Exit program" action Return("desktop")

############################################
## Drawing/Painting Software (Michelangelo)
screen michelangelo:
    vbox:
        xpos 0.01
        ypos 0.2
        text "Welcome to Michelangelo!"
        textbutton "Exit program" action Return("desktop")


########################
## Web Browser Screens
screen webBrowser:
    vbox:
        xpos 0.01
        ypos 0.2
        textbutton "LemmingSoft Forums" action Return("lsf")
        textbutton "Amazon" action Return("amazon")
        textbutton "Exit Browser" action Return("desktop")

screen amazon:
    vbox:
        xpos 0.01
        ypos 0.2
        text "Amazon!"
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



############################3
## Computer Images
init:
    image computer = "#CF6800"
    image computer browser = "#B2FB69"
    image computer browser amazon = "#C8CF00"
    image computer browser lsf = "#CF0026"
    image computer browser lsf recruitment = "#F86CA2"
    image computer browser lsf messages = "#6CF8C2" 
    image computer sentence = "#7D001B"
    image computer michelangelo = "#007D0F"
