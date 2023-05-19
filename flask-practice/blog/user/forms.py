from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Save')

    