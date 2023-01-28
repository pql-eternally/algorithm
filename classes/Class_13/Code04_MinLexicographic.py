"""
给定一个由字符串组成的数组strs，必须把所有的字符串拼接起来，返回所有可能的拼接结果中字典序最小的结果

使用贪心算法
贪心算法不用证明，使用对数器暴力验证
"""
import random
import operator


def sort_by_ascii(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if operator.lt(arr[i] + arr[j - 1], arr[j - 1] + arr[i]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


def lowest_str(arr: list) -> str:
    """
    贪心算法，不能单纯的比较a，b，排序比较：a + b 与 b + a
    """
    sort_by_ascii(arr)
    return ''.join(arr)


def generate_random_str(str_len: int) -> str:
    words = []
    str_len = random.randint(1, str_len)
    for i in range(str_len):
        word = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        words.append(word)
    return ''.join(words)


def generate_random_str_arr(arr_len: int, str_len: int) -> list:
    arr = []
    arr_len = random.randint(1, arr_len)
    for i in range(arr_len):
        arr.append(generate_random_str(str_len))
    return arr


def main():
    arr = generate_random_str_arr(10, 5)
    print(arr)
    s = lowest_str(arr)
    print(s)


if __name__ == '__main__':
    main()
