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
        
screen sales:
    $ y = len(sales.earnings)+2
    add "#000"
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
                    $ price = str(sale.price)
                    text price
                    $ total += sale.price
                    
                text "Total:"
                null
                null
                $ total = "$" + str(total)
                text total
            
    vbar value YScrollValue("vp") style "v_bar" xalign 1.0
    textbutton "Return" ypos 700 action Return()

screen game_list:
    $ num_games = len(games)
    add "#000"
    window:
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
                    text mytext
                    $ price = str(round(g.price, 2))
                    $ price1 = " $" + price
                    if not g.commercial:
                        $ price1 = "Free"
                    text price1 xalign 0.5
                    #text g.genre
                    if g.commercial:
                        textbutton "Change Price" action Jump("change_price")
                    else:
                        null
                    textbutton "View Cover" action Show("show_cover", game=g)                
                    #text g.relationship
                    

        
    vbar value YScrollValue("vp") style "v_bar" xalign 1.0

    textbutton "Return" ypos 700 action Return()
    
label change_price:
    scene black
    $ price = "0.0"
    $ price = renpy.input("New price?", price, length=6)
    jump sim

    
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