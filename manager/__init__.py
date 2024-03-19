import os
from flask import Flask

# create and configure the application
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'development',
        DATABASE = os.path.join(app.instance_path, 'manager.sqlite'),
    )

    # load the instance config, if it exist when not testing
    if test_config is None:
        app.config.from_pyfile('config.py', silent= True)
    else:
        app.config.from_mapping(test_config)
    #
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A test page that says Hello
    @app.route('/hello')
    def hello():
        return 'Hello. Welcome'

    return app