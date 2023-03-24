import random
import cProfile
import pstats

from functools import wraps


def monitor_exception():
    if random.randint(0, 1) == 0:
        raise Exception('模拟异常')


def profile_measure(sort: str = 'time', mount: int = 10):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            res = f(*args, **kwargs)
            pr.disable()
            pstats.Stats(pr).strip_dirs().sort_stats(sort).print_stats(mount)
            return res

        return decorated

    return wrapper


def async_profile_measure(sort: str = 'time', mount: int = 10):
    def wrapper(f):
        @wraps(f)
        async def decorated(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            res = await f(*args, **kwargs)
            pr.disable()
            pstats.Stats(pr).strip_dirs().sort_stats(sort).print_stats(mount)
            return res

        return decorated

    return wrapper
