import math
import random
import sympy as sp
from sympy import symbols, diff

class Derivative:
    def __init__(self):
        self.constantOne = None
        self.constantTwo = None
        self.coeffOne = None
        self.coeffTwo = None
        self.exponentOne = None
        self.exponentTwo = None
        self.location = None
        self.x = sp.symbols('x')

    def constantFunc(self):

        constantOne = random.randint(1,134)

        func = constantOne
        func_str = f"{constantOne}"
        return func, func_str
    
    def powerFunc(self):

        coeffOne = random.randint(-5,5)
        exponentOne = random.randint(1,5)

        func = coeffOne * self.x ** exponentOne
        func_str = f"{func}"
        return func, func_str

    def productFunc(self):

        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)

        func = (coeffOne * self.x ** exponentOne) * (coeffTwo * self.x ** exponentTwo)
        func_str = f"{func}"
        return func, func_str

        

    def constant(self):
        check = 0
        func, func_str = self.constantFunc()
        print(f"What's the derivative of {func_str} ?")
        while check < 1:
            i = input()
            if i == "0":
                print("Good job!")
                check = 1
                return
            else:
                print (f"try again \n"  f"What's the derivative of {func_str} ?")

    def power(self):
        check = 0
        location = random.randint(0,5)
        func, func_str = self.powerFunc()
        answer = diff(func,self.x).evalf(subs={self.x: location})
        print(f"What's the derivative of {func_str} at x = {location}?")
        while check < 1:
            i = float(input())
            if i == answer:
                print("Good job!")
                check = 1
                return
            else:
                print ("try again \n" f"What's the derivative of {func_str} at x = {location}?")

    def product(self):
        check = 0
        location = random.randint(0,5)
        func, func_str = self.productFunc()
        val = diff(f, x)
        answer = val.evalf(subs={x: location})
        print("What's the derivative of " + str(f) + " at x = " + str(location))
        while check < 1:
            i = float(input())
            if i == answer:
                print("Good job!")
                check = 1
                return
            else:
                print ("try again")
                print(str(answer))   

    def quotient(self):
        check = 0
        location = random.randint(0,5)
        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)
        x = symbols('x')
        f = (coeffOne * x**exponentOne + constantOne) / (coeffTwo * x**exponentTwo + constantTwo)
        val = diff(f, x)
        answer = val.evalf(subs={x: location})
        print("What's the derivative of " + str(f) + " at x = " + str(location))
        while check < 1:
            i = float(input())
            if i == answer:
                print("Good job!")
                check = 1
                return
            else:
                print ("try again")
                print(str(answer))

    def chain(self):
        check = 0
        location = random.randint(0,5)
        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)
        x = symbols('x')
        f = (constantOne * (coeffOne * x**exponentOne + coeffTwo * x + constantTwo)**exponentTwo)
        val = diff(f, x)
        answer = val.evalf(subs={x: location})
        print("What's the derivative of " + str(f) + " at x = " + str(location))
        while check < 1:
            i = float(input())
            if i == answer:
                print("Good job!")
                check = 1
                return
            else:
                print ("try again")
                print(str(answer))
