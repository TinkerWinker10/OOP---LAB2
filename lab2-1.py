class Product:

    def __init__(self,product, price, description, **kwargs):
        self.product = product
        if not isinstance(price, (float, int)):
            raise TypeError("Incorrect price")
        else: 
            self.price = price
        self.description = description
        self.kwargs = kwargs
    
    def get_value(self):
        return self.price

    def __str__(self):
        return "Product: " + self.product + "; Price: " + str(self.price) + "; Description: " + self.description +"; Dimension: "+ ','.join(list(map(str, list(self.kwargs.values()))))

class Customer:
    def __init__(self, surname, name, patronymic, mobile):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        if not  len(mobile)==10:
            raise TypeError("Incorect mobile")
        else:
            self.mobile = mobile
    
    def __str__(self):
        return "\nSurname: "+self.surname +"; \nName: "+ self.name +"; \nPatronymic: "+ self.patronymic +"; \nMobile: "+ self.mobile

class Order():
    def __init__(self, customer, **kwargs):
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



water = Product("Morshinska", 20, "water", width = 5,height =  10)
bigwater = Product("big Morshinska", 40, "water", width = 10,height =  20)

first_customer = Customer("Teleha", "Nikita", "Oleksiyovich","0677987872")

first_order = Order(first_customer, first = water, second = bigwater, third = water)
print(first_order.customerdata(),  first_order.totalvalue(), first_order.productdata())



    
