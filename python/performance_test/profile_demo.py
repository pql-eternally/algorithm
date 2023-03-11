"""
line_profiler可以用来分析代码的行执行时间
kernprof -l profile_demo.py # -l 表示使用line_profiler -v 表示详细信息
python -m line_profiler profile_demo.py.lprof
从 Python 3.7 开始，CPython 提供了一个内置的 C 扩展模块 cProfile，
它可以进行类似 line_profiler 的性能分析。因此，在 Python 3.7 及以上版本中，
您可以使用 cProfile 来进行性能分析，而无需安装任何第三方模块。

测试一下代码总的效率以及各个部分的效率
python -m cProfile profile_demo.py
"""
import functools


def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.current = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()


"""
执行结果
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.002    0.002    0.269    0.269 <string>:1(<module>)
104728    0.223    0.000    0.223    0.000 profile_demo.py:16(is_prime)
    1    0.000    0.000    0.000    0.000 profile_demo.py:25(__init__)
    1    0.000    0.000    0.000    0.000 profile_demo.py:30(__iter__)
10001    0.044    0.000    0.267    0.000 profile_demo.py:33(__next__)
    1    0.000    0.000    0.269    0.269 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def fib(n: int):
    """
     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
4356587/31    1.213    0.000    1.213    0.039 profile_demo.py:55(fib)
     31/1    0.000    0.000    1.214    0.607 profile_demo.py:68(fib_seq)

    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@functools.lru_cache()
def fib_with_cache(n):
    """
     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        31    0.000    0.000    0.000    0.000 profile_demo.py:61(fib_with_cache)
        31/1    0.000    0.000    0.000    0.000 profile_demo.py:68(fib_seq)
    """
    if n <= 2:
        return 1
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)


def fib_with_dp(n):
    """
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 profile_demo.py:79(fib_with_dp)
    """
    if n < 1:
        return 0
    dp = [1, 1]
    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp


def fib_seq(n: int, fib_fn: callable):
    res = []
    if n >= 1:
        res.extend(fib_seq(n - 1, fib_fn))
    res.append(fib_fn(n))
    return res


if __name__ == '__main__':
    """
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
4356587/31    1.178    0.000    1.178    0.038 profile_demo.py:55(fib)
       31    0.000    0.000    0.000    0.000 profile_demo.py:67(fib_with_cache)
        1    0.000    0.000    0.000    0.000 profile_demo.py:79(fib_with_dp)
     62/2    0.000    0.000    1.178    0.589 profile_demo.py:92(fib_seq)
    """
    fib_seq(30, fib)
    fib_seq(30, fib_with_cache)
    fib_with_dp(30)
