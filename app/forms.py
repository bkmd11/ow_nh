from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewRouteForm(FlaskForm):
    name = StringField('Route Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    picture_name = StringField('Picture File Name')
    description = StringField('Description', validators=[DataRequired()])
    directions = StringField('Getting There', validators=[DataRequired()])
