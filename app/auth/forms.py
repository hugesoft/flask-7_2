#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email,Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
        Email()])

    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
            'Usernames must have only letters, '
            'numbers, dots or underscores')])

    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])

    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in user.')

class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64),
        Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'Keep me logged in')
    submit = SubmitField(u'登陆')
