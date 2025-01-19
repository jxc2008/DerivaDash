import random
import sympy as sp

class Integral:
    def __init__(self):
        self.x = sp.symbols('x')

    def constant_integral(self):
        """Calculate the definite integral of a constant."""
        constant = random.randint(1, 10)
        a_bound = random.randint(0, 5)
        b_bound = random.randint(a_bound + 1, a_bound + 5)
        result = constant * (b_bound - a_bound)
        return {
            "function": f"Integral of {constant} from {a_bound} to {b_bound}",
            "result": result
        }

    def linear_integral(self):
        """Calculate the integral of a linear function."""
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        a_bound = random.randint(0, 5)
        b_bound = random.randint(a_bound + 1, a_bound + 5)
        func = a * self.x + b
        result = sp.integrate(func, (self.x, a_bound, b_bound))
        return {
            "function": f"Integral of {a}*x + {b} from {a_bound} to {b_bound}",
            "result": float(result)
        }

    def quadratic_integral(self):
        """Calculate the integral of a quadratic function."""
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        a_bound = random.randint(0, 5)
        b_bound = random.randint(a_bound + 1, a_bound + 5)
        func = a * self.x**2 + b * self.x + c
        result = sp.integrate(func, (self.x, a_bound, b_bound))
        return {
            "function": f"Integral of {a}*x^2 + {b}*x + {c} from {a_bound} to {b_bound}",
            "result": float(result)
        }

    def cubic_integral(self):
        """Calculate the integral of a cubic function."""
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        a_bound = random.randint(0, 5)
        b_bound = random.randint(a_bound + 1, a_bound + 5)
        func = a * self.x**3 + b * self.x**2 + c * self.x + d
        result = sp.integrate(func, (self.x, a_bound, b_bound))
        return {
            "function": f"Integral of {a}*x^3 + {b}*x^2 + {c}*x + {d} from {a_bound} to {b_bound}",
            "result": float(result)
        }

    def u_substitution_integral(self):
        """Calculate the integral using u-substitution."""
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        outer_func = random.choice([sp.sin, sp.cos, sp.exp])
        inner_func = a * self.x + b
        func = outer_func(inner_func) * a
        integral = sp.integrate(func, self.x)
        return {
            "function": f"Integral of {a}*{outer_func.__name__}({inner_func})",
            "result": str(integral) + " + C"
        }

    def integration_by_parts(self):
        """Calculate the integral using integration by parts."""
        u = self.x**2
        dv = sp.exp(self.x)
        du = sp.diff(u, self.x)
        v = sp.integrate(dv, self.x)
        result = u * v - sp.integrate(v * du, self.x)
        return {
            "function": "Integration by parts of x^2 * exp(x)",
            "result": str(result) + " + C"
        }

    
    def random_integral(self, selected_rules, user_input=None, correct_answer=None):
        """
        Generate random integral problems based on selected rules.
        - selected_rules: List of selected rules (e.g., ["constant", "linear"]).
        - user_input: User's last input.
        - correct_answer: The correct answer for the previous problem (optional).
        """
        # Check the user's last input (if provided)
        if user_input is not None and correct_answer is not None:
            if str(user_input) != str(correct_answer):
                return {"status": "incorrect", "message": "Try again!", "correct_answer": correct_answer}

        # Randomly select a rule from the user's choices
        rule = random.choice(selected_rules)

        # Generate a random integral problem based on the selected rule
        if rule == "integer":
            problem = self.constant_integral()
        elif rule == "linear":
            problem = self.linear_integral()
        elif rule == "quadratic":
            problem = self.quadratic_integral()
        elif rule == "cubic":
            problem = self.cubic_integral()
        elif rule == "u_substitution":
            problem = self.u_substitution_integral()
        elif rule == "integration_by_parts":
            problem = self.integration_by_parts()
        else:
            raise ValueError("Invalid rule selected.")

        # Return the new problem
        return {"status": "new_problem", "problem": problem}
