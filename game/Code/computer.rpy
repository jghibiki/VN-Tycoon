
label computer:
    python:
        computerLoop = True
        showDesktop = True
        showBrowser = False
    while(computerLoop):
        #show screens
        if showDesktop:
            show computer
            call screen computer
        elif showBrowser and type(showBrowser) == bool:
            show computer browser
            call screen webBrowser
        elif showBrowser == "lsf":
            show computer browser lsf
            call screen lsf
        elif showBrowser == "amazon":
            show computer browser amazon
            call screen amazon


        #parse returns
        if _return == "web_browser":
            $showDesktop = False
            $showBrowser = True
        if _return == "leave":
            return # or maybe jump to sim instead


#######################
## Computer Screens

screen computer:
    #if we end up using different bgs based on the job change this
    vbox: 
        xpos 0.5
        ypos 0.5
        text "computer desktop!"
        textbutton "Open Web Browser" action Return("web_browser")
        textbutton "Leave Computer" action Return("leave") 




screen webBrowser:
    vbox:
        text "web browser"

screen amazon:
    vbox:
        text "Amazon!"

screen lsf:
    vbox:
        text "LemmingSoft Forums"

############################3
## Computer Images
init:
    image computer = "#CF6800"
    image computer browser = "#B2FB69"
    image computer browser amazon = "#C8CF00"
    image computer browser lsf = "#CF0026"
