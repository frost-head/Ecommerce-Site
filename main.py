from logging import error
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html', whatsNew=[{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'active':'False','title':'Check out are all new math course','price':'599','image':'/static/whatsNew3.jpeg'}])

@app.route('/create-account', methods=['GET','POST'])
def createAccount():
    return render_template(
        'CreateAccount.html'
    )


@app.route('/clothing')
def clothings():
    return render_template('Clothing.html',results=[{'title':'Check out are new skirts','price':'1552','image':'/static/whatsNew1.jpeg','active':'True'},{'title':'Check out are new skirts','price':'12','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'}])

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/cloth')
def cloth():
    return render_template('Clothpage.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True, host= '0.0.0.0')