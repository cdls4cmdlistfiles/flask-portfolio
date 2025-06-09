
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = EmailField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')