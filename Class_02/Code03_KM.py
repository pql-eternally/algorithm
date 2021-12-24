"""
一个数组中有一种数出现K次，其他数都出现了M次，已知M > 1，K < M，找到出现了K次的数，要求额外空间复杂度O(1)，时间复杂度O(N)
"""
import random


def find_only_k_times(arr: list, k: int, m: int) -> int:
    """
    总的时间复杂度是：O(N) + O(1)，取最大的即为O(N)
    空间复杂度就开辟了两个变量，所以是O(1)
    """
    # 假设arr中最大值不超过2^31 - 1，我们定义32位存放arr中所有数每个数对应二进制位的和
    bits = [0] * 32
    # a & 1 = 1 ==> a: xxxx...1
    # a & 2 = 2 ==> a: xxx...10
    # a & 4 = 4 ==> a: xx...100
    # 这里就循环固定的32次，是常数次数，相比与arr中数字趋向于无穷大可以忽略不记，所以这里的时间复杂度是O(N)
    for i in range(0, 32):
        bit = 1 << i
        for num in arr:
            if num & bit == bit:
                bits[i] += 1

    k_num = 0
    # 按二进制位出现的次数分别对m取余，如果不为0并且是k则说明出现k次的数字当前位为1（注意：这里时间复杂度是O(1)）
    for i in range(0, 32):
        if (bits[i] % m) == k:
            k_num |= (1 << i)
    return k_num


def comparator(arr: list, k: int) -> int:
    for num in arr:
        if arr.count(num) == k:
            return num
    return -1


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


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        k = random.randint(2, 5)
        m = max(k + 1, random.randint(3, 7))
        arr = random_generator_arr(k, m, 10)
        res1 = find_only_k_times(arr, k, m)
        res2 = comparator(arr, k)
        if res1 != res2:
            print(f'arr: {arr}，res1：{res1}，res2：{res2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
