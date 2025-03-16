from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save_data', methods=['GET'])
def save_data():
    usn = request.args['usn']
    name= request.args['name']
    dm = request.args['dm']
    sds = request.args['sds']
    cc = request.args['cc']
    ai = request.args['ai']
    print(usn,name,dm,sds,cc,ai)
    
    return redirect(url_for('home'))

app.run()