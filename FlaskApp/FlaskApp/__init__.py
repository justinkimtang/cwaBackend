from flask import Flask , render_template, flash, redirect, url_for, request
import bcrypt
from dbconnect import connection

app = Flask(__name__)
@app.route("/")
def home():
    title = "Home Page"
    paragraph = ["This is where the home page will go"]
    return render_template("index.html", title = title, paragraph =paragraph)

@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    response = ''
    try:
        if request.method =='POST':
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            hashed = bcrypt.hashpw(str(attempted_password),bcrypt.gensalt())
            
            try:
                c, conn = connection()
                c.execute("SELECT password FROM users WHERE username=%s OR email=%s",[attempted_username, attempted_username])
                for password in c:
                    p = ("{}".join(password))

                    if p == bcrypt.hashpw(str(attempted_password),p):
                         return redirect(url_for('dashboardpage'))
                    else:
                         flash('invalid password')
            except:
                response ="execute failed"
                conn.rollback()
                
            return render_template("login.html",error=response)
        else:
            response = "Waiting for insert"
            return render_template("login.html",error=response)
    
    except Exception as e:
        #flash(e)
        return render_template("login.html",error = response)

@app.route('/dashboard/')
def dashboardpage():
    return render_template("dashboard.html")


@app.route('/sign-up/', methods = ['GET', 'POST'])
def sign_up_page():
    response = ''
    try:
        if request.method =='POST':
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            attempted_email = request.form['email']
            attempted_firstname = request.form['first_name']
            attempted_lastname = request.form['last_name']
            hashed = bcrypt.hashpw(str(attempted_password),bcrypt.gensalt())

            try:
                c, conn = connection()
                c.execute("SELECT username FROM users WHERE username=%s UNION SELECT email FROM users WHERE email=%s",[attempted_username,attempted_email])
                if c.rowcount == 0:
                    c.execute("INSERT INTO users(username,password,email,first_name,last_name) VALUES(%s,%s,%s,%s,%s)",[attempted_username,hashed,attempted_email,attempted_firstname,attempted_lastname])
                    conn.commit()
                    return redirect(url_for('dashboardpage'))
                else:
                    response = 'username or email is already taken'
                    conn.rollback()
                    return render_template("signup.html",error=response)
            except:
                response ="execute failed"
                conn.rollback()
                
            return render_template("signup.html",error=response)
        else:
            response = ""
            return render_template("signup.html",error=response)
    
    except Exception as e:
        response = "request failure"
        return render_template("signup.html",error = response)
            

        
if __name__ == "__main__":
    app.run()
