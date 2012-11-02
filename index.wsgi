import sae

from apigen import app
application = sae.create_wsgi_app(app)
