from flask import Blueprint, request, jsonify, make_response
from src.data import acnt_info
import datetime

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/hello')
def hello():
    return "Welcome to counsel system login function!"

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    if data:
        cur_time = datetime.datetime.now()
        for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
        data['register_time'] = for_time
        data['last_login_time'] = for_time
        rslt = acnt_info.add_acnt_info(**data)
        if rslt:
            result = {'message': 'Data received successfully'}
            return jsonify(result), 200
        else:
            result = {'message': 'Data received successfully but registered failed'}
            return jsonify(result), 201
    else:
        result = {'message': 'No data received from frontend'}
        return jsonify(result), 400

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    if data:
        account = data['account']
        infos = acnt_info.find_acnt_info(account=account)
        if infos:
            user_id = infos.user_id
            result = {'message': 'Data received successfully', 'user_id' : user_id}
            return jsonify(result), 200
        else:
            result = {'message': 'Data received successfully but account not found'}
            return jsonify(result), 201
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


@api.route('/account/<account_id>', methods=['GET', 'PUT'])
def get_account(account_id):
    if request.method == 'GET':
        if account_id:
            result = {'message': 'Data received successfully', 'account_id': account_id}
            return jsonify(result), 200
        else:
            result = {'message': 'No data received from frontend'}
            return jsonify(result), 400
    elif request.method == 'PUT':
        response = make_response("Request successful", 200)
        return response
    else:
        return jsonify({"error": "Method not allowed"}), 405

@api.route('/password/forget', methods=['POST'])
def forget_password():
    result = {'message': 'forget password!!!'}
    return jsonify(result), 200

@api.route('/password/setup', methods=['POST', 'GET'])
def setup_password():
    if request.method == 'POST':
        result = {'message': 'setup password POST!!!'}
        return jsonify(result), 200
    elif request.method == 'GET':
        result = {'message': 'setup password GET!!!'}
        return jsonify(result), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405