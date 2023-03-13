from flask import Flask, flash, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/oneth/University/SDGP/Login/database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route('/')
def loginpage():
    return render_template('login.html')
 
@app.route('/', methods=['POST'])
def login():
    
    email = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('SELECT * FROM user WHERE email=? AND password=?',(email, password))
    row = c.fetchone()
    
    if row:
        c1 = conn.cursor()
        c1.execute('SELECT username, password FROM user WHERE username=? AND password=?',(email, password))
        row1 = c1.fetchone()
        email, password = row1

        session['username'] = username

        return redirect('/home')
    
    else:
        
        flash("Enter details are wrong! Please check again")
        
        return redirect('/')

    return render_template('login.html')

@app.route('/signup')
def signupPage():
    return render_template('SignUp.html')   



if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(port= 3000, debug=True)    