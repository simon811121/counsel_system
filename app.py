from flask import Flask, request, render_template, redirect, url_for
from flask.views import MethodView
from api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def hello():
    return "Welcome to counsel system main page!"

if __name__ == '__main__':
    app.run(debug=True)