# Import modules

class Entity(ABC):
    # Abstract class for entities
    pass

#-----------------------------------------------------------
class Product(Entity):
    # Define Product class
    # Add some attibutes like: id, value, amount, scale of products.
    # Define __repr__ and __str__ for class
    pass
                                                                
#---------------------------------------------------------------    
class Inventory(Entity):
    # Define Inventory class
    # Add some attirbutes like: id and products(a dictionary)
    pass
    
    def product_add(self, *args):
        # Add new product to products
        # If args contains tupe/list of products you have to add one by one
        pass
    
#-----------------------------------------------------    
class ObjFactory(ABC):
    # Abctract class for factory
    pass

#-------------------------------------------   
class InventoryFactory(ObjFactory):
    pass

class ProductFactory(ObjFactory):
    pass

