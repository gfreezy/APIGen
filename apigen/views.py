#!/usr/bin/env python
#coding: utf8
from flask import request, render_template, redirect
from apigen import app


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_post():
    return 'ok'
    # return render_template('create.html')


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
