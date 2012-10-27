from flask import Flask, request, render_template, redirect
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.debug = True


@app.route('/edit/<service_id>')
def edit(service_id):
    #eit a exist apigen
    return render_template('edit.html', parameters=[1, 2, 3, 4], responses=[1, 2, 3], service_id=service_id)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form['gen'] == 'init':
        #get apigen id, init, redirect
        genid = 1
        return redirect('/edit/%s' % genid)
        #list all services_ids and show create button
    return render_template('home.html', all_services=[1, 2, 3, 4])


@app.route('/service/<apigen_id>')
def apigen(apigen_id=None):
    #return the response
    return apigen_id
