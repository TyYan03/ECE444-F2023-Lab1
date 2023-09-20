from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/Tyler')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
