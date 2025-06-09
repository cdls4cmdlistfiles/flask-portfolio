
from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.secret_key = '$%^BVJSD*)!@_()'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # e.g., 
app.config['MAIL_PORT'] = 587  # For TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'gianerminoespineda@gmail.com'
app.config['MAIL_PASSWORD'] = 'lcorbsogcbzswimd'
app.config['MAIL_DEFAULT_SENDER'] = 'roleplay@gmail.com'

mail = Mail(app)

@app.route('/')
def main():
    template = 'home.html'
    form = ContactForm()
    return render_template(template, form=form)




@app.route('/post-message', methods=['POST'])
def post_message():
    form = ContactForm()
    if form.validate_on_submit():
        # Send email
        msg = Message(
            subject=f"New contact form submission from {form.name.data}",
            recipients=['your-email@example.com'],  # Replace with your email
            body=f"""
            Name: {form.name.data}
            Email: {form.email.data}
            Message: {form.message.data}
            """
        )
     
    mail.send(msg)
    template = 'success.html'
    return render_template(template)
      
@app.get('/close-msg')
def close_msg():
    return "" 

if __name__=='__main__':
    app.run()