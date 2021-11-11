from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html', whatsNew=[{'title':'Check out are new skirts','price':'1299','image':'/static/whatsNew1.jpeg','active':'True'},{'active':'False','title':'Check out are new shirts','price':'1099','image':'/static/whatsNew2.jpeg'},{'active':'False','title':'Check out are all new math course','price':'599','image':'/static/whatsNew3.jpeg'}])

app.run(debug=True, host= '0.0.0.0')