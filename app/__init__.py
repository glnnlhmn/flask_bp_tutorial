from flask import Flask
from app.main.routes import main

__author__ = 'Glenn Lehman'
__credits__ = ['Glenn Lehman']
__license__ = '{license}'
__version__ = '0.0.001'
__maintainer__ = 'Glenn Lehman'
__email__ = 'glnn.lhmn@gmail.com}'
__status__ = 'prerelease'


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)

    return app
