init python:
    class Sale:
        def __init__(self, game):
            self.name = game.title
            self.price = game.price
            #self.date = ...
            #self.price = "12.34"
            self.date = "1.1.2014"
            
    class Sales:
        def __init__(self):
            self.earnings = []
        def sell(self, game):
            sale = Sale(game)
            self.earnings.append(sale)
        
    sales=Sales()
        
screen sales:
    add "#000"
    $ y = len(sales.earnings)+2
    grid 4 y:
        spacing 10
        null
        text "item name"
        text "date"
        text "price"
        for sale in sales.earnings:
            null
            text sale.name
            text sale.date
            text sale.price
    
        text "Total:"
        null
        null
        text "$0.00"
    textbutton "Return" ypos 700 action Return()

screen game_list (page=1):
    $ num_games = len(games)
    $ pages =  num_games / 4
    add "#000"
    vbox:
        text "Your games:"
        viewport id "vp":
            mousewheel True
            draggable True
            grid 7 num_games:
                for g in games:                        
                            window xmaximum 262 ymaximum 143:
                                add g.bg:
                                    zoom 0.2
                                add g.sp1 xalign 0.1:
                                    zoom 0.2
                                if g.sp2:
                                    add g.sp2 xalign 0.7:
                                        zoom 0.2
                            text g.title
                            $ price = str(0.0)# str(g.price)
                            $ price1 = " $" + price
                            text price1
                            text g.genre
                            textbutton "Cover" action Show("show_cover", game=g)                
                            text g.relationship
                            textbutton "Change" action Jump("change_price")
                            
            vbar value YScrollValue("vp")


    textbutton "Return" ypos 700 action Return()
    
label change_price:
    $ price = "0.0"
    $ price = renpy.input("New price?", price, length=6)
    
    
    