from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)

from wtforms.validators import InputRequired, Length


class CoursesForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(min=10, max=1000)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level', 
                       choices=['Beginner','Intermediate','Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')