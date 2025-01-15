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

    def quotientFunc(self):

        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)

        func = (coeffOne * self.x ** exponentOne) / (coeffTwo * self.x ** exponentTwo)
        func_str = f"{func}"
        return func, func_str
    
    def chainFunc(self):

        constantOne = random.randint(-5,5)
        constantTwo = random.randint(-5,5)
        coeffOne = random.randint(-5,5)
        coeffTwo = random.randint(-5,5)
        exponentOne = random.randint(1,3)
        exponentTwo = random.randint(1,3)

        func = (constantOne * (coeffOne * self.x**exponentOne + coeffTwo * self.x + constantTwo)**exponentTwo)
        func_str = f"{func}"
        return func, func_str
    
    def runConst(self):
        self.execute_function(self.constantFunc, "linear")

    def runPower(self):
        self.execute_function(self.powerFunc, "quadratic")

    def runProduct(self):
        self.execute_function(self.productFunc, "quadratic")

    def runQuot(self):
        self.exectute_function(self.quotientFunc, "quadratic")

    def runChain(self):
        self.execute_function(self.chainFunc, "quadratic")
 
    def execute_function(self, generate_func, func_type):
    
        func, func_str = generate_func()

        problem_type = random.choice(['indefinite', 'definite'])

        if problem_type == 'indefinite':
            derivative = sp.diff(func, self.x)
            question = f"What's the derivative of {func_str}?"
            answer = derivative
        else:
            location = random.randint(0,5)   
            derivative = sp.diff(func, self.x)
            question = f"What's the derivative of {func_str}"
            answer = derivative.evalf()
    
        print(f"\n[{func_type.upper()} FUNCTION] {question}")

        user_input = input("Your answer: ").strip()

        if problem_type == 'indefinite':
            try:
                user_simp= sp.sympify(user_input)
                difference = sp.simplify(user_simp - func)
                if difference == 0:
                    print("Good job! Your answer is correct.")
                else:
                    print(f"Incorrect. The correct answer is {derivative}")
            except (sp.SympifyError, TypeError):
                print(f"Invalid input. The correct answer is {derivative}")
        else:
            try:
                user_ans = user_input
                correct_numeric = float(answer)
                if abs(user_ans - correct_numeric) < 1e-2:
                    print("Good job! Your answer is correct.")
                else:
                    print(f"Incorrect. The correct answer is approximately {correct_numeric:.2f}.")
            except ValueError:
                print(f"Invalid input. The correct answer is approximately {answer:.2f}.")
                
    def runGame(self):
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

            if choice == 1:
                self.runConst

            elif choice == 2:
                self.runPower

            elif choice == 3:
                self.runProduct

            elif choice == 4:
                self.runQuot
            
            elif choice == 5:
                self.runChain
            
            else:
                print("Invalid choice. Please input either 1,2,3,4,5 or 6.")
                continue
           
            continue_choice = input("\nDo you want to solve another problem? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thanks for playing DerivaDash! Goodbye!")
                break
            




