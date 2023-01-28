"""
一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这种数
一个数组中有两种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这两种数
"""
import random


def find_once_odd_num(arr: list) -> int:
    """
    依据：0 ^ num = num
         num ^ num = 0
    """
    res = 0
    for num in arr:
        res ^= num
    return res


def find_twice_odd_num(arr: list) -> tuple:
    """
    任何数和这个数的相反数与的结果可以找到最右侧的1
    """
    # 将所有的数异或，可以得到出现奇数的那两个数字异或的结果
    res = 0
    for num in arr:
        res ^= num
    # 找到该值二进制位中随便一位1，比如找最右侧一个1
    flag = res & -res
    # 将arr中数&上面结果，可以将arr中数分成两类，这样可以找到其中一个数值
    res1 = 0
    for num in arr:
        if (num & flag) == 0:
            res1 ^= num
    # 两个数字异或的结果和其中一个数字异或求得另一个数字
    res2 = res ^ res1
    return res1, res2


def random_generator_arr(odd_count: int) -> list:
    arr = []
    count = 0
    while count < odd_count:
        num = random.randint(0, 100)
        if num in arr:
            continue
        # 随机产生奇数
        num_count = random.randrange(1, 10, 2)
        arr.extend([num] * num_count)
        count += 1

    while len(arr) < 100:
        num = random.randint(0, 100)
        if num in arr:
            continue
        # 随机产生偶然
        num_count = random.randrange(2, 10, 2)
        arr.extend([num] * num_count)
    # random.shuffle(arr)
    return arr


def test_once_odd_num() -> None:
    """
    随机生成一个列表，使得某个数出现奇数次，其余数出现偶数次
    """
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = random_generator_arr(1)
        num = find_once_odd_num(arr)
        count = arr.count(num)
        if count % 2 != 1:
            print(f'arr: {arr}， num: {num}， count: {count}')
            return
    print('Done ...')


def test_twice_odd_num() -> None:
    """
    随机生成一个列表，使得某两个数出现奇数次，其余数出现偶数次
    """
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = random_generator_arr(2)
        res1, res2 = find_twice_odd_num(arr)
        count1 = arr.count(res1)
        count2 = arr.count(res2)
        if (count1 % 2 != 1) | (count2 % 2 != 1):
            print(f'arr: {arr}， res1: {res1}， res2: {res2}')
            return
    print('Done ...')


def main():
    # test_once_odd_num()
    test_twice_odd_num()


if __name__ == '__main__':
    main()
