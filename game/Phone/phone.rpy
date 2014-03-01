init python: # For setting up the variables before they need to be used.
    photos = [] # Used for the camera
    photo_sv = 0 #number of photos
    currently_viewed_picture = 1 # This is used in the picture viewing app, to keep track of which photo is being viewed.
    phone_screen_bg = "phone/phone_screen_blank.png"
    pong_oponent=0
    pong_player=0
    
image phone_background_v:
    "phone/phone_bg.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150
image phone_button_idle_v:
    "phone/phone_button_idle.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150
image phone_button_hover_v:
    "phone/phone_button_hover.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150
    
image photo_view_bg:
    "phone/photo_view_bg.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150
image photo_view_back:
    "phone/photo_view_back.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150
image photo_view_forward:
    "phone/photo_view_forward.png"
    xanchor 0.5
    yanchor 0.5
    rotate -90.0
    xanchor 0.0
    yanchor 0.0
    xpos 0
    ypos -150

    
    
    
# screen phone_button:
    # vbox align (.65,.04):
        # imagebutton:
            # idle "phone/phone smallest.png"
            # hover "phone/phone smaller.png"
            # action [Hide("phone_button"), Show ("mainphonescreen")]

screen phone_button:
    #vbox align (.04,.04):
        imagebutton:
            align (.04,.04)
            focus_mask True
            idle "phone/phone_icon.png"
            hover "phone/phone_icon.png"
            action [Hide("phone_button"), Show ("mainphonescreen")]
        $ Clocks (55, 45, 11)
            
screen mainphonescreen:
    tag phone
    modal True
    add phone_screen_bg
    add "phone/phone_bg.png"
    
    add "phone/phone_icons_bg.png"
    $ Clocks(130, 113)
    frame:
        background None
#        area (23, 133, 261, 368)
        area (18, 133, 261, 368)
        style_group "phone"
        grid 4 4:
            vbox ypos 15:
                imagebutton idle "phone/icons/camera.png" hover "phone/icons/camera.png" focus_mask True action ui.callsinnewcontext("take_a_photo") xalign .5
                text "Camera"
            vbox ypos 15:
                imagebutton idle "phone/icons/clock.png" hover "phone/icons/clock.png" focus_mask True action [Hide("mainphonescreen"), Show("clock")] xalign .5
                text "Clock"
            vbox ypos 15:
                imagebutton idle "phone/icons/web.png" hover "phone/icons/web.png" focus_mask True xalign .5
                text "Web"
            vbox ypos 15:
                imagebutton idle "phone/icons/pong.png" hover "phone/icons/pong.png" focus_mask True action ui.callsinnewcontext("pong") xalign .5
                text "Pong"


            vbox ypos 30:
                imagebutton idle "phone/icons/map.png" hover "phone/icons/map.png" focus_mask True xalign .5
                text "Maps"
            vbox ypos 30:
                imagebutton idle "phone/icons/ipod.png" hover "phone/icons/ipod.png" focus_mask True action ShowMenu("phone_sound_options") xalign .5
                text "iPod"
            vbox ypos 30:
                if photo_sv>0:
                    imagebutton idle "phone/icons/photos.png" hover "phone/icons/photos.png" focus_mask True action [Hide("mainphonescreen"), Show("view_photos")] xalign .5
                    text "Photos"
                else:
                    null
            null

            vbox ypos 50:
                imagebutton idle "phone/icons/save.png" hover "phone/icons/save.png" focus_mask True action [Hide("mainphonescreen"), Show("phone_button"), ShowMenu('save')] xalign .5
                text "Save"
            vbox ypos 50:
                imagebutton idle "phone/icons/skip.png" hover "phone/icons/skip.png" focus_mask True action [Hide("mainphonescreen"), Show("phone_button"), Skip()] xalign .5
                text "Skip"            
            vbox ypos 50:
                imagebutton idle "phone/icons/auto.png" hover "phone/icons/auto.png" focus_mask True action [Hide("mainphonescreen"), Show("phone_button"), Preference("auto-forward", "toggle")] xalign .5
                text "Auto"
            vbox ypos 50:
                imagebutton idle "phone/icons/settings.png" hover "phone/icons/settings.png" focus_mask True action [Hide("mainphonescreen"), Show("phone_button"), ShowMenu("preferences")] xalign .5
                text "Settings"

            vbox ypos 69:
                imagebutton idle "phone/icons/phone.png" hover "phone/icons/phone.png" focus_mask True action ui.callsinnewcontext("phone_call") xalign .5
                text "Phone" outlines [(2, "50626b", 0, 0)]
            vbox ypos 69:
                imagebutton idle "phone/icons/text.png" hover "phone/icons/text.png" focus_mask True xalign .5
                text "Text" outlines [(2, "50626b", 0, 0)]
                
            vbox ypos 69:
                imagebutton idle "phone/icons/notes.png" hover "phone/icons/notes.png" focus_mask True  xalign .5
                text "Notes" outlines [(2, "50626b", 0, 0)]
            vbox ypos 69:
                imagebutton idle "phone/icons/calendar.png" hover "phone/icons/calendar.png" focus_mask True xalign .5
                text "Calendar" outlines [(2, "50626b", 0, 0)]

    imagebutton idle "phone/phone_button_idle.png" hover "phone/phone_button_hover.png" focus_mask True action [Play ("sound", "sfx/click.wav"), Hide("mainphonescreen"), Show("phone_button")]
    add "phone/phone_reflection.png"

init -1 python:
    style.phone_text.size = 14
    style.phone_text.color = "bccacc"
    style.phone_text.xalign = .5
    style.phone_vbox.xalign =.5
        
screen blank_phone_screen:
    tag phone
    modal True
    add phone_screen_bg
    add "phone/phone_bg.png"
    
    imagebutton idle "phone/phone_button_idle.png" hover "phone/phone_button_hover.png" focus_mask True action [Play ("sound", "sfx/click.wav"), Hide("phone_sound_options"),Hide("calendar"),Hide("clock"),SetVariable("clock", False),Show("mainphonescreen")]    
    add "phone/phone_reflection.png"
    #add "phone/300x400 phone no icons.png"
    #imagebutton pos(127, 492) idle "phone/back_button.png" hover "phone/back_button.png" action [Play ("sound", "sfx/click.wav"), Hide("phone_sound_options"),Hide("calendar"),Hide("clock"),SetVariable("clock", False),Show("mainphonescreen")]
    
    
screen phone_sound_options:
    #tag phone
    use blank_phone_screen
    side "c b r":
        area (28, 107, 284, 442)
        viewport id "vp":
            use sound_options

init python:
    import os, hashlib
    def camera_take_photo():
        newPhoto = renpy.invoke_in_new_context (_camera_take_photo)
        photos.append(newPhoto)
        return True
    def _camera_take_photo():
        #renpy.take_screenshot((960,540)) # 75% of screen size
        renpy.take_screenshot((640,360)) # 50% of screen size
        #renpy.take_screenshot((1280,720)) # Full screen
        #renpy.take_screenshot((677,380)) # Resized to fit the phone screen
        photo = renpy.game.interface.get_screenshot()
        #photoname = hashlib.md5(photo).hexdigest() # ORIGINAL
        photoname = str (playtrough) + '_' + str(photo_sv)
        photodir = config.basedir + "/game/photos/"
        if(os.path.isdir(photodir) == False):
            os.mkdir(photodir)
        f = open(photodir + photoname + ".png", "wb")
        f.write(photo)
        f.close()
        return photoname

label take_a_photo:    
    $ photo_sv += 1
    hide screen mainphonescreen
    with Pause(0.1)
    $ camera_take_photo()
    show screen mainphonescreen
    with Fade(0.1, 0.0, 0.5, color="#fff")
    return 

    
    
    
