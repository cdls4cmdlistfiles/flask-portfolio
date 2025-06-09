from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', 
                      validators=[DataRequired()],
                      render_kw={"placeholder": "Your name"})
    
    email = StringField('Email',
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Your email address"})
    
    message = TextAreaField('Message',
                          validators=[DataRequired()],
                          render_kw={"placeholder": "Your message here..."})
    
    submit = SubmitField('Submit')
