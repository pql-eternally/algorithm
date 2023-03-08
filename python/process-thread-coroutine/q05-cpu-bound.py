import time

from functools import wraps
from threading import Thread


def func_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        f(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'函数{f.__name__}耗时{end_time - start_time}秒')

    return wrapper


@func_time
def count_down(n):
    """
    函数count_down耗时6.437547994秒
    """
    print(f'calc: {n}')
    while n > 0:
        n -= 1


@func_time
def count_down_multi_thread(n):
    """
    函数count_down耗时6.1298445589999995秒
    函数count_down耗时6.218262002秒
    函数count_down_multi_thread耗时6.218644223秒
    """
    t1 = Thread(target=count_down, args=[n // 2])
    t2 = Thread(target=count_down, args=[n // 2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def main():
    n = 100000000
    count_down(n)
    count_down_multi_thread(n)


if __name__ == '__main__':
    main()
