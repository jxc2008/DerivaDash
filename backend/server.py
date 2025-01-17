from flask import Flask, request, jsonify
from flask_cors import CORS
from derivative_logic import Derivative
from integral_logic import Integral

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

derivative = Derivative()
integral = Integral()

@app.route('/random_problem', methods=['POST'])
def random_problem():
    data = request.json
    selected_rules = data.get('selected_rules', [])
    user_input = data.get('user_input')
    correct_answer = data.get('correct_answer')

    # Separate derivative and integral rules
    derivative_rules = [rule for rule in selected_rules if "rule" in rule]
    integral_rules = [rule for rule in selected_rules if "function" in rule]

    # Randomly choose between derivative and integral (if both are selected)
    if derivative_rules and integral_rules:
        choice = random.choice(["derivative", "integral"])
    elif derivative_rules:
        choice = "derivative"
    elif integral_rules:
        choice = "integral"
    else:
        return jsonify({"status": "error", "message": "No valid rules selected."})

    # Generate the problem based on the choice
    if choice == "derivative":
        result = derivative.random_derivative(derivative_rules, user_input, correct_answer)
    else:
        result = integral.random_integral(integral_rules, user_input, correct_answer)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)