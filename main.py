
class Item:
    def __init__(self, name: str, price: float, quantity = 0):
    #Run Validations to Received Argument
        assert price >= 0, f"Price {price} is not greater or equals to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equals to zero!"
        
        # Assign to self Object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("IPhone", 1000, 5)
item2 = Item("Laptop", 10000, 7)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#----------------------------------------------    



class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity = 0):
    #Run Validations to Received Argument
        assert price >= 0, f"Price {price} is not greater or equals to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equals to zero!"
        
        # Assign to self Object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
#----------------------------------------------    

item1 = Item("IPhone", 1000, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 10000, 7)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

#----------------------------------------------    

        
from item import Item

item1 = Item("MyItem", 750)

#Setting an Attribute 
item1.name = "OtherItem"

#Getting an Attribute
print(item1.name)


#----------------------------------------------    

      
from item import Item

item1 = Item("MyItem", 750, 6)

item1.send_email()

     
#----------------------------------------------    
from phone import Phone

item1 = Phone("IPhone15", 1000, 3)

item1.apply_discount()

print(item1.price)
                   
#----------------------------------------------    


from keyboard import Keyboard
item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)