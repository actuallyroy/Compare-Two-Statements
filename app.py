from flask import Flask, request
from collections import namedtuple

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Home Page</h1>'


@app.route('/login', methods=["GET", "POST"])
def api():
    user_input = request.args.get("username")
    pass_input = request.args.get("password")
    if(user_input == 'admin' and pass_input == '12345'):
        return {'login': 'success'}
    else:
        return {'login' : 'failed'}