screen view_photos_back:
    #add "phone_background_v"
    add "photo_view_bg"
    # imagemap:
        # ground "phone/phoneforpictureviewing.png"
        # hover "phone/phoneforpictureviewingblurry.png"
        # hotspot (182, 420, 238, 73) clicked [ui.callsinnewcontext("view_previous_photo"), Show("view_photos")] # Left button
        # hotspot (618, 420, 238, 73) clicked [ui.callsinnewcontext("view_next_photo"), Show("view_photos")] # Right button
        # hotspot (861, 218, 107, 102) clicked [Hide("view_photos"), Show("mainphonescreen")] # Home button

    imagebutton idle "photo_view_back" hover "photo_view_back" focus_mask True action [ui.callsinnewcontext("view_previous_photo"), Show("view_photos")]
    imagebutton idle "photo_view_forward" hover "photo_view_forward" focus_mask True action [ui.callsinnewcontext("view_next_photo"), Show("view_photos")]

    
    imagebutton idle "phone_button_idle_v" hover "phone_button_hover_v" focus_mask True action [Play ("sound", "sfx/click.wav"), Hide("view_photos"), Show("mainphonescreen")]
            
            
screen view_photos:
    tag phone
    modal True
    add "photo_view_bg"
    if currently_viewed_picture > 1:
        #imagebutton idle "photo_view_back" hover "photo_view_back" focus_mask True action [ui.callsinnewcontext("view_previous_photo"), Show("view_photos")]
        imagebutton idle "photo_view_forward" hover "photo_view_forward" focus_mask True action [SetVariable("currently_viewed_picture", currently_viewed_picture-1), Show("view_photos")]
    if currently_viewed_picture < photo_sv:
        imagebutton idle "photo_view_back" hover "photo_view_back" focus_mask True action [SetVariable("currently_viewed_picture", currently_viewed_picture+1), Show("view_photos")]
#    imagebutton idle "photo_view_forward" hover "photo_view_forward" focus_mask True action [ui.callsinnewcontext("view_next_photo"), Show("view_photos")]


    side "c b r":
        area (153, 102, 370, 230)
        viewport:
            draggable True
            vbox:
                $ pic = "photos/" + str (playtrough) + '_' + str(currently_viewed_picture) + ".png"
                #$ pic="pho/"+str(currently_viewed_picture)+".png"
                add pic
                
    add "phone_background_v"
    imagebutton idle "phone_button_idle_v" hover "phone_button_hover_v" focus_mask True action [Play ("sound", "sfx/click.wav"), Hide("view_photos"), Show("mainphonescreen")]


# label view_previous_photo:
    # if currently_viewed_picture > 1:
        # $ currently_viewed_picture -= 1
    # return

# label view_next_photo:
    # if currently_viewed_picture < photo_sv:
        # $ currently_viewed_picture += 1
    # return    
      
screen phone_call:
    use blank_phone_screen
      
label phone_call:
    menu:
        "Call girlfriend":
            "You don't have one, you loser."
    return

    
screen calendar:
    use blank_phone_screen
    #side "c b r":
        # area (180, 38, 689, 383)
        # viewport:
    vbox:
        xpos 22
        ypos 100    
        $ Calendar()
        $ Clocks()

        
        
screen clock:
    tag phone
    modal True

    use blank_phone_screen
    frame:
        background None
        area (18, 133, 261, 368)
        $ Calendar(20,0, 20)
        #xpos .5
        #ypos .5
        #xpos 22
        #ypos 100    
        $ AClocks(y=.55)
        
        #$ clock = True
        

        
label pong:
    window hide None
    $ pong_oponent=0
    $ pong_player=0
    show bg pong field
    show phone_background_v
    show screen return_button
    $ win_score = 2
    python:        
        while pong_oponent<win_score+1 and pong_player<win_score+1:
            ui.add(PongDisplayable())
            winner = ui.interact(suppress_overlay=True, suppress_underlay=True)
            if winner == "oponent":
                pong_oponent+=1
            else:
                pong_player+=1
                
    return
        
screen return_button:
    imagebutton idle "phone_button_idle_v" hover "phone_button_hover_v" focus_mask True action [Play ("sound", "sfx/click.wav"), SetVariable("pong_oponent", 21), Return()]    
    
