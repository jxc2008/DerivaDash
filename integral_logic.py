import math
import random
import sympy as sp

class Integral:
    def __init__(self):
        self.constant_one = None
        self.coefficient = 0
        self.x = sp.symbols('x')
        
    def zero(self):
        question = "What's the integral of 0, from x = 0 to x = 1?"
        correct_answer = "1"
        
        print(question)
        
        while True:
            answer = input("Your answer: ").strip()
            
            if answer == correct_answer:
                print("Good job!")
                break 
            else:
                print("Try again.")
                print(question)
    
    def generate_linear_function(self):
        a = random.randint(-10, 10)
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        
        func = a * self.x + b
        
        func_str = f"{a}*x + {b}" if b >= 0 else f"{a}*x - {abs(b)}"
        
        return func, func_str
    
    def linear_function(self):
        func, func_str = self.generate_linear_function()
        
        problem_type = random.choice(['indefinite', 'definite'])
        
        if problem_type == 'indefinite':
            integral = sp.integrate(func, self.x)
            question = f"Find the indefinite integral of {func_str} with respect to x."
            correct_answer = integral
        else:
            a_bound = random.randint(-10, 10)
            b_bound = random.randint(-10, 10)
            while b_bound == a_bound:
                b_bound = random.randint(-10, 10)
            
            integral = sp.integrate(func, (self.x, a_bound, b_bound))
            question = f"Calculate the integral of {func_str} from x = {a_bound} to x = {b_bound}."
            correct_answer = integral.evalf()
        
        print("\n" + question)
        
        user_input = input("Your answer: ").strip()
        
        if problem_type == 'indefinite':
            try:
                user_expr = sp.sympify(user_input)
                derivative = sp.diff(user_expr, self.x)
                difference = sp.simplify(derivative - func)
                if difference == 0:
                    print("Good job! Your answer is correct.")
                else:
                    print(f"Incorrect. The correct answer is {integral} + C.")
            except (sp.SympifyError, TypeError):
                print(f"Invalid input. The correct answer is {integral} + C.")
        else:
            try:
                user_answer = float(user_input)
                correct_numeric = float(correct_answer)
                if abs(user_answer - correct_numeric) < 1e-2:
                    print("Good job! Your answer is correct.")
                else:
                    print(f"Incorrect. The correct answer is approximately {correct_numeric:.2f}.")
            except ValueError:
                print(f"Invalid input. The correct answer is approximately {correct_answer:.2f}.")
    
    def generate_uSub_function(self):
        a = random.randint(-10, 10)
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        
        outer_functions = [
            sp.sin,
            sp.cos,
            sp.exp,
            sp.log,
            sp.sqrt,
            sp.tan,
            sp.cot,
            sp.sec,
            sp.csc,           
        ]
        
        outer_func = random.choice(outer_functions)
        inner_function = a * self.x + b
        func = outer_func(inner_function) * a
        
        func_name_map = {
            sp.sin: "sin",
            sp.cos: "cos",
            sp.exp: "exp",
            sp.log: "ln",
            sp.sqrt: "sqrt",
            sp.tan: "tan",
            sp.cot: "cot",
            sp.sec: "sec",
            sp.csc: "csc"
        }
        
        outer_func_name = func_name_map.get(outer_func, "f")
        
        if b >= 0:
            func_str = f"{outer_func_name}({a}*x + {b}) * {a}"
        else:
            func_str = f"{outer_func_name}({a}*x - {abs(b)}) * {a}"
        
        return func, func_str
    
    def uSub_function(self):
        
        integrand, integrand_str = self.generate_uSub_function()
        
        problem_type = random.choice(['indefinite', 'definite'])
        if problem_type == "indefinite":
            integral = sp.integrate(integrand, self.x)
            question = f"Find the indefinite integral of {integrand_str} with respect to x."
            correct_answer = integral
        else:
            a_bound = random.randint(-10, 10)
            b_bound = random.randint(-10, 10)
            while b_bound == a_bound:
                b_bound = random.randint(-10, 10)
            
            integral = sp.integrate(integrand, (self.x, a_bound, b_bound))
            question = f"Calculate the integral of {integrand_str} from x = {a_bound} to x = {b_bound}."
            correct_answer = integral.evalf()
            
            print("\n" + question)
            
            user_input = input("Your answer: ").strip()
            
            if problem_type == 'indefinite':
                try:
                    user_expr = sp.sympify(user_input)
                    derivative = sp.diff(user_expr, self.x)
                    difference = sp.simplify(derivative - func)
                    if difference == 0:
                        print("Good job! Your answer is correct.")
                    else:
                        print(f"Incorrect. The correct answer is {integral} + C.")
                except (sp.SympifyError, TypeError):
                    print(f"Invalid input. The correct answer is {integral} + C.")
            else:
                try:
                    user_answer = float(user_input)
                    correct_numeric = float(correct_answer)
                    if abs(user_answer - correct_numeric) < 1e-2:
                        print("Good job! Your answer is correct.")
                    else:
                        print(f"Incorrect. The correct answer is approximately {correct_numeric:.2f}.")
                except ValueError:
                    print(f"Invalid input. The correct answer is approximately {correct_answer:.2f}.")

    def run_game(self):
        print("Welcome to DerivaDash - Mental Math for Integrals!")
        
        while True:
            print("\nChoose a challenge:")
            print("1. Solve a linear integral problem")
            print("2. Solve a zero integral problem")
            print("3, Solve a u-sub integral problem")
            print("4. Exit the game")
            
            choice = input("Enter your choice (1/2/3/4): ").strip()
            
            if choice == '1':
                self.linear_function()
            elif choice == '2':
                self.zero()
            elif choice == '3':
                self.uSub_function()
            elif choice == '4':
                print("Thanks for playing DerivaDash! Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
                continue  # Loop back if invalid input
            
            # Ask the user if they want to continue
            continue_choice = input("\nDo you want to solve another problem? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thanks for playing DerivaDash! Goodbye!")
                break


