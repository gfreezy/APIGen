from flask.ext.script import Manager
from flask.ext.assets import ManageAssets
from apigen import app

manager = Manager(app)
manager.add_command("assets", ManageAssets())


if __name__ == '__main__':
    manager.run()
