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

screen game_list:
    add "#000"
    vbox:
        text "Your games:"
        for g in games:
        
            hbox:
                text g.title
                $ price = str(g.price)
                $ price1 = "$" + price
                text price1
                #textbutton "Change" action Jump("change_price")
    
    textbutton "Return" ypos 700 action Return()
    
label change_price:
    $ price = "0.0"
    $ price = renpy.input("New price?", price, length=6)
    
    
    