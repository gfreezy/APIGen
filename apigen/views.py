#!/usr/bin/env python
#coding: utf8
import json
from urllib import urlencode
from flask import request, render_template, redirect, abort, url_for, flash
from apigen import app, db
from apigen.models.get_request import GetRequest
from apigen.util import check_dict, change_dict, render_args, sample_params, crossdomain
from apigen.const import django_syntax, jinja_syntax, mako_syntax


@app.route('/create')
def create():
    return render_template(
        'create.html',
        django_syntax=django_syntax,
        jinja_syntax=jinja_syntax,
        mako_syntax=mako_syntax)


@app.route('/create', methods=['POST'])
def create_post():
    lang = request.form['lang']
    params = request.form['params']
    resp = request.form['resp']
    if (params and resp and lang):
        check_dict(params)
        if not params:
            flash('params not allowed')
            return redirect(url_for('create'))
        request_instance = GetRequest(lang=lang, params=params, resp=resp)
        db.session.add(request_instance)
        db.session.commit()
        flash('gen succeeded')
        return redirect(url_for('success', id=request_instance.id))
    flash('query empty')
    return redirect(url_for('create'))


@app.route('/service/<id>/success')
def success(id):
    api = GetRequest.query.get(id)
    if not api:
        abort(404)

    sample = sample_params(api.params)
    query = urlencode(sample)

    return render_template('success.html', api=api, query=query)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    grs = db.session.query(GetRequest)
    return render_template('home.html', all_services=grs)


@app.route('/service/<apigen_id>')
@crossdomain('*')
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
        abort(400)


@app.route('/preview')
def preview():
    params = request.args.get("params")
    resp = request.args.get("resp")
    lang = request.args.get("lang")

    sample = sample_params(params)
    try:
        ret = render_args(lang, resp, sample)
    except Exception, e:
        return str(e)

    return ret


@app.route('/')
@app.errorhandler(400)
def not_enough_params(error):
    return render_template('not_enough_params.html'), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
