"""
给定一个整型数组arr，和一个整数num
某个arr中的子数组sub，如果想达标，必须满足：sub中最大值 – sub中最小值 <= num，
返回arr中达标子数组的数量

子数组必须是连续的
"""
import time
import random
from typing import List
from collections import deque


def sub_arr_num(arr: List[int], target_sum: int) -> int:
    """
    使用滑动窗口统计
    @param arr:
    @param target_sum:
    @return:
    """
    count = 0
    N = len(arr)
    min_window = deque()
    max_window = deque()
    right = 0
    for left, num in enumerate(arr):
        while right < N:
            cur_num = arr[right]
            # 调整小值窗口
            while min_window and cur_num <= arr[min_window[-1]]:
                min_window.pop()
            min_window.append(right)
            # 调整大值窗口
            while max_window and arr[max_window[-1]] <= cur_num:
                max_window.pop()
            max_window.append(right)
            # 校验当前窗口最大值最小值是否满足
            if arr[max_window[0]] - arr[min_window[0]] > target_sum:
                break
            else:
                right += 1
        # 从left到right当前窗口满足条件
        count += (right - left)
        # 调整窗口左侧
        if min_window and min_window[0] == left:
            min_window.popleft()
        if max_window and max_window[0] == left:
            max_window.popleft()
    return count


def sub_arr_num2(arr: List[int], num: int) -> int:
    res = 0
    N = len(arr)
    # 从 0到N 依次获取满足条件到个数
    for left in range(N):
        cur_count = 0
        for right in range(left, N):
            sub_arr = arr[left: right + 1]
            if max(sub_arr) - min(sub_arr) <= num:
                cur_count = len(sub_arr)
            else:
                break
        res += cur_count
    return res


def generate_random_arr(max_size: int = 10, min_value: int = 0, max_value: int = 100) -> List[int]:
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def test_run_time(test_count, arr_max_size=100):
    print('Start ...')
    print('生成测试样本...')
    samples = []
    for i in range(0, test_count):
        arr = generate_random_arr(arr_max_size)
        num = random.randint(10, 50)
        samples.append((arr, num))
    print('生成测试样本完成...')

    print('执行暴力尝试...')
    t1 = time.time()
    for arr, num in samples:
        sub_arr_num(arr, num)
    t2 = time.time()
    print(f'执行暴力尝试完成，用时：{t2 - t1}...')

    print('执行滑动窗口求解...')
    t3 = time.time()
    for arr, num in samples:
        sub_arr_num2(arr, num)
    t4 = time.time()
    print(f'执行滑动窗口完成，用时：{t4 - t3}...')
    print('Done ...')


def main():
    print('Start ...')
    test_count = 0
    for i in range(0, test_count):
        arr = generate_random_arr(50)
        num = random.randint(10, 20)
        res1 = sub_arr_num(arr, num)
        res2 = sub_arr_num2(arr, num)
        assert res1 == res2, (arr, num, res1, res2)
    print('Done ...')

    test_run_time(100000)


if __name__ == '__main__':
    main()
