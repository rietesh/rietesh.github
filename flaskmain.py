from flask import Flask, render_template, request
from flask_mail import Mail, Message
import requests
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '90b6edb3c2dd44'
app.config['MAIL_PASSWORD'] = '21d3a6d22ff1ed'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/", methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

# message object mapped to a particular URL ‘/’
@app.route("/sendmail", methods = ['POST'])
def index1():
    if request.method == 'POST':
        Name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        msg = Message(
                    'Hello from {}'.format(Name),
                    sender =email,
                    recipients = ['receiversid@gmail.com']
                    )
        msg.body = "The sender's emailid: {} \nMessage: {}".format(email, message)
        with open('mail.logs' , 'a') as f:
            f.write("The sender's emailid: {} \nMessage: {} \n".format(email, message))
        
        # mail.send(msg)
        return render_template('thankyou.html')
   
if __name__ == '__main__':
    app.run()
