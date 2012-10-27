#!/usr/bin/env python
#coding: utf8
from flask import request, render_template, redirect
from apigen import app, db
from apigen.models.get_request import GetRequest


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_post():
    method = request.form['method']
    params = request.form['params']
    resp = request.form['resp']
    if (method and params and resp):
        request_instance = GetRequest(method=method, params=params, resp=resp)
        db.session.add(request_instance)
        db.session.commit()
    return redirect('/')


@app.route('/')
def home():
    grs = db.session.query(GetRequest)
    return render_template('home.html', all_services=grs)


@app.route('/service/<apigen_id>')
def apigen(apigen_id=None):
    gr = apigen_id and db.session.query(GetRequest).filter(GetRequest.id == apigen_id).one()
    return "%s %s %s " % (gr.method, gr.resp, gr.params)
