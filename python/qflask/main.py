import time
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello flask index!'


@app.route('/sleep')
def sleep():
    time.sleep(1)
    return 'Hello flask sleep!'


app.run(port=5000, debug=True)
