
# The game starts here.
label start:
    $ mygame=Game()
    $ games=[]
    $ skills = Skills()
    
    call screen char_select
    $ cclass = _return
    $ art_min = 0
    $ writing_min = 0
    $ coding_min = 0
    $ composing_min = 0
    if cclass=="artist":
        $ art_min = 5
        $ skills.art += art_min
    if cclass=="writer":
        $ writing_min = 5
        $ skills.writing += writing_min
    if cclass=="coder":
        $ coding_min = 5
        $ skills.coding += coding_min
    if cclass=="composer":
        $ composing_min = 5
        $ skills.composing += composing_min
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

   
    if cclass=="artist":
        $job = "artist"
        jump artist
    if cclass=="writer":
        $job = "writer"
        jump writer
    if cclass=="coder":
        $job = "coder"
        jump programmer
    if cclass=="composer":
        $job = "composer"
        jump composer        
   

    "You should be seeing this text."
    "Something went wrong. :("

    return
