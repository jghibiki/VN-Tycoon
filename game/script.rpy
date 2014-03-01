
# The game starts here.
label start:
    call screen char_select
    $ cclass = _return
    $ art_min = 0
    $ writing_min = 0
    $ coding_min = 0
    $ composing_min = 0
    if cclass=="artist":
        $ art_min = 5
        $ art += art_min
    if cclass=="writer":
        $ writing_min = 5
        $ writing += writing_min
    if cclass=="coder":
        $ coding_min = 5
        $ coding += coding_min
    if cclass=="composer":
        $ composing_min = 5
        $ composing += composing_min
    call screen set_attributes(cclass)

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
