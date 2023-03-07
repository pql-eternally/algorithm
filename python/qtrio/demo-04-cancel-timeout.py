import trio


async def do_http_get(url):
    print(f"starting http get: {url}")
    await trio.sleep(5)
    print("http get finished")
    return 123


async def func1():
    with trio.move_on_after(3):
        result = await do_http_get("https://www.baidu.com")
        print("result is", result)
    print("with block finished")


async def func2():
    print("starting...")
    with trio.move_on_after(5):
        with trio.move_on_after(10):
            await trio.sleep(20)
            print("sleep finished without error")
        print("move_on_after(10) finished without error")
    print("move_on_after(5) finished without error")


async def func3():
    with trio.move_on_after(5) as cancel_scope:
        await trio.sleep(10)
    print(cancel_scope.cancelled_caught)  # prints "True"


trio.run(func3)
