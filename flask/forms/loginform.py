from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.numeric import DecimalField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = DecimalField('id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = DecimalField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')