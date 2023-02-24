"""
psutil可以用来测试CPU和内存利用率
"""
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


def func2():
    a = [i ** 2 for i in range(1000000)]
    return sum(a)


def main():
    """
    执行结果：
    CPU平均使用率：21.54%
    内存平均使用率：58.919999999999995%
    运行时间：14.564秒
    """
    start_time = time.time()
    cpu_percent_list = []
    mem_percent_list = []
    for _ in range(10):
        # 获取CPU使用率
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_percent_list.append(cpu_percent)
        # 获取内存使用率
        mem_percent = psutil.virtual_memory().percent
        mem_percent_list.append(mem_percent)

        # 执行测试函数
        func2()

    end_time = time.time()

    # 计算CPU和内存使用率平均值
    cpu_percent_avg = sum(cpu_percent_list) / len(cpu_percent_list)
    mem_percent_avg = sum(mem_percent_list) / len(mem_percent_list)

    # 输出测试结果
    print(f"CPU平均使用率：{cpu_percent_avg}%")
    print(f"内存平均使用率：{mem_percent_avg}%")
    print(f"运行时间：{end_time - start_time:.3f}秒")


if __name__ == '__main__':
    main()
