class Coffee: 

    all = []
    
    def __init__( self, name ):

        if type(name) is str:
            self._name = name
        else:
            raise Exception("name must be a string")
        Coffee.all.append(self)
        
    @property 
    def name (self):
        return self._name
    
    @name.setter
    def name ( self, new_name ):
        raise Exception( "Name can't be changed after creation" )

    def orders(self):
        return [ order for order in Order.all if order.coffee is self ]
    
    def customers(self):
        return list ( set ( [ order.customer for order in self.orders() ] ) )
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        from statistics import mean
        return round ( mean( [ order.price for order in self.orders() ] ), 2 ) 





from classes.order import Order
from classes.customer import Customer