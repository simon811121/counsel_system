from flask import Flask
from src.api import api
from src.home import home
import os

def create_app():
    flask_app = Flask(__name__)
    flask_app.secret_key = os.urandom(16)
    flask_app.register_blueprint(home)
    flask_app.register_blueprint(api)

    return flask_app

if __name__ == '__main__':
    server = create_app()
    server.run('0.0.0.0', port=5000, debug=True)
