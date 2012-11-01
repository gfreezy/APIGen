import os
from flask import Flask


app = Flask(__name__)


if 'SERVER_SOFTWARE' in os.environ:
    import sae.const
    from flaskext.sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (
        sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST,
        sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 10
    app.debug = False

else:
    from flask.ext.sqlalchemy import SQLAlchemy

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.debug = True

app.secret_key = 'a46bf773e4f315377d65ba1b3fe36a02'
db = SQLAlchemy(app)


@app.before_request
def before_request(req):
    db.session.close()
    return req


import views
