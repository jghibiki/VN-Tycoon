init -1 python:
    #item defines, so they can be used in screens:
    tablet = None
    keyboard = None
    book_c = None
    book_w = None
    book_p = None
    book_d = None
    repBonus = 0

# The game starts here.
label start:
    
    python:
        mygame=Game()
        comishWork = ComishWork()
        games=[]
        skills = Skills()
        sales = Sales()
        userNames = []
        repBonus = 0.04

    call screen char_select
    $ renpy.block_rollback()
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
    $ renpy.block_rollback()
    python:
        inventory = Inventory()
        tablet = Item("Drawing Tablet", 199.00, "Assets/gui/shop_tablet.png")
        keyboard = Item("Keyboard", 299.00, "Assets/gui/shop_keyboard.png")
        book_c = Item("Composing for Morons", 35.00, "Assets/gui/shop_book.png")
        book_w = Item("Writing for the Asinine", 35.00, "Assets/gui/shop_book.png")
        book_p = Item("Programming for Idiots",35.00, "Assets/gui/shop_book.png")
        book_d = Item("Drawing for Losers", 35.00, "Assets/gui/shop_book.png")
        
        #variables for tarzan
        showCart = False
        tarzanCart = []
        tarzanStore = []
        tarzanStore.append(keyboard)
        tarzanStore.append(book_c)
        tarzanStore.append(book_w)
        tarzanStore.append(book_p)
        tarzanStore.append(book_d)
        tarzanStore.append(tablet)

        #the initial poll for the message board threads
        pollThreads()
    
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
        
        artist_event2, artist_event3, artist_event4, artist_event5, artist_event6, artist_event7, artist_event8, artist_event9, artist_event10 = False, False, False, False, False, False, False, False, False

        writer_event2, writer_event3, writer_event4, writer_event5, writer_event6, writer_event7, writer_event8, writer_event9, writer_event10 = False, False, False, False, False, False, False, False, False
        
        coder_event2, coder_event3, coder_event4, coder_event5, coder_event6, coder_event7, coder_event8, coder_event9, coder_event10 = False, False, False, False, False, False, False, False, False
        
        
    scene black
    
    
    
    
    
    #show screen phone_button
#    show screen inventory_button


    
    $ game_os = "win"
    $ job = cclass
    
    
    
    $ posts_list = make_posts_list()
    
    
    if cclass=="artist":
        jump artist_event1
        #jump artist_event2
        #jump test
    if cclass=="writer":
        jump writer_event1
    if cclass=="coder":
        $ game_os = "mac"
        jump coder_event1
    if cclass=="composer":
        $ game_os = "mac"
        jump composer        
    

    "You shouldn't be seeing this text."
    "Something went wrong. :("

    return
