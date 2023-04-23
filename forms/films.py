from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class FilmsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    submit = SubmitField('Применить')