from flask import Flask, request, jsonify
from flask_cors import CORS
from salary_calculator import SalaryCalculator

app = Flask(__name__)
CORS(app)
calculator = SalaryCalculator()

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    position = data.get('position')
    period = data.get('period')
    
    if not position or not period:
        return jsonify({'error': 'Missing position or period'}), 400
    
    if position not in ['OEP', 'OE', 'CE']:
        return jsonify({'error': 'Invalid position'}), 400
    
    if period not in ['January', 'July']:
        return jsonify({'error': 'Invalid period'}), 400

    result = calculator.calculate_salary(position, period)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
