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

    def run_integral(self):
        print("Welcome to DerivaDash - Mental Math for Integrals!")

        while True:
            print("\nChoose a challenge:")
            print("1. Solve a constant integral problem")
            print("2. Solve a linear integral problem")
            print("3. Solve a quadratic integral problem")
            print("4. Solve a cubic integral problem")
            print("5. Solve a u-substitution integral problem")
            print("6. Solve an integration by parts problem")
            print("7. Exit the game")

            choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()

            if choice == '1':
                print(self.constant_integral())

            elif choice == '2':
                print(self.linear_integral())

            elif choice == '3':
                print(self.quadratic_integral())

            elif choice == '4':
                print(self.cubic_integral())

            elif choice == '5':
                print(self.u_substitution_integral())

            elif choice == '6':
                print(self.integration_by_parts())

            elif choice == '7':
                print("Thanks for playing DerivaDash! Goodbye!")
                break

            else:
                print("Invalid choice. Please input 1, 2, 3, 4, 5, 6, or 7.")

            continue_choice = input("\nDo you want to solve another problem? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thanks for playing DerivaDash! Goodbye!")
                break
