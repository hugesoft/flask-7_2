#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField(u'请输入你的姓名',  validators=[Required()])
    name.size = 12
    submit = SubmitField(u'提交')
