#function to resize the characters:
init python:
    class ProportionalScale(im.ImageBase): # A mix between im.Scale and im.FactorScale for character images
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = im.image(imgname)
            super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = int(maxwidth)
            self.maxheight = int(maxheight)
            self.bilinear = bilinear

        def load(self):
            child = im.cache.get(self.image)
            currentwidth, currentheight = child.get_size()
            xscale = 1.0
            yscale = 1.0
            if (currentwidth > self.maxwidth):
                xscale = float(self.maxwidth) / float(currentwidth)
            if (currentheight > self.maxheight):
                yscale = float(self.maxheight) / float(currentheight)
            if (xscale < yscale):
                minscale = xscale
            else:
                minscale = yscale
            newwidth = currentwidth * minscale
            newheight = currentheight * minscale
            #renpy.log("Loading image %s from %f x %f to %f x %f" % (self.imgname, currentwidth , currentheight , newwidth, newheight)) # Debug code to see when the loading really happens
            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv
        def predict_files(self):
            return self.image.predict_files()

init +1 python:
    mr = MusicRoom(fadeout=1.0)
    for song in song_list:
        mr.add(song["name"], always_unlocked=True)

        
screen music_room_phone:
    tag phone
    modal True
    window:
        background None
        xalign 0.99
        xsize 307
        use blank_phone_screen
        side "c b r":
            area (28, 107, 284, 442)
            viewport id "vp":
                frame background None xpos 250 ypos 150:
                    has vbox spacing 15
                    for song in song_list:
                        textbutton song["title"] action mr.Play(song["name"]) style "henpie"
        on "replace" action mr.Play()
        on "replaced" action Play("music", config.main_menu_music)

    
screen music_room:
    tag menu
    use extras
    add "music_room_title" xpos 152 ypos 22
    frame background None xpos 250 ypos 150:
        has vbox spacing 15
        for song in song_list:
            textbutton song["title"] action mr.Play(song["name"])
    on "replace" action mr.Play()
    on "replaced" action Play("music", config.main_menu_music)
    
    
#Galleries:
init python:
    #Galleries settings - start
    
    #list the CG gallery images here:
    gallery_cg_items = []
    #gallery_cg_items = ["angeldead"]
    #list the BG gallery images here:
    gallery_bg_items = []
    #gallery_bg_items = ["work", "library"]
    
    # list one image for each sprite (neutral) here:
    gallery_ch_items = []
    #gallery_ch_items = ["woman neutral"]
    
    
    #list the images for the rest of expressions for each sprite here:
    gallery_woman = ["woman happy blush", "woman happy talk blush", "woman happy talk", "woman happy", "woman huff blush", "woman huff", "woman serious blush", "woman serious", "woman shock", ]
    

    gallery_dev_items = []
    
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150
    gal_xpos = 50
    gal_ypos = 120
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_dev = Gallery()
    for gal_item in gallery_dev_items:
        g_dev.button(gal_item + " butt")
        g_dev.image("#000", gal_item)
        #g_dev.unlock(gal_item)
        
    g_dev.transition = fade
    dev_page=0
    
    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        
        #BGs with variations:
        if gal_item == "home day":
            g_bg.image( "home night")
            g_bg.unlock("home night")
    g_bg.transition = fade
    bg_page=0
    
    g_ch = Gallery()
    for gal_item in gallery_ch_items:
        g_ch.button(gal_item + " butt")
        if gal_item=="woman neutral":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item)
            for item in gallery_woman:
                g_ch.image("#000", item)
                g_ch.unlock(item)

        # if gal_item=="angel laughing":
            # g_ch.image("#000", gal_item)
            # g_ch.unlock(gal_item)
            # for item in gallery_angel:
                # g_ch.image("#000", item)
                # g_ch.unlock(item)
                
    g_ch.transition = fade
    ch_page=0

init:
    $ border_size=6
    image gal_bg=LiveComposite((thumbnail_x, thumbnail_y), (0,0), Solid("dadada"))    
    image gal_frame_x=LiveComposite((thumbnail_x, border_size), (0,0), Solid("CECECE"))
    image gal_frame_y=LiveComposite((border_size, thumbnail_y-border_size*2), (0,0), Solid("CECECE"))
    image gal_frame_x_sel=LiveComposite((thumbnail_x, border_size), (0,0), Solid("4abff2"))
    image gal_frame_y_sel=LiveComposite((border_size, thumbnail_y-border_size*2), (0,0), Solid("4abff2"))
    
init +1:
    image gal_locked=LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (42,50), Text("Locked", style="title"))
    
    image gal_frame=LiveComposite((thumbnail_x, thumbnail_y), (border_size*2,1), ImageReference("gal_frame_x"), (border_size*2,thumbnail_y-border_size+1), ImageReference("gal_frame_x"), (border_size*2,border_size+1), ImageReference("gal_frame_y"), (thumbnail_x+border_size,border_size+1), ImageReference("gal_frame_y"))

    image gal_frame_sel=LiveComposite((thumbnail_x, thumbnail_y), (border_size*2,1), ImageReference("gal_frame_x_sel"), (border_size*2,thumbnail_y-border_size+1), ImageReference("gal_frame_x_sel"), (border_size*2,border_size+1), ImageReference("gal_frame_y_sel"), (thumbnail_x+border_size,border_size+1), ImageReference("gal_frame_y_sel"))
    
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_dev_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_ch_items:
        renpy.image (gal_item + " butt", LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (int(thumbnail_x/4),0), ProportionalScale(ImageReference(gal_item), thumbnail_x, thumbnail_y)))

screen cg_gallery:
    tag menu
    use extras
    add "cg_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1            
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
                    
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]
    
screen bg_gallery:
    tag menu
    use extras
    add "bg_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:                
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
                    #add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]

screen ch_gallery:
    tag menu
    use extras
    add "character_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_ch_page = ch_page + 1
            if next_ch_page > int(len(gallery_ch_items)/gal_cells):
                $ next_ch_page = 0
            for gal_item in gallery_ch_items:
                $ i += 1
                if i <= (ch_page+1)*gal_cells and i>ch_page*gal_cells:
                    add g_ch.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
            for j in range(i, (ch_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_ch_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('ch_page', next_ch_page), ShowMenu("ch_gallery")]

screen dev_gallery:
    tag menu
    use extras
    add "concept_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_dev_page = dev_page + 1            
            if next_dev_page > int(len(gallery_dev_items)/gal_cells):
                $ next_dev_page = 0
            for gal_item in gallery_dev_items:
                $ i += 1
                if i <= (dev_page+1)*gal_cells and i>dev_page*gal_cells:
                    add g_dev.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
            for j in range(i, (dev_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_dev_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('dev_page', next_dev_page), ShowMenu("dev_gallery")]

            