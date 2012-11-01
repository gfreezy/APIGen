import os
import sys
import sae

app_root = os.path.dirname(__file__)

# 两者取其一
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))


from apigen import app

application = sae.create_wsgi_app(app)
