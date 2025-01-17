import math
import random
import sympy as sp
from sympy import symbols, diff
import anvil.server  # Import the Anvil server library

class Derivative:
    def __init__(self):
        self.x = sp.symbols('x')

    @anvil.server.callable
    def constant_derivative(self):
        """Return the derivative of a constant function."""
        constant = random.randint(1, 134)
        func = constant
        derivative = 0
        return {"function": str(func), "derivative": str(derivative)}

    @anvil.server.callable
    def power_rule_derivative(self, coeff=None, exponent=None):
        """Return the derivative of a power function."""
        coeff = coeff or random.randint(-5, 5)
        exponent = exponent or random.randint(1, 5)
        func = coeff * self.x**exponent
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

    @anvil.server.callable
    def product_rule_derivative(self):
        """Return the derivative of a product of two functions."""
        coeff1 = random.randint(-5, 5)
        coeff2 = random.randint(-5, 5)
        exp1 = random.randint(1, 3)
        exp2 = random.randint(1, 3)
        func = (coeff1 * self.x**exp1) * (coeff2 * self.x**exp2)
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

    @anvil.server.callable
    def quotient_rule_derivative(self):
        """Return the derivative of a quotient of two functions."""
        coeff1 = random.randint(-5, 5)
        coeff2 = random.randint(-5, 5)
        exp1 = random.randint(1, 3)
        exp2 = random.randint(1, 3)
        numerator = coeff1 * self.x**exp1
        denominator = coeff2 * self.x**exp2
        func = numerator / denominator
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

    @anvil.server.callable
    def chain_rule_derivative(self):
        """Return the derivative of a composite function."""
        coeff1 = random.randint(-5, 5)
        coeff2 = random.randint(-5, 5)
        constant = random.randint(-5, 5)
        exp_inner = random.randint(1, 3)
        exp_outer = random.randint(1, 3)
        inner_func = coeff1 * self.x**exp_inner + coeff2 * self.x + constant
        func = (inner_func)**exp_outer
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

    @anvil.server.callable
    def run_const(self):
        return self.constant_derivative()

    @anvil.server.callable
    def run_power(self):
        return self.power_rule_derivative()

    @anvil.server.callable
    def run_product(self):
        return self.product_rule_derivative()

    @anvil.server.callable
    def run_quotient(self):
        return self.quotient_rule_derivative()

    @anvil.server.callable
    def run_chain(self):
        return self.chain_rule_derivative()

    @anvil.server.callable
    def run_game(self):
        print("Welcome to DerivaDash - Mental Math for Derivatives!")

        while True:
            print("\nChoose a challenge:")
            print("1. Solve a constant derivative problem")
            print("2. Solve a derivative problem using power rule")
            print("3. Solve a derivative problem using product rule")
            print("4. Solve a derivative problem using quotient rule")
            print("5. Solve a derivative problem using chain rule")
            print("6. Exit the game")

            choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

            if choice == '1':
                print(self.run_const())

            elif choice == '2':
                print(self.run_power())

            elif choice == '3':
                print(self.run_product())

            elif choice == '4':
                print(self.run_quotient())

            elif choice == '5':
                print(self.run_chain())

            elif choice == '6':
                print("Thanks for playing DerivaDash! Goodbye!")
                break

            else:
                print("Invalid choice. Please input 1, 2, 3, 4, 5, or 6.")

            continue_choice = input("\nDo you want to solve another problem? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thanks for playing DerivaDash! Goodbye!")
                break
