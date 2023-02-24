"""
line_profiler可以用来分析代码的行执行时间
kernprof -lv profile_demo.py
"""
import cProfile


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
cProfile.run('list(PrimeIter(10000))')
