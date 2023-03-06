"""
python3.5引入async和await关键字，可以简化协程的写法。

yield from 用于生成器和协程之间的委托和协作，可以用于串联多个协程或生成器。await 用于异步函数中等待其他协程或异步操作完成，并获取其结果
yield from 和 await 的区别：
1、yield from 用于在协程之间传递值和控制权，它可以将一个协程委托给另一个协程来执行，直到子协程执行完毕为止。
await 用于等待一个协程执行完毕，然后获取其结果。
2、yield from 可以在生成器中使用，它可以将生成器的执行暂停，并将控制权交给另一个协程或生成器。
await 只能在异步函数中使用，它可以将异步函数的执行暂停，并将控制权交给事件循环，以便它可以执行其他任务。
3、yield from 可以用于串联多个协程或生成器，以实现复杂的协作式异步编程。
await 只能等待一个协程完成，并获取其结果，它通常用于等待 I/O 操作或其他异步操作完成。
4、在 Python 3.7 之前，使用 yield from 实现协程需要使用生成器和协程结合的方式。
而从 Python 3.7 开始，可以使用 async def 和 await 来定义协程，这样可以更加简单和直观地编写异步代码。
"""
import asyncio


async def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1
    print('Lift-off! ({})'.format(number))


# 执行协程的两种方式：
# 1、使用 asyncio.run() 函数
# async def main():
#     print("Running main...")
#     await asyncio.gather(
#         countdown("A", 2),
#         countdown("B", 3),
#     )
#     print("Main finished!")
#
#
# asyncio.run(main())

# 2、使用 asyncio.get_event_loop() 函数
loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

