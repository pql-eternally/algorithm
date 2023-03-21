import time
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'Hello flask index!'


@app.route('/sleep')
def sleep():
    time.sleep(3)
    return 'Hello flask sleep!'


@app.route('/io-bound')
def io_bound():
    with open('/Users/qhkjit/Develop/algorithm/python/resource/test-io-read.txt', 'r') as f:
        text = f.read()
    return f'Hello flask io bound, file length: {len(text)}!'


@app.route('/cpu-bound')
def cpu_bound():
    s = 0
    for i in range(50000000):
        s += i
    return f'Hello flask cpu bound, total sum is: {s}'


app.run(port=5000, debug=True)
