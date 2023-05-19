from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms import StringField, SubmitField, PasswordField
from .dao import user_dao


class UserRegistration(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if user_dao.check_user_exists(username=username):
            raise ValidationError('User is already registered. Please use a different username.')


class UserLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Save')