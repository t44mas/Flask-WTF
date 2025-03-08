from flask_wtf import FlaskForm
from wtforms.fields.simple import FileField, SubmitField
from wtforms.validators import DataRequired


class galeryForm(FlaskForm):
    file = FileField('Добавить картинку', validators=[DataRequired()])
    submit = SubmitField('Отправить')