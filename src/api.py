from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/hello')
def hello():
    return "Welcome to counsel system login function!"

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    if data:
        result = {'message': 'Data received successfully', 'data': data}
        return jsonify(result), 200
    else:
        result = {'message': 'No data received from frontend'}
        return jsonify(result), 400

@api.route('/logout')
def logout():
    result = {'message': 'Logout successfully'}
    return jsonify(result), 200

@api.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        data = request.json
        result = {'message': 'account POST', 'data': data}
        return jsonify(result), 200
    elif request.method == 'GET':
        result = {'message': 'account GET'}
        return jsonify(result), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405


@api.route('/account/<account_id>', methods=['GET'])
def get_account(account_id):
    if account_id:
        result = {'message': 'Data received successfully', 'account_id': account_id}
        return jsonify(result), 200
    else:
        result = {'message': 'No data received from frontend'}
        return jsonify(result), 400