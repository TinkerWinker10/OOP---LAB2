from typing import Type


class Product:
    """
    Class, which descibes a Product of online store
    """
    def __init__(self,product, price, description, **kwargs):
        self.product = product
        self.price = price
        self.description = description
        self.kwargs = kwargs
    
    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, data):
        if not isinstance(data, str):
            raise TypeError("Product name must be a string")
        if  not len(data):
            raise ValueError("Product name cant be empty")

        self.__product = data

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError("Product price must be a number")
        if  not data:
            raise ValueError("Product price cant be empty")
        if  data<0:
            raise ValueError("Product price cant be below zero")

        self.__price = data
    
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, data):
        if not isinstance(data, str):
            raise TypeError("Product description must be a string")
        if  not data:
            raise ValueError("Product description cant be empty")

        self.__description = data

    def get_value(self):
        """
        Method, which returns instance price
        """
        return self.price

    def __str__(self):
        """
        Returns instance attrbutes
        """
        return f'Product:{self.product} Price: {self.price} Description: {self.description}Dimensions:{",".join(list(map(str, list(self.kwargs.values()))))}'

class Customer:

    def __init__(self, surname, name, patronymic, mobile):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile = mobile
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        if not isinstance(data, str):
            raise TypeError("Name must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__name = data

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, data):
        if not isinstance(data, str):
            raise TypeError("Patronymic must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__patronymic = data

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, data):
        if not isinstance(data, str):
            raise TypeError("Surname must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__surname = data


    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, data):
        if not isinstance(data, int):
            raise TypeError("Mobile must be a number")
        if not data:
            raise ValueError("Field cannot be empty")
        if len(str(data))>12:
            raise ValueError("Mobile length cant be more than 12 digits")

        self.__mobile = data


    def __str__(self):
        """
        Returns instance attrbutes
        """
        return f'\nSurname: {self.surname}\nName: {self.name}\nPatronymic: {self.patronymic}\nMobile: {self.mobile}'

class Order():
    """
    Class, which describes order"""
    def __init__(self, customer = None, **kwargs):
        self.customer_name = customer.name
        self.customer_surname = customer.surname
        self.mobile = customer.mobile
        self.kwargs = kwargs

    def total_value(self):
        """
        Method, which returns total price of order
        """
        total = 0
        for key in self.kwargs:
            total += self.kwargs[key].get_value()
        return total    
    

    def __str__(self):
        """
        Method, which returns info about order
        """
        return f'Surname: {self.customer_surname}\nName: {self.customer_name}\nMobile: {self.mobile}\nOrder info:{list(map(str, list(self.kwargs.values())))}'


if __name__=='__main__':
    water = Product("Morshinska", 20, "water", width = 5,height =  10)
    bigwater = Product("big Morshinska", 40, "water", width = 10,height =  20)
    customer = Customer("Nikita", "Teleha", "Oleksiyovish", 380671467985)


    order = Order(customer, first = water, second = bigwater)
    print(order)
    print("Order value:",order.total_value())
    
