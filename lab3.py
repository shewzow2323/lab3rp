from flask import Flask, request, jsonify
import random

app = Flask(__name__)
stored_number = None
stored_operation = None
@app.route('/number', methods=['GET'])
def get_number():
    param = request.args.get('param', type=int)
    if param is not None:
        random_num = random.randint(1, 10)
        result = random_num * param
        global stored_number, stored_operation
        stored_number = result
        stored_operation = "multiply"
        return jsonify({'number': result, 'operation': 'multiply'})
    else:
        return jsonify({'error': 'Parameter "param" is missing'}), 400

@app.route('/number', methods=['POST'])
def post_number():
    data = request.get_json()
    if 'jsonParam' in data:
        random_num = random.randint(1, 10)
        result = random_num * data['jsonParam']
        global stored_number, stored_operation
        stored_number = result
        stored_operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
        return jsonify({'number': result, 'operation': stored_operation})
    else:
        return jsonify({'error': 'Field "jsonParam" is missing'}), 400

@app.route('/number', methods=['DELETE'])
def delete_number():
    random_num = random.randint(1, 10)
    global stored_number, stored_operation
    stored_number = random_num
    stored_operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
    return jsonify({'number': random_num, 'operation': stored_operation})

if __name__ == '__main__':
    app.run(debug=True)
