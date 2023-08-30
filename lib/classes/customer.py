class Customer:
   
    all = []        
   
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if type(new_name) is str and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception('Name must be a string and between 1 and 15 characters long.')

    def orders(self):
        return [ order for order in Order.all if order.customer is self ]
    
    def coffees(self):
        return list ( set ( [ order.coffee for order in self.orders() ] ) )
    
    def create_order( self, coffee, price ):
        Order (
            customer = self,
            coffee = coffee,
            price = price
        )



from classes.coffee import Coffee
from classes.order import Order