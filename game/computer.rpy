
label computer:
    #show computer Desktop
    menu:
        "open browser":
            jump webBrowser            
        "turn off": 
            return #change to return to a specific screen 
    jump computer

label webBrowser:
     #show web browser start page
     menu:
        "LemmingSoft Forums":
            jump lsf
        "Amazon":
            jump amazon
        "Close Browser":
            jump computer


label lsf:
    #show lemmingSoft forums screen here
    menu:
      "Browse new posts":
          $pass #the poll the system for a list of stupid/random posts about random projects
      "Check Recruitment forum":
          $pass #poll for recruitment options and display
      "Back":
          jump webBrowser
    jump lsf

