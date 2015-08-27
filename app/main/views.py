from flask import Flask,render_template

from . import main

@main.route('/')
def index():
    return render_template('index.html')
#'<h1>Hello World!test</h1>'

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
