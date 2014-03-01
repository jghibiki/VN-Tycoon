image room="gui/main_bg.jpg"

label sim:
    scene room
    menu:
        "go to work":
            #$ inventory.work()
            $ salary = max(art, writing, coding, composing)
            if time.dec(4):
                $ inventory.earn(salary)
                "Work, work, work... You earned $[salary]."
            else:
                "You are too sleepy to work."
        "turn on the computer":
            call computer
        "draw":
            if time.dec(1):
                "You spend some time practicing drawing."
                $ art += 1
            else:
                "You are too sleepy to draw."
        "sleep":
            $ day += 1
            $ time = Time(24)
            
    jump sim

label computer:
    #show computer Desktop
    menu:
        "open browser":
            label webBrowser            
        "turn off": 
            return #change to return to a specific screen 
    jump computer

labek webBrowser:
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

