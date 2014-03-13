
# The game starts here.
label start:
    
    python:
        mygame=Game()
        games=[]
        skills = Skills()
        sales = Sales()
        userNames = []
    
    call screen char_select
    posts_list = make_posts_list()
    python:
        cclass = _return
        art_min = 0
        writing_min = 0
        coding_min = 0
        music_min = 0
        if cclass=="artist":
            art_min = 6
            skills.art += art_min
        if cclass=="writer":
            writing_min = 6
            skills.writing += writing_min
        if cclass=="coder":
            coding_min = 6
            skills.coding += coding_min
        if cclass=="composer":
            music_min = 6
            skills.music += music_min
    call screen set_attributes(cclass)

    python:
        inventory = Inventory()
        tablet = Item("Tablet", 299)
        #rest of the item definitions here (including software)
    
        time=Time(24)
        day=1
        
        #last_day = day
        last_time = minutes
        
        if not persistent.playtrough:
            persistent.playtrough = 1
        else:
            persistent.playtrough += 1
        playtrough = persistent.playtrough
        
        artist_event2 = False
        artist_event3 = False
        
    scene black
    
    #show screen phone_button
#    show screen inventory_button

    $ job = cclass
    if cclass=="artist":
        #$job = "artist"
        #jump artist_event1
        #jump artist_event2
        jump test
    if cclass=="writer":
        #$job = "writer"
        jump writer
    if cclass=="coder":
        #$job = "coder"
        jump coder
    if cclass=="composer":
        #$job = "composer"
        jump composer        
    

    "You shouldn't be seeing this text."
    "Something went wrong. :("

    return
