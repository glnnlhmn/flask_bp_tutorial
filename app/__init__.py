from flask import Flask
from example_blueprint import example_blueprint

__author__ = 'Glenn Lehman'
__credits__ = ['Glenn Lehman']
__license__ = '{license}'
__version__ = '0.0.001'
__maintainer__ = 'Glenn Lehman'
__email__ = 'glnn.lhmn@gmail.com}'
__status__ = 'prerelease'


def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_blueprint)

    return app
