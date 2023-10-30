<img src="./images/product-inventory.png" width="700"/>

# Product Inventory
> DIFFICULTY: **EASY**

Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

## TODO

1. Create an abstract class *Entity* for entities.
2. Create *Product* class that inherites from Entity class.  
Add some attibutes like: id, value, amount, scale of products.  
Define *repr* and *str* methods for it.
3. Create *Inventory* class that inherites from Entity class.  
Add some attirbutes like: id and products(a dictionary)  
Define product_add method to add new product to products attribute.  
Check the input is a single product or a list of products.
