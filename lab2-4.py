class Binary:
    """
    Class, which create a binary tree and contains background data of product prices
    """
    def __init__(self, code, price):
        
        self.left = None
        self.right = None
        self.data = code
        self.price = price

    def insert(self, data, price):
        """
        Method, which insert data in binary tree
        Function received arguments data and price. If new data lower that previous data
        new data become a left leaf of binary tree, if higher - right leaf. Using 
        recursion, function find the correct place to put new data in the tree
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Binary(data, price)
                else:
                    self.left.insert(data, price)
            elif data > self.data:
                if self.right is None:
                    self.right = Binary(data, price)
                else:
                    self.right.insert(data, price)
        else:
            self.data = data

    def PrintTree(self):
        """
        Method, which print binary tree
        If left leafs exists, it prints them, same operation for right leafs
        """
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def get_value(self, data):
        """
        Method, which find code in binary tree
        Function receive new data and according to this data, process will start
        If new data lower than old data, it finds equals in left branch, in other case - in right branch
        In case of finding equal - function return data, if not - return message "Not Found"
        """
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
        """
        Method, whict returns instance arguments
        """
        return f'\nProduct: {self.name} \nProduct code: {self.code} \nPrice per 1: {self.price}' 
    
    
    def get_code(self):
        """
        Method, which returns code of instance
        """
        return self.code

    def get_price(self):
        """
        Method, which returns price of instance
        """
        return self.price
        

laptop = Product(12, 'laptop', 100)
phone = Product(15, 'phone', 150)
tv = Product(9, 'tv', 100)
satnav = Product(25, 'satnav', 150)



if __name__ == "__main__":
    root = Binary(laptop.get_code(), laptop.get_price())
    root.insert(phone.get_code(), phone.get_price())
    root.insert(satnav.get_code(), satnav.get_price())
    root.insert(tv.get_code(), tv.get_price())

    root.PrintTree()
    try:
        value = str(input('Enter product code and quantity with whitespace: ')).split(' ', 2)
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



