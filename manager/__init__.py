import os
from flask import Flask

# create and configure the application
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'development',
        DATABASE = os.path.join(app.instance_path, 'manager.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exist when not testing
        app.config.from_pyfile('config.py', silent= True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # intialize  the application
    from manager import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
   
    return app