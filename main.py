from flask import Flask,request, render_template,redirect
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/", methods=['POST'])
def valid():
    User_name = request.form['user-name']
    Password = request.form['password']
    Verify_Password = request.form['verify-password']
    Email= request.form['email']
    un_error=''
    pw_error=''
    vp_error=''
    mail_error=''


    if User_name == '' or len(User_name) < 3 or len(User_name) > 20:
       un_error= 'That is not a valid username'
    
    if Password == '' or len(Password) < 3 or len(Password) > 20:
       pw_error= 'That is not a valid password'
    if Password != Verify_Password:
        vp_error='Passwords dont match'
    if Verify_Password == '':
        vp_error= 'That is not a valid password'
    if len(Email)>0:
        if len(Email) < 3 or len(Email) > 20 or Email.count('@') > 1 or Email.count(".")>1:
            mail_error='Please enter valid email address'

    if not un_error and not pw_error and not vp_error and not mail_error:
        msg = User_name
        return redirect('valid-form?msg={0}' .format(msg))
    
    
    
    
        
    else:
        return render_template('login.html', User_name=User_name, un_error=un_error,pw_error=pw_error,vp_error=vp_error,mail_error=mail_error, Password=Password, Verify_Password=Verify_Password, Email=Email)

      
@app.route("/valid-form")
def login():
    msg = request.args.get('msg')
    #return render_template('welcome.html', User_name=User_name)
    return render_template('welcome.html', msg= msg)

app.run()