
# The game starts here.
label start:
    call screen char_select
    call screen set_attributes(_return)

    python:
        inventory = Inventory()
        tablet = Item("Tablet", 299)
        #rest of the item definitions here (including software)
    
        time=Time(24)
        
        
        day=1
        if not persistent.playtrough:
            persistent.playtrough = 1
        else:
            persistent.playtrough += 1
        playtrough = persistent.playtrough
        

    scene black
    
    show screen phone_button
#    show screen inventory_button

   
    if _return=="artist":
        $job = "artist"
        jump artist
    if _return=="writer":
        $job = "writer"
        jump writer
    if _return=="coder":
        $job = "coder"
        jump programmer
    if _return=="composer":
        $job = "composer"
        jump composer        


    "You've created a new Ren'Py game."
    "Once you add a story, pictures, and music, you can release it to the world!"

    return
