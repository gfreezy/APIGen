# import sae.const
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.secret_key = 'a46bf773e4f315377d65ba1b3fe36a02'
db = SQLAlchemy(app)
app.debug = True

import views
