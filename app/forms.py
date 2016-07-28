from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Required


class loginform(Form):
    username = StringField(validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class pushpostform(Form):
    post = TextAreaField( validators=[DataRequired()])
    date = DateTimeField('Datetime')
    submit = SubmitField('submit')
