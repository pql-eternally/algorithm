import random


def monitor_exception():
    if random.randint(0, 1) == 0:
        raise Exception('模拟异常')
