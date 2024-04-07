from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

# Add any form classes for Flask-WTF here

class MovieForm(FlaskForm):
    title = StringField('Title', validators =[DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpeg', 'png'])])