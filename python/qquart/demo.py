from quart import Quart

app = Quart(__name__)


@app.route('/')
async def hello():
    return 'hello'


@app.route("/api")
async def json():
    return {"hello": "world"}


if __name__ == '__main__':
    app.run()
