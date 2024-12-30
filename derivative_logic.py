import math
import random
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

    def constant(self):
        x = 0
        constantOne = random.randint(1,134)
        print("What's the derivative of " + str(constantOne) + " ?")
        while x < 1:
            i = input()
            if i == "0":
                print("Good job!")
                x = 1
                return
            else:
                print ("try again")
                print("What's the derivative of " + str(constantOne) + " ?")

    def power(self):
        x = 0
        coeffOne = random.randint(-10,10)
        location = random.randint(0,5)
        exponentOne = random.randint(1,5)
        answer = coeffOne * exponentOne * (location**(exponentOne-1))
        print("What's the derivative of " + str(coeffOne) + "x^" + str(exponentOne) + " at x = " + str(location) + " ?")
        while x < 1:
            i = float(input())
            if i == answer:
                print("Good job!")
                x = 1
                return
            else:
                print ("try again")
                print("What's the derivative of " + str(coeffOne) + "x^" + str(exponentOne) + " at x = " + str(location) + " ?")
                print(str(answer))

    def product(self):
        check = 0
        location = random.randint(0,5)
        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)
        x = symbols('x')
        f = (coeffOne * x**exponentOne + constantOne) * (coeffTwo * x**exponentTwo + constantTwo)
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
