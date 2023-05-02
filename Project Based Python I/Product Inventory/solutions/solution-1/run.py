# Source Link Code
# https://github.com/Drhealsgood/miniprojects/tree/master/class_projects/product_inventory

from abc import *

class Entity(metaclass=ABCMeta):
    
    @abstractproperty
    def id_number(self):
        return 0

class Product(Entity):

    id = 0


    def __init__(self, name=None, value=0, amount=0, scale='kg'):
        '''
        Constructor
        '''
        self._id    = Product.id
        Product.id  = Product.id + 1
        if not name:
            self._name = "{0}_{1}".format(self.__class__, self._id)
        else:
            self._name = name
        self._value = value
        self._amount = amount 
        self._scale = scale
    
    @property
    def id_number(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,other):
        self._amount = other
        
    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, other):
        self._scale = other
        
    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)
    
    def __str__(self):
        return "{amount}{scale} of {name} valued at {value}".format(
                amount=self._amount,scale=self._scale,name=self._name,
                value=self._value
                                                                    )
    
class Inventory(Entity):
    
    id  = 0
    
    def __init__(self):
        self._id        = Inventory.id
        Inventory.id    = Inventory.id + 1
        self._products  = {}
        
    def product_add(self, *args):
        
        def add_to_products(prod):
            try:
                self._products[prod.name].append(prod)
            except:
                self._products[prod.name] = [prod]
                
        for arg in args:
            if isinstance(arg, tuple) or isinstance(arg,list):
                for prod in arg:
                    add_to_products(prod)
            elif isinstance(arg,Product):
                add_to_products(arg)
            # if it's not a product it won't get added
    
    @property
    def product_value(self):
        """
        @return: int: total value of product on hand
        """
        return sum([single.value for product in self._products for single in self._products[product]])
    
    @property
    def product_count(self):
        """
        @return: int: amt of product on hand
        """
        return len([p for product in self._products for p in self._products[product]])
    
    @property
    def product_diff_amount(self):
        """
        @return: int: the amount of different products on hand
        """
        return len(self._products)

    @property
    def products(self):
        """
        @return: list(Product): product on hand
        """
        return self._products
        
    @property
    def id_number(self):
        """
        @return:  int: identity number of product
        """
        return self._id
    
    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)
    
class ObjFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_object(self):
        return 0
    
    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__name__, self._id)
    
class InventoryFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Inventory()

class ProductFactory(ObjFactory):
    
    def get_object(self, amt=1):
        for i in range(amt):
            yield Product()
            
if __name__ == "__main__":
    """
    Product Inventory Project – Create an application which manages an inventory of products. 
    Create a product class which has a price, id, and quantity on hand. 
    Then create an inventory class which keeps track of various products and can sum up the inventory value.
    """
    # create an inventory
    inventory   = Inventory()
    # add some products to the inventory
    genProd = lambda value: Product(value=value)
    for i in range(1,10):
        inventory.product_add(genProd(value=i))
    for i in range(1,5):
        inventory.product_add(genProd(value=i))
    # Get amount of product on hand, value of product, and amt of differnet product
    prod_amt    = inventory.product_count
    prod_val    = inventory.product_value
    prod_diff   = inventory.product_diff_amount
    for name, info in (("amount of product",prod_amt), ("value of product",prod_val), ("different products",prod_diff)):
        print("{0}: {1}".format(name,info))
    print(inventory.products)
    for product in inventory.products:
        print(product + " prob details: " + str(inventory.products[product]))