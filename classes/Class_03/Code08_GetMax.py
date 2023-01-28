"""
用递归行为得到数组中的最大值，并用master公式来估计时间复杂度
"""
import random


def random_generator_arr(k: int, m: int, count: int = 100) -> list:
    """
    随机生成列表
    """
    k_num = random.randint(0, 100)
    arr = []
    arr.extend([k_num] * k)
    while len(arr) < count:
        m_num = random.randint(0, 100)
        if m_num in arr:
            continue
        arr.extend([m_num] * m)
    random.shuffle(arr)
    return arr


def get_max(arr: list) -> int:
    """
    评估时间复杂度：根据master公式可以列出
    T(N) = aT(N/b) + O(N^d)
    log(b, a) > d   ==>  O(N^log(b, a))
    log(b, a) < d   ==>  O(N^d)
    log(b, a) = d   ==>  O(N^d * logN)
    每次递归中，可以解决N/2个问题，并且需要两次，然后需要一次求两个数最大值
    所以：T(N) = 2T(N/2) + O(1) ==> a=2 b=2 d=0
    log(b, a) = 1 > d  ==> O(N^log(b, a)) ==> O(N)
    """
    return process(arr, 0, len(arr) - 1)


def process(arr: list, left: int, right: int) -> int:
    # L...R上只有一个数
    if left == right:
        return arr[left]
    # L...R上有多个数
    mid = left + ((right - left) >> 1)
    left_max = process(arr, left, mid)
    right_max = process(arr, mid + 1, right)
    return max(left_max, right_max)


def comparator(arr: list) -> int:
    if not arr:
        return -1
    m = arr[0]
    for num in arr:
        if num > m:
            m = num
    return m


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        k = random.randint(2, 5)
        m = max(k + 1, random.randint(3, 7))
        arr = random_generator_arr(k, m, 10)
        res1 = get_max(arr)
        res2 = comparator(arr)
        if res1 != res2:
            print(f'arr: {arr}，res1：{res1}，res2：{res2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
