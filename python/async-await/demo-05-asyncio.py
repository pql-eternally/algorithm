"""
python3.4引入asyncio，
asyncio.coroutine装饰器被用来将一个函数标记为作为协程的函数，该函数用于异步及其事件循环，
不过这个装饰器已经废弃使用了，现在使用async关键字来定义协程函数。

@types.coroutine 是一个类型提示装饰器
@asyncio.coroutine 是一个用于启用生成器协程函数中 yield from 语法的装饰器
"""
import asyncio

import types


# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
@asyncio.coroutine
# @types.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1
    print('Lift-off! ({})'.format(number))


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
