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
    await asyncio.sleep(1)
    return 'Hello fastapi sleep!'
