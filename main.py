
# factory.py
from flask import Flask


from src.api import api
from src.home import home
from src.data import Account_Info


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(home)
    flask_app.register_blueprint(api)

    return flask_app

def create_acnt_info():
    acnt_info = Account_Info()
    return acnt_info

if __name__ == '__main__':
    server = create_app()
    server.run('0.0.0.0', port=5000, debug=True)
    acnt_info = create_acnt_info()
