"""
窗口内最大值或最小值更新结构的实现
假设一个固定大小为W的窗口，依次划过arr，
返回每一次滑出状况的最大值
例如，arr = [4,3,5,4,3,3,6,7], W = 3
返回：[5,5,5,4,6,7]

滑动窗口遵循的原则：
1、left可以向右滑动
2、right可以向右滑动
3、left不能大于right


"""
import random
from collections import deque
from typing import List


def window_move(arr: List[int], w: int) -> List[int]:
    res = []
    window = deque()
    for index, num in enumerate(arr):
        limit_index = index - w
        # 判断窗口左侧下标是否滑出窗口
        while window and window[0] <= limit_index:
            window.popleft()
        while window and arr[window[-1]] <= num:
            window.pop()
        window.append(index)
        if index + 1 >= w and window:
            res.append(arr[window[0]])
    return res


def get_window_max(arr: List[int], w: int) -> List[int] or None:
    """
    暴力获取最大值
    """
    res = []
    if not arr or w < 1 or len(arr) < w:
        return
    N = len(arr)
    L = 0
    R = w - 1
    while R < N:
        res.append(max(arr[L:R + 1]))
        L += 1
        R += 1
    return res


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = 100) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        w = random.randint(1, len(arr))
        res1 = window_move(arr, w)
        res2 = get_window_max(arr, w)
        assert res1 == res2, (arr, w, res1, res2)
    print('Done ...')


if __name__ == '__main__':
    main()
