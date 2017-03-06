from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(Form):
    pid = StringField('PID', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)


class SignUpForm(Form):
    pid = StringField('PID', validators=[DataRequired()])
    password = PasswordField("Desired password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Repeat password", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
