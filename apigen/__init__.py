#coding: utf8
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment, Bundle


app = Flask(__name__)

if 'SERVER_SOFTWARE' in os.environ:
    import sae.const

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (
        sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST,
        sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    app.debug = True

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.debug = True

app.config['ASSETS_DEBUG'] = app.debug
app.secret_key = 'a46bf773e4f315377d65ba1b3fe36a02'
db = SQLAlchemy(app)

assets = Environment(app)
js_base = Bundle(
    'js/jquery.min.js', 'js/bootstrap.min.js',
    filters='jsmin', output='js/base.js')
js_create = Bundle(
    'js/tab.js', 'js/json2.js', 'js/create.js',
    filters='jsmin', output='js/create_page.js')
css_base = Bundle(
    'css/bootstrap.min.css', 'css/layout.css',
    filters='cssmin', output='css/base.css')
css_index = Bundle('css/index.css',
    filters='cssmin', output='css/index_page.css')
css_create = Bundle('css/create.css',
    filters='cssmin', output='css/create_page.css')
css_success = Bundle('css/success.css',
    filters='cssmin', output='css/success_page.css')

assets.register('js_base', js_base)
assets.register('js_create', js_create)
assets.register('css_base', css_base)
assets.register('css_index', css_index)
assets.register('css_create', css_create)
assets.register('css_success', css_success)


@app.after_request
def after_request(req):
    db.session.close()
    return req


import views
