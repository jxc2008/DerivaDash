import math
import random
import sympy as sp

class Integral:
    def __init__(self):
        self.constant_one = None
        self.coefficient = 0
        self.x = sp.symbols('x')
        
    def constant_integral(self):
        constant = random.randint(1, 10)
        a_bound = random.randint(0, 5)
        b_bound = random.randint(a_bound + 1, a_bound + 5) 
        
        question = f"What's the integral of {constant}, from x = {a_bound} to x = {b_bound}?"
        correct_answer = str(constant * (b_bound - a_bound))
        
        print(f"[CONSTANT FUNCTION] {question}")
        
        while True:
            answer = input("Your answer: ").strip()
            
            if answer == correct_answer:
                print("Good job!")
                break
            else:
                print(f"Incorrect. The answer is {correct_answer}.")
                break
    
    def generate_linear_function(self):
        a = random.randint(-10, 10)
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        
        func = a * self.x + b
        
        func_str = f"{a}*x + {b}" if b >= 0 else f"{a}*x - {abs(b)}"
        
        return func, func_str
    
    def linear_function(self):
        self.execute_function(self.generate_linear_function, "linear")
    
    def generate_quadratic_function(self):
        a = random.randint(-10, 10)
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        
        func = a * self.x**2 + b * self.x + c
        
        func_str = f"{a}*x**2"
        func_str += f" + {b}*x" if b >= 0 else f" - {abs(b)}*x"
        func_str += f" + {c}" if c >= 0 else f" - {abs(c)}"
        
        return func, func_str
    
    def quadratic_function(self):
        self.execute_function(self.generate_quadratic_function, "quadratic")
        
    def generate_cubic_function(self):
        a = random.randint(-10, 10)
        while a == 0:
            a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        
        func = a * self.x**3 + b * self.x**2 + c * self.x + d
        
        func_str = f"{a}*x**3"
        func_str += f" + {b}*x**2" if b >= 0 else f" - {abs(b)}*x**2"
        func_str += f" + {c}*x" if c >= 0 else f" - {abs(c)}*x"
        func_str += f" + {d}" if d >= 0 else f" - {abs(d)}"
        
        return func, func_str
    
    def cubic_function(self):
        self.execute_function(self.generate_cubic_function, "cubic")
        
    def execute_function(self, generate_func, func_type):
        func, func_str = generate_func()
        
        problem_type = random.choice(['indefinite', 'definite'])
        
        if problem_type == 'indefinite':
            integral = sp.integrate(func, self.x)
            question = f"Find the indefinite integral of {func_str} with respect to x."
            correct_answer = integral
        else:
            a_bound = random.randint(-10, 10)
            b_bound = random.randint(-10, 15)
            while b_bound <= a_bound:
                b_bound = random.randint(-10, 15)
            
            integral = sp.integrate(func, (self.x, a_bound, b_bound))
            question = f"Calculate the integral of {func_str} from x = {a_bound} to x = {b_bound}."
            correct_answer = integral.evalf()
        
        print(f"\n[{func_type.upper()} FUNCTION] {question}")
        
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
                correct_numeric = float(correct_answer.evalf())
                if abs(user_answer - correct_numeric) < 1e-2:
                    print("Good job! Your answer is correct.")
                else:
                    print(f"Incorrect. The correct answer is approximately {correct_numeric:.2f}.")
            except ValueError:
                print(f"Invalid input. The correct answer is approximately {float(correct_answer.evalf()):.2f}.")
                
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
        self.execute_function(self.generate_uSub_function, "uSub")
    
    def generate_ibp_function(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        
        self.trig_functions = ['sin(x)', 'cos(x)', 'tan(x)', 'sec(x)', 'csc(x)', 'cot(x)'] 
        self.inv_trig_functions = ['asin(x)', 'acos(x)', 'atan(x)', 'asec(x)', 'acsc(x)', 'acot(x)']  
        self.poly_functions = ['x', 'x**2', 'x**3']
        
        self.trig_function = random.choice(self.trig_functions)
        self.inv_trig_function = random.choice(self.inv_trig_functions)
        self.poly_function = random.choice(self.poly_functions)
        
        self.ibp_problems = {
            "Poly × Exp": f"{a} * {self.poly_function} * exp({b} * x)",
            "Poly × Log": f"{a} * {self.poly_function} * log({b} * x)",
            "Poly × Trig": f"{a} * {self.poly_function} * {self.trig_function}",
            "Exp × Trig": f"{a} * exp({b} * x) * {self.trig_function}",
            "Log Alone": f"{a} * log({b} * x)",
            "Inverse Trig × Poly": f"{a} * {self.inv_trig_function} * {self.poly_function}"
        }
        
        problem_type = random.choice(list(self.ibp_problems.keys()))
        func = self.ibp_problems[problem_type]
        expression = sp.sympify(func)
        func_str = str(expression)
        
        return func, func_str

    def ibp_function(self):
        self.execute_function(self.generate_ibp_function, "ibp")
        
    def run_game(self):
        print("Welcome to DerivaDash - Mental Math for Integrals!")
        
        while True:
            print("\nChoose a challenge:")
            print("1. Solve a constant integral problem")
            print("2. Solve a linear integral problem")
            print("3. Solve a quadratic integral problem")
            print("4. Solve a cubic integral problem")
            print("5. Solve a u-substitution integral problem")
            print("6. Solve an integration by parts integral problem")
            print("7. Exit the game")
            
            choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()
            
            if choice == '1':
                self.constant_integral()
            elif choice == '2':
                self.linear_function()
            elif choice == '3':
                self.quadratic_function()
            elif choice == '4':
                self.cubic_function()
            elif choice == '5':
                self.uSub_function()
            elif choice == '6':
                self.ibp_function()
            elif choice == '7':
                print("Thanks for playing DerivaDash! Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, or 7.")
                continue
            
            continue_choice = input("\nDo you want to solve another problem? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thanks for playing DerivaDash! Goodbye!")
                break


