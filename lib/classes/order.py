
class Order:
    all=[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if type (new_price) is int and new_price in range(1,11):
            self._price = new_price
        else:
            raise Exception("Price must be a number between 1 and 10")

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if type(new_customer) is Customer:
            self._customer = new_customer
        else:
            raise TypeError("Customer must be of the Customer Class")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if type(new_coffee) is Coffee:
            self._coffee = new_coffee
        else:
            raise TypeError("Coffee must be of the Coffee Class")
    



from classes.customer import Customer
from classes.coffee import Coffee