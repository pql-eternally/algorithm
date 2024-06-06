import asyncio
import time

from flask import Flask

app = Flask(__name__)


@app.route('/sync')
def sync_fn():
    start_time = time.time()
    # 模拟同步操作，这里使用time.sleep()暂停1秒钟
    time.sleep(2)
    end_time = time.time()
    return f"Sync request processed in {end_time - start_time} seconds"


@app.route('/async')
async def async_fn():
    start_time = time.time()
    # 模拟异步操作，这里使用asyncio.sleep()暂停1秒钟
    await asyncio.sleep(2)
    end_time = time.time()
    return f"Async request processed in {end_time - start_time} seconds"


if __name__ == '__main__':
    app.run()
