#!/usr/bin/env python
#coding: utf8
from flask import request, render_template,\
    redirect, abort
from apigen import app, db
from apigen.models.get_request import GetRequest
from jinja2 import Template
from apigen.util import dump_dict, change_dict
import json


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_post():
    params = request.form['params']
    resp = request.form['resp']
    if (params and resp):
        dump_result = dump_dict(params)
        if not dump_result:
            return redirect('/')
        request_instance = GetRequest(params=json.dumps(dump_result), resp=resp)
        db.session.add(request_instance)
        db.session.commit()
    return redirect('/')


@app.route('/')
def home():
    grs = db.session.query(GetRequest)
    return render_template('home.html', all_services=grs)


@app.route('/service/<apigen_id>')
def apigen(apigen_id=None):
    gr = apigen_id and db.session.query(GetRequest).get(apigen_id)
    if not gr:
        abort(404)
    params = json.loads(gr.params)
    result = change_dict(params, request.args)
    tem = Template(gr.resp)
    return Template.render(tem, **result)
