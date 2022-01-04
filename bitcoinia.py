from flask import Flask,flash
from flask import render_template, request, redirect, url_for
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os


app = Flask(__name__)
app.secret_key = 'f3cfe9ed8fae309f02079dbf'

data ="data1o1"
value2 = "datx4i"




app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://esoutvnswrotay:7fdf39aa8481eaaac8f6513de09366f048bddb1504a4f2f696ac8392125bc436@ec2-54-174-43-13.compute-1.amazonaws.com:5432/d5dejr1usnvp2n'

# uri = os.getenv("postgres://postgres://ccfszdwsuuxfzu:434734dd0dcef146d2b7162ea46d9bb53047d74e84b9c5f093cd5763bcc36f61@ec2-174-129-37-144.compute-1.amazonaws.com:5432/d72hfkp6vau80d")
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy(app)



class Bitcoinia(db.Model):
    __tablename__ = 'bitcoinia'
    index = db.Column(db.Numeric, primary_key=True)
    timestamp = db.Column(db.DateTime(), server_default=func.now())
    data = db.Column(db.String(30))
    hash = db.Column(db.String(64), unique=True)
    previoushash = db.Column(db.String(64))
    ilosc = db.Column(db.Numeric)

    def __init__(self, index,data, hash, previoushash, ilosc):
        self.index = index
        # self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.previoushash = previoushash
        self.ilosc = ilosc




@app.route("/")
def hello_world():
    return "Welcome at bItcoInIa !"


@app.route('/1')
def hello(name=None):

    import re
    import string
    import random
    all_chars = string.ascii_letters + string.digits + string.punctuation
    hash_1 = ''.join(random.choices(all_chars, k=54))



    get1 = Bitcoinia.query.order_by(Bitcoinia.index.desc()).first()


    # try:
    get1_hash = get1.hash
    ten = get1_hash[0:10]
    nexthash = ten + hash_1


    get1_index = get1.index
    index2 = int(get1_index)
    index3 = index2 + 1


    get1_data = get1.data
    data1 = get1_data

    data2  = re.findall('\d+', data1)
    data4 = 'block'+ str(int(data2[0])+1) + 'chain'
    # except AttributeError:
    #     data4 ='0'
    #     index3 = '0'
    #     nexthash = '0'
    #     get1_hash='0'

        






    def get_hash():
        get1 = Bitcoinia.query.order_by(Bitcoinia.hash.desc()).first()
        get1_hash = get1.hash
        return get1_hash


    def get_bitcoinia():
        get1 = Bitcoinia.query.order_by(Bitcoinia.timestamp)
        return get1





    return render_template('bitcoinia1.html', index=index3, data=data4, hash=nexthash, previoushash=get1_hash  )








@app.route('/submit', methods=['POST', 'GET'])
def submit():
    
    if request.method == 'POST':
        # form = Bitcoinia_form()
        

        index = request.form['index']
        data = request.form['data']
        previoushash = request.form['previoushash']
        hash = request.form['hash']
        ilosc= request.form['ilosc']


        if not ilosc:
            error_statement = "dane wymagane"
        # if form.validate_on_submit():
            flash('Nie wypełniono pola')
            return redirect(url_for('hello', error_statement=error_statement))
        else:
            datta = Bitcoinia(index,data, hash, previoushash, ilosc)
            db.session.add(datta)
            db.session.commit()

        return redirect(url_for('hello'))

    else:

        return redirect(url_for('hello'))