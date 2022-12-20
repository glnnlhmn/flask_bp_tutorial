# from app import create_app
#
#
# app = create_app()

from flask import Flask

__author__ = 'Glenn Lehman'
__credits__ = ['Glenn Lehman']
__license__ = '{license}'
__version__ = '0.0.001'
__maintainer__ = 'Glenn Lehman'
__email__ = 'glnn.lhmn@gmail.com}'
__status__ = 'prerelease'


app = Flask(__name__)

@app.route('/')
def index():
    return "This is an example app"