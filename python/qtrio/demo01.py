import trio
import time


async def async_double(x):
    return 2 * x


async def double_sleep(x):
    await trio.sleep(2 * x)
    return await async_double(x)


async def broken_double_sleep(x):
    print("*yawn* Going to sleep")
    start_time = time.perf_counter()

    # Whoops, we forgot the 'await'!
    # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    await trio.sleep(2 * x)

    sleep_time = time.perf_counter() - start_time
    print(f"Woke up after {sleep_time:.2f} seconds, feeling well rested!")


def main():
    # res = trio.run(async_double, 3)
    # print(res)

    # res = trio.run(double_sleep, 1)
    # print(res)

    res = trio.run(broken_double_sleep, 1)
    print(res)


if __name__ == '__main__':
    main()
