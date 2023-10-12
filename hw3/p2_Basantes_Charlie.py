# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:49:29 2020

@author: solid
"""

class Product:
    def __init__(self, name, mass, stock, price):
        self.name = name
        self.mass = mass
        self.stock = int(stock)
        self.price = float(price)
        
       
    def get_price(self):
        return self.price
    
    def __str__(self): #method to convert object of this class to string
        name_str = self.name
        price_str = self.price.__str__()
        mass_str = self.mass.__str__()
        stock_str = self.stock.__str__()
        return name_str +", $"+ price_str +", "+ mass_str +" kg, "+ stock_str +" in stock"
    
    def set_price(self, price):
        self.price = price
        return self.price
    

class DiscountedProduct: #parametrized constructor
    def __init__(self,disc,Product):
        self.disc=disc
        self.Product=Product
        
    def price(self): #getter method to get discounted price
        return self.Product.price-(self.disc*self.Product.price)
    
    
    def __str__(self): #method to convert object of this class to string
        discount = (self.disc*100).__str__()
        product_name = self.Product.name
        product_price = self.price().__str__()
        product_mass = self.Product.mass.__str__()
        in_stock = self.Product.stock.__str__()
        
        return "discounted "+ discount +"%: "+ product_name +", $"+ product_price +", "+ product_mass +" kg, "+ in_stock +" in stock"


def main():
    
    # create a product object for Lavalamps, priced at $100, 
    p = Product(name  = "Lavalamps", price = 30, mass = 1.0, stock = 1)
    print(p.set_price(100))
    #and with 123 of them in stock: p = Product(name="Lavalamp", price=30, mass=0.8, stock=123)   
    p = Product(name="LavaLamps", mass = 0.8, stock = 123, price = 30)
    print(p)  # prints "Lavalamp, $30, 0.8 kg, 123 in stock"
    
    # p.price() returns 30.0
    print(p.get_price())
    
    # create a discounted  product of p, with a 20% discount: 
    disc_p = DiscountedProduct(0.2, p)
    print(disc_p.price()) # prints "24" (24 == 30 - 20% * 30)
    
    print(disc_p)  # prints "discounted 20%: Lavalamp, $24, 0.8 kg, 123 in stock"
    # now, we change the product p: 
    p.set_price(20)
    
    print(p.get_price())   # prints "20"
    
    # the price change also affects the discounted product object that embeds p:
    print(disc_p)      # prints "discounted 20%: Lavalamp, $16, 0.8 kg, 123 in stock"
    
    # disc_p.price() returns 16 (16 == 20 - 20% * 20)
    print(disc_p.price())
    

if __name__ == '__main__':
    main() 