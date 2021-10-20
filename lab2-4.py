"""
Create a class BINARY TREE that contains background information of product prices 
(product code, price of 1 product). The tree is sorted by product codes. From the keyboard enter 
data on the number of products in the format: product code, 
number of products. Using a tree, find the cost of products (cost = quantity * price of one product).
"""
class Node:
    def __init__(self, code, price):
        
        self.left = None
        self.right = None
        self.data = code
        self.price = price

#code i price - dict


    def insert(self, data, price):
    
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, price)
                else:
                    self.left.insert(data, price)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, price)
                else:
                    self.right.insert(data, price)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def get_value(self, data):
        if data < self.data:

            if self.left is None:
                return str(data)+" Not Found"
            else:
                return self.left.get_value(data)
        elif data > self.data:
            if self.right is None:
                return str(data)+" Not Found"
            else:
                return self.right.get_value(data)
        else:
            return self.price

class Product:
    def __init__(self,code, name,  price):
        
        self.code = code
        self.name = name
        self.price = price

    def __str__(self):
        return f'\nProduct: {self.name} \nProduct code: {self.code} \nPrice per 1: {self.price}' 
    
    
    def get_code(self):
        return self.code

    def get_price(self):
        return self.price
        

laptop = Product(12, 'laptop', 100)
phone = Product(15, 'phone', 150)
tv = Product(9, 'tv', 100)
satnav = Product(25, 'satnav', 150)



if __name__ == "__main__":
    root = Node(laptop.get_code(), laptop.get_price())
    root.insert(phone.get_code(), phone.get_price())
    root.insert(satnav.get_code(), satnav.get_price())
    root.insert(tv.get_code(), tv.get_price())
    
    root.PrintTree()
    try:
        value = str(input('Enter product code and quantity ')).split(' ', 2)
        code = int(value[0])
        quantity = int(value[1])
        data = root.get_value(code)
        if type(data) == int:
            print(data*quantity)
        else:
            print(data)
    except ValueError:
        print("Incorrect data...")
        exit(1)



