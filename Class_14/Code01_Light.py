"""
给定一个字符串str，只由'X'和'.'两种字符构成
'X'表示墙，不能放灯，也不需要点亮；'.'表示居民点，可以放灯，需要点亮
如果灯放在i位置，可以让i-1，i和i+1三个位置被点亮
返回如果点亮str中所有需要点亮的位置，至少需要几盏灯
"""
import random


def min_light(s: str) -> int:
    i = 0
    light = 0
    length = len(s)
    while i < length:
        if s[i] == 'X':
            i += 1
        else:
            light += 1
            if i + 1 == length:
                break
            if s[i + 1] == 'X':
                i = i + 2
            else:
                i = i + 3
    return light


def generator_random_str(str_len: int):
    arr = []
    str_len = random.randint(1, str_len)
    for i in range(str_len):
        if random.random() < 0.2:
            arr.append('X')
        else:
            arr.append('.')
    return ''.join(arr)


def main():
    s = generator_random_str(20)
    res = min_light(s)
    print(s, res)


if __name__ == '__main__':
    main()
