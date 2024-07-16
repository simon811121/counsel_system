from flask import Blueprint, request, jsonify, make_response, session
from src.data import acnt_info
from src.util import get_cur_time
import datetime
import pytz
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__, url_prefix='/api/v1')
CORS(api, resources=r'/*')

settings = {
    'AUTO_LOGOUT_TIME': 300  # 300 seconds => 5 mins
}
def _settings_update(new_time=300):
    settings['AUTO_LOGOUT_TIME'] = new_time

@api.route('/hello')
def hello():
    return "Welcome to counsel system login function!"

@cross_origin()
@api.route('/register', methods=['POST'])
def register():
    data = request.json
    if data:
        account = data['account']
        if acnt_info.check_account_aval(account) == False:
            result = {'message': 'Data received successfully but registered failed. Duplicate Account'}
            return jsonify(result), 400
        for_time = get_cur_time()
        data['register_time'] = for_time
        data['last_login_time'] = for_time
        rslt = acnt_info.add_acnt_info(**data)
        if rslt:
            result = {'message': 'Data received successfully'}
            return jsonify(result), 200
        else:
            result = {'message': 'Data received successfully but registered failed'}
            return jsonify(result), 400
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
            infos.last_login_time = get_cur_time()
            acnt_info.update_acnt_info(user_id=user_id, last_login_time=infos.last_login_time)
            password = data['password']
            if account not in session:
                session['account'] = user_id
                session['login_time'] = datetime.datetime.now(pytz.timezone('Asia/Taipei'))
            if password == infos.password:
                result = {'message': 'Data received successfully', 'user_id' : user_id}
                return jsonify(result), 200
            else:
                result = {'message': 'Data received successfully but wrong password'}
                return jsonify(result), 401
        else:
            result = {'message': 'Data received successfully but account not found'}
            return jsonify(result), 401
    else:
        result = {'message': 'No data received from frontend'}
        return jsonify(result), 400

@api.route('/logout')
def logout():
    session.pop('account', None)
    session.pop('login_time', None)
    result = {'message': 'Logout successfully'}
    return jsonify(result), 200

@api.route('/check_logout')
def check_logout():
    login_time = session['login_time']
    time_diff = datetime.datetime.now(pytz.timezone('Asia/Taipei')) - login_time
    if time_diff.total_seconds() > settings['AUTO_LOGOUT_TIME']:
        logout()
        result = {'message': 'Auto Logout successfully'}
        return jsonify(result)
    result = {'message': 'Not yet time to logout'}
    return jsonify(result)

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