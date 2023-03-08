"""
psutil可以用来测试CPU和内存利用率
"""
import os
import psutil
import time


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


def gen_iterator():
    return [i for i in range(100000000)]


def gen_generator():
    return (i for i in range(100000000))


def profile_func(f):
    """
    执行结果：
    CPU平均使用率：21.54%
    内存平均使用率：58.919999999999995%
    运行时间：14.564秒
    """
    start_time = time.time()
    cpu_percent_list = []
    mem_percent_list = []
    for _ in range(1):
        # 获取CPU使用率
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_percent_list.append(cpu_percent)
        # 获取内存使用率
        mem_percent = psutil.virtual_memory().percent
        mem_percent_list.append(mem_percent)

        # 执行测试函数
        func_name = f.__name__
        show_memory_info(f"before fn<{func_name}> call")
        arr = f()
        show_memory_info(f"after fn<{func_name}> call")
        print(sum(arr))
        del arr
        show_memory_info(f"end fn<{func_name}> call")

    end_time = time.time()

    # 计算CPU和内存使用率平均值
    cpu_percent_avg = sum(cpu_percent_list) / len(cpu_percent_list)
    mem_percent_avg = sum(mem_percent_list) / len(mem_percent_list)

    # 输出测试结果
    print(f"CPU平均使用率：{cpu_percent_avg}%")
    print(f"内存平均使用率：{mem_percent_avg}%")
    print(f"运行时间：{end_time - start_time:.3f}秒")


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print(f'{hint} memory used: {memory} MB')


def main():
    profile_func(gen_iterator)
    print("-" * 50)
    profile_func(gen_generator)


if __name__ == '__main__':
    main()
