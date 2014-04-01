init python:
    class Sale:
        def __init__(self, game, day=day, minutes=minutes):
            self.name = game.title
            self.price = game.price
            self.minutes = minutes
            self.day = day
            #self.date = "1.1.2014"
            
    class Sales:
        def __init__(self):
            self.earnings = []
        def sell(self, game, day=day, minutes=minutes):
            sale = Sale(game, day, minutes)
            self.earnings.append(sale)
            inventory.earn(sale.price)
    sales=Sales()
        
init -1:
    $ game_tmp = None

label edit_price:
    $ price = round(game_tmp.price, 2)
    call screen edit_price(game_tmp.price)
    python:
        try:
            game_tmp.price = float(_return)
        except ValueError:
            pass
    return
    
screen edit_price(game_price=""):
    add "#000"
    window:
        has vbox
        text "Enter a new price:"
        input default game_price allow "0123456789."

screen bmt_mezzo:
    use computer
    use webBrowser
    add "Assets/gui/sales.png"
    hbox:
        xpos 995
        ypos 123
        textbutton "Games List" action Show("game_list") style "link_button"
        text " | " size 14 color "000"
        textbutton "Sales Report" action Show("sales") style "link_button"
        text " | " size 14 color "000"
        textbutton "Logout" action Return("web_browser") style "link_button"
    
    
init:
    style link:
        size 14
        #font "Assets/gui/labtop_secundo_superwide.ttf"
        color "#0000ff"
        
    style link_button:
        background None
        xmargin 0
        #ymargin 0
        xpadding 0
        ypadding 0
        
        ysize 10
        #ymaximum 10
        
    style link_button_text is link:
        #selected_color "#fff"
        #selected_background "#78a5c5"
        #hover_color "#0000ff"
        hover_underline True
    
screen sales:
    tag app
    use bmt_mezzo
    
    $ y = len(sales.earnings)+2
    window:
        xmaximum 1266
        xminimum 1266
        ymaximum 508
        yminimum 508
        ypos 187
        yanchor 0.0
        xpos 28
        xanchor 0.0
        
        add "#ededed"
        window:
            right_margin 55
            viewport id "vp":
                mousewheel True
                grid 4 y:
                    spacing 10
                    null
                    text "item name"
                    text "date"
                    text "price"
                    
                    $ total = 0
                    for sale in sales.earnings:
                        null
                        text sale.name

                        $ date = "Day " + str(sale.day) + " " + str(sale.minutes / 60) + ":" + str(sale.minutes % 60)
                        text date
                        $ price = "$" + str(round(sale.price, 2))
                        text price
                        $ total += sale.price
                        
                        
                    text "Total:"
                    null
                    null
                    $ total = "$" + str(round(total, 2))
                    text total
                    
        vbar value YScrollValue("vp") style "v_bar" xalign 1.0
        textbutton "Return" ypos 700 action Return("web_browser")

screen game_list:
    tag app
    use bmt_mezzo
    
    $ num_games = len(games)
    
    window:
        xmaximum 1266
        xminimum 1266
        ymaximum 508
        yminimum 508
        ypos 187
        yanchor 0.0
        xpos 28
        xanchor 0.0
        background None
        add "#ededed"
        window:
            background None
            right_margin 55
            viewport id "vp":
                mousewheel True
                draggable True
                grid 5 num_games:
                    for g in games:
                        window xmaximum 262 ymaximum 143:
                            add g.bg:
                                zoom 0.2
                            add g.sp1 xalign 0.1:
                                zoom 0.2
                            if g.sp2:
                                add g.sp2 xalign 0.7:
                                    zoom 0.2
                        $ relationship = g.relationship
                        if not relationship=="none":
                            $ relationship = relationship[0].upper() + relationship[1] + relationship[2].upper()
                        $ mytext = g.title + "\n" + g.genre.title() + ", " + relationship
                        text mytext size 12 color "000" text_align 0.5 xalign 0.5 yalign 0.5 
                        $ price = str(round(g.price, 2))
                        $ price1 = " $" + price
                        if not g.commercial:
                            $ price1 = "Free"
                            $ price1 += " / " + str(g.downloads) + " downloads"
                        else:
                            $ price1 += " / " + str(g.sales) + " sales"
#                        vbox:
                        text price1 xalign 0.5 size 14 color "000" yalign 0.5 
#                            if not g.commercial:
#                                text "[g.downloads] downloads"
                            #else:
                                #text g.sales
                                
                        #text g.genre
                        if g.commercial:
                            textbutton "Change Price" action [SetVariable("game_tmp", g), ui.callsinnewcontext("edit_price")] style "link_button" yalign 0.5 
                        else:
                            null
                        textbutton "View Cover" action Show("show_cover", game=g) style "link_button" yalign 0.5 
                        #text g.relationship

                        
                        
        vbar value YScrollValue("vp") style "v_bar" xalign 1.0
        textbutton "Return" ypos 700 action Return("web_browser")
    
init:
    style v_bar:
        thumb "Assets/gui/vbar_thumb.png"
        ymaximum 768
        xmaximum 50
        top_bar "Assets/gui/vbar.png"
        bottom_bar "Assets/gui/vbar.png"
        thumb_shadow None
        thumb_offset 2
        bar_vertical True
        bar_invert True