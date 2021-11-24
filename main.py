import os
from flask import Flask, render_template, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import passlib


app = Flask(__name__)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'FrostHead'
app.config['MYSQL_PASSWORD'] = 'FrostHead@439751'
app.config['MYSQL_DB'] = 'ecommerce'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    return render_template('Home.html', whatsNew=[{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'active':'False','title':'Check out are all new math course','price':'599','image':'/static/whatsNew3.jpeg'}])

@app.route('/create-account', methods=['GET','POST'])
def createAccount():
    if "user" in session:
        return redirect('/')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        username = request.form['username']
        cur = mysql.connection.cursor()
        cur.execute("select * from user where username = '{}'".format(username))
        data = cur.fetchone()
        cur.close()
        if data:
            flash('Username Not avilable','danger')
            return redirect('/create-account')

        cur = mysql.connection.cursor()
        cur.execute("insert into user(Name, Email, Password, Username) values(%s,%s,%s,%s)",(name, email, pw_hash, username))
        mysql.connection.commit()
        cur.execute("select Uid from user where Username = '{}'".format(username))
        uid = cur.fetchone()
        session['user'] = uid
        cur.close()
        return redirect('/')
    return render_template(
        'CreateAccount.html'
    )

@app.route('/clothing')
def clothings():
    return render_template('Clothing.html',results=[{'title':'Check out are new skirts','price':'1552','image':'/static/whatsNew1.jpeg','active':'True'},{'title':'Check out are new skirts','price':'12','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'}])


@app.route('/login', methods=['GET','POST'])
def login():
    if "user" in session:
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("select * from user where username = '{}'".format(username))
        data = cur.fetchone()
        if data:
            if bcrypt.check_password_hash(data['Password'], password):
                session['user'] = data['Uid']
                return redirect('/')
            else:
                flash('Wrong password or username', 'danger')
                return redirect('/login')
        else:
            flash("User not found", 'danger')
            return redirect('/login')


    return render_template('Login.html')

@app.route('/cloth')
def cloth():
    return render_template('Clothpage.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True, host= '0.0.0.0')