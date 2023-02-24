"""
memory_profiler 可以用来监控 Python 程序的内存使用情况
python -m memory_profiler xxx.py
在输出的结果中，我们可以看到每行代码所占用的内存、每个函数调用的内存、每个代码对象（如变量、列表等）所占用的内存等信息。
通过分析这些信息，我们可以找出代码中存在的内存泄漏或内存占用过大的问题，从而进行优化。
"""
from memory_profiler import profile


@profile
def func():
    """
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
         7     16.0 MiB     16.0 MiB           1   @profile
         8                                         def func():
         9     23.7 MiB      7.6 MiB           1       a = [1] * (10 ** 6)
        10    176.3 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
        11     23.7 MiB   -152.6 MiB           1       del b
        12     23.7 MiB      0.0 MiB           1       return a

    """
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    func()
