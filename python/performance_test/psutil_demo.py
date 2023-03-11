"""
psutil可以用来测试CPU和内存利用率
"""
import os
import psutil
import time
import gc

from typing import Callable


def func():
    # 获取CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU使用率：{cpu_percent}%")

    # 获取内存使用情况
    mem_info = psutil.virtual_memory()
    mem_total = mem_info.total
    mem_used = mem_info.used
    mem_percent = mem_info.percent
    print(f"总内存：{mem_total}字节")
    print(f"已用内存：{mem_used}字节")
    print(f"内存使用率：{mem_percent}%")


def sum_iterator():
    return sum([i for i in range(100000000)])


def sum_generator():
    return sum(i for i in range(100000000))


def profile_func(run_count: int = 1):
    def get_memory_uss():
        pid = os.getpid()
        process = psutil.Process(pid)
        memory_info = process.memory_full_info()
        memory = memory_info.uss / 1024. / 1024
        return memory

    def wrapper(f: Callable, *args, **kwargs):
        func_name = f.__name__
        start_time = time.time()
        cpu_percents = []
        mem_percents = []
        memory_uses = []
        for _ in range(run_count):
            # 获取CPU使用率
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_percents.append(cpu_percent)
            # 获取内存使用率
            mem_percent = psutil.virtual_memory().percent
            mem_percents.append(mem_percent)
            # 获取内存使用情况
            memory_used = psutil.Process(os.getpid()).memory_full_info().uss / 1024. / 1024
            memory_uses.append(memory_used)
            # 执行测试函数
            before_used = get_memory_uss()
            f(*args, **kwargs)
            after_used = get_memory_uss()
            memory_used = after_used - before_used
            memory_uses.append(memory_used)

        end_time = time.time()
        # 计算CPU和内存使用率平均值
        cpu_percent_avg = sum(cpu_percents) / run_count
        mem_percent_avg = sum(mem_percents) / run_count
        mem_use_avg = sum(memory_uses) / run_count
        # 输出测试结果
        print(f"函数[{func_name}]CPU平均使用率：{cpu_percent_avg:.2f}%")
        print(f"函数[{func_name}]内存平均使用率：{mem_percent_avg:.2f}%")
        print(f"函数[{func_name}]内存平均使用量：{mem_use_avg:.3f}MB")
        print(f"函数[{func_name}]平均运行时间：{(end_time - start_time) / run_count:.3f}秒")

    return wrapper


def main():
    test_count = 2
    profile_func(test_count)(sum_iterator)
    print("-" * 50)
    gc.freeze()
    profile_func(test_count)(sum_generator)


if __name__ == '__main__':
    main()
