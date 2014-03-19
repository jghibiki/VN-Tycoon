init -2 python:
    class Item:
        def __init__(self, name, price, pic="#FFF"):
            self.name = name
            self.price = price 
            self.pic = pic

    class Inventory:
        def __init__(self, money=0):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.price:
                self.money -= item.price
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount
            
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
