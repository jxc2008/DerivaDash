from flask import Flask, request, jsonify
from flask_cors import CORS
from derivative_logic import Derivative
from integral_logic import Integral  # Import the Integral class if needed

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

derivative = Derivative()
integral = Integral()  # Instantiate Integral if you plan to create endpoints for integrals

@app.route('/random_derivative', methods=['POST'])
def random_derivative():
    data = request.json
    selected_rules = data.get('selected_rules', [])
    user_input = data.get('user_input')
    correct_answer = data.get('correct_answer')

    # Use the existing logic to generate a random derivative
    result = derivative.random_derivative(selected_rules, user_input, correct_answer)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
