class Product:

    def __init__(self,product, price, description, **kwargs):
        self.product = product
        if not isinstance(price, (float, int)):
            raise TypeError("Incorrect price")
        
        self.price = price
        self.description = description
        self.kwargs = kwargs
    
    def get_value(self):
        return self.price

    def __str__(self):
        return "Product: " + self.product + "; Price: " + str(self.price) + "; Description: " + self.description +"; Dimension: "+ ','.join(list(map(str, list(self.kwargs.values()))))

class Customer:
    __slots__ = ("surname", "name", "patronymic", "mobile")
    
    def __init__(self, surname, name, patronymic, mobile):
        if not len(surname)==0 and  isinstance(surname, str):
            self.surname = surname
        else: raise ValueError("Empty field or incorrect")
        if not len(name)==0 and isinstance(name, str):
            self.name = name
        else: raise ValueError("Empty field or incorrect")
        if not len(patronymic)==0 and isinstance(patronymic, str):
            self.patronymic = patronymic
        else: raise ValueError("Empty field or incorrect")
        if not  len(mobile)==10:
            raise TypeError("Incorect mobile")
        self.mobile = mobile
    
    def __str__(self):
        return "\nSurname: "+self.surname +"; \nName: "+ self.name +"; \nPatronymic: "+ self.patronymic +"; \nMobile: "+ self.mobile

class Order():
    def __init__(self, customer = None, **kwargs):
        self.customer = customer
        self.kwargs = kwargs
        self.total = 0
  
    def totalvalue(self):
        for key in self.kwargs:
            self.total += self.kwargs[key].get_value()
        return f'\nTotal price: {self.total}'

    def customerdata(self):
        return self.customer

    def productdata(self):
        return f'\nOrder info:{list(map(str, list(self.kwargs.values())))}'


if __name__=='__main__':
    water = Product("Morshinska", 20, "water", width = 5,height =  10)
    bigwater = Product("big Morshinska", 40, "water", width = 10,height =  20)
    first_customer = Customer("Teleha", "Nikita", "Oleksiyovich","0677987872")
    first_order = Order(first_customer, first = water, second = bigwater, third = water)
    print(first_order.customerdata(),  first_order.totalvalue(), first_order.productdata())


    
