#coding:utf-8
from flask import Flask,render_template

from . import main
from .. import db
from ..models import Role,User
from ..email import send_email

@main.route('/')
def index():
    return render_template('index.html')
#'<h1>Hello World!test</h1>'

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/createdb')
def createdb():
    db.create_all()
    admin_role = Role(name = 'Admin')
    mod_role = Role(name = 'Moderator')
    user_role = Role(name = 'User')
    user_john = User(username = 'john', role = admin_role)
    user_susan = User(username = 'susan', role = user_role)
    user_david = User(username = 'david', role = user_role)

    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)

    db.session.commit()
    return render_template('user.html', name = 'create_all')

@main.route('/drop')
def drop_all():
    db.drop_all()
    return  render_template('user.html', name = 'drop_all')

@main.route('/find/<name>')
def find(name):
    show = User.query.filter_by(username=name).first()
    if show != None:
        return render_template('user.html', name = show.username)
    else:
        return render_template('user.html', name = name + u' 找不到.')

@main.route('/mail')
def email():
    send_email('hugesoft@126.com', u'马翔的电子邮件测试标题',
        'mail/new_user', user = 'hugesoft@126.com')
    return render_template('user.html',user = 'email send test')

