#!/usr/bin/env python
#coding: utf8
from flask import request, render_template,\
    redirect, abort
from apigen import app, db
from apigen.models.get_request import GetRequest
from apigen.util import dump_dict, change_dict,\
    render_args
import json


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create_post():
    lang = request.form['lang']
    params = request.form['params']
    resp = request.form['resp']
    if (params and resp and lang):
        dump_result = dump_dict(params)
        if not dump_result:
            return redirect('/')
        request_instance = GetRequest(lang=lang, params=json.dumps(dump_result), resp=resp)
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
    return render_args('jinja', gr.resp, result)

@app.errorhandler(461)
def page_not_found(error):
    return render_template('461.html'), 461

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
