import math
import random
import sympy as sp
from sympy import symbols, diff

class Derivative:
    def __init__(self):
        self.x = sp.symbols('x')

    def constant_derivative(self):
        """Return the derivative of a constant function."""
        constant = random.randint(1, 134)
        func = constant
        derivative = 0
        return {"function": str(func), "derivative": str(derivative)}

    def power_rule_derivative(self, coeff=None, exponent=None):
        """Return the derivative of a power function."""
        coeff = coeff or random.randint(-5, 5)
        exponent = exponent or random.randint(1, 5)
        func = coeff * self.x**exponent
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

    def product_rule_derivative(self):
        """Return the derivative of a product of two functions."""
        coeff1 = random.randint(-5, 5)
        coeff2 = random.randint(-5, 5)
        exp1 = random.randint(1, 3)
        exp2 = random.randint(1, 3)
        func = (coeff1 * self.x**exp1) * (coeff2 * self.x**exp2)
        derivative = diff(func, self.x)
        return {"function": str(func), "derivative": str(derivative)}

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

    def random_derivative(self, selected_rules, user_input=None, correct_answer=None):
        """
        Generate random derivative problems based on selected rules.
        - selected_rules: List of selected rules (e.g., ["power", "chain"]).
        - user_input: User's last input.
        - correct_answer: The correct answer for the previous problem (optional).
        """
        # Check the user's last input (if provided)
        if user_input is not None and correct_answer is not None:
            if str(user_input) != str(correct_answer):
                return {"status": "incorrect", "message": "Try again!", "correct_answer": correct_answer}

        # Randomly select a rule from the user's choices
        rule = random.choice(selected_rules)

        # Generate a random function based on the selected rule
        if rule == "power":
            problem = self.power_rule_derivative()
        elif rule == "chain":
            problem = self.chain_rule_derivative()
        elif rule == "product":
            problem = self.product_rule_derivative()
        elif rule == "quotient":
            problem = self.quotient_rule_derivative()
        elif rule == "constant":
            problem = self.constant_derivative()
        else:
            raise ValueError("Invalid rule selected.")

        # Return the new problem
        return {"status": "new_problem", "problem": problem}
