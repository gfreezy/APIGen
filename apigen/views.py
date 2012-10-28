#!/usr/bin/env python
#coding: utf8
from flask import request, render_template,\
    redirect, abort, url_for, flash
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
            flash('params not allowed')
            return redirect(url_for('create'))
        request_instance = GetRequest(lang=lang, params=json.dumps(dump_result), resp=resp)
        db.session.add(request_instance)
        db.session.commit()
        flash('gen succeeded')
        return redirect(url_for('success', id=request_instance.id))
    flash('query empty')
    return redirect(url_for('create'))


@app.route('/service/<id>/success')
def success(id):
    return render_template('success.html', id=id)


@app.route('/')
def home():
    grs = db.session.query(GetRequest)
    return render_template('home.html', all_services=grs)


@app.route('/service/<apigen_id>')
def apigen(apigen_id=None):
    gr = apigen_id and GetRequest.query.get(apigen_id)
    if not gr:
        abort(404)
    params = json.loads(gr.params)
    result = change_dict(params, request.args)
    resp = gr.resp
    if gr.lang == 'mako':
        resp = '<%!from apigen.template_module import get_pic, get_words, get_random%>'+resp
    try:
        return render_args(gr.lang, resp, result)
    except TypeError:
        return render_template('not_enough_params.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
