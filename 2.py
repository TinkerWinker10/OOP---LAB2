from math import gcd

class Rational:
    d = 0

    def __init__(self, num=1, denum=1):
        if not denum != 0:
            raise ZeroDivisionError
        if not isinstance(num, int):
            raise TypeError("Wrong arguments")
        if not isinstance(denum, int):
            raise TypeError("Wrong arguments")
        else:
            self.num = num
            self.denum = denum

    def reducedfraction(self):
        d = gcd(self.num, self.denum)
        self.num = self.num//d
        self.denum = self.denum//d
        return "Reduced form of fraction: " + str(self.num) +"/"+ str(self.denum)
    
    def __truediv__(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num
        return Rational(num, denum)        

    def __add__(self, other):
        num = self.num*other.denum + other.num * self.denum
        denum = self.denum * other.denum
        return Rational(num, denum)

    def __sub__(self, other):
        num = self.num*other.denum - other.num * self.denum
        denum = self.denum * other.denum
        return Rational(num, denum)

    def __mul__(self, other):
        num = self.num*other.num
        denum = self.denum*other.denum
        return Rational(num, denum)
    
    def printfraction(self):
        print("Fraction is: " + str(self.num) +"/"+ str(self.denum))
    
    def div(self):
        return "Float-point format: " + str(self.num/self.denum)

        

x = Rational(2,4)
y = Rational(1,9)
z = x * y
print(x.div())
print(x.reducedfraction())
print(y.reducedfraction())
z.printfraction()
