"""
docs:
Documentation: https://fastapi.tiangolo.com
Source Code: https://github.com/tiangolo/fastapi

install:
pip install fastapi
pip install "uvicorn[standard]"

run:
uvicorn main:app --reload
"""

import asyncio
import aiofiles
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get('/sleep')
async def sleep():
    await asyncio.sleep(3)
    return 'Hello fastapi sleep!'


@app.get('/io-bound')
async def io_bound():
    async with aiofiles.open('/Users/qhkjit/Develop/algorithm/python/resource/test-io-read.txt') as fp:
        text = await fp.read()
    return f'Hello fastapi io bound, file length: {len(text)}!'


@app.get('/cpu-bound')
async def cpu_bound():
    s = 0
    for i in range(50000000):
        s += i
    return f'Hello faster api cpu bound, total sum is: {s}'
