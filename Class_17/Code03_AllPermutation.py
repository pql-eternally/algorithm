"""
打印一个字符串的全部排列
打印一个字符串的全部排列，要求不要出现重复的排列

全排列：是每个字符必须选但是可位置不同

例如： abc的全排列
abc acb
bac bca
cab aba
"""
from typing import List, Set


def permutation(word: str):
    chars = list(word)
    res = []
    process(chars, '', res)
    return res


def process(chars: List, path: str, res: List):
    """
    @param chars: 剩余的字符列表
    @param path: 之前选择的字符组成的字符串
    @param res: 存放拼接好的结果
    """
    if not chars:
        res.append(path)
        return
    for i in range(len(chars)):
        c = chars.pop(i)
        process(chars, path + c, res)
        chars.insert(i, c)


def permutation2(word: str):
    """
    字符串的全部排列，要求不要出现重复的排列
    """
    chars = list(word)
    res = set()
    process2(chars, 0, res)
    return list(res)


def process2(chars: List, index: int, res: Set):
    if index == len(chars):
        res.add(''.join(chars))
        return
    for i in range(index, len(chars)):
        swap(chars, index, i)
        process2(chars, index + 1, res)
        swap(chars, index, i)


def permutation3(word: str):
    """
    字符串的全部排列，要求不要出现重复的排列
    不使用集合实现
    """
    chars = list(word)
    res = []
    process3(chars, 0, res)
    return list(res)


def process3(chars: List, index: int, res: List):
    if index == len(chars):
        res.append(''.join(chars))
        return
    visitor_chars = set()
    for i in range(index, len(chars)):
        c = chars[i]
        if c in visitor_chars:
            continue
        visitor_chars.add(c)
        swap(chars, index, i)
        process3(chars, index + 1, res)
        swap(chars, index, i)


def swap(chars: List, i: int, j: int):
    chars[i], chars[j] = chars[j], chars[i]


def main():
    word = 'abcc'
    res = permutation(word)
    res2 = permutation2(word)
    res2.sort()
    res3 = permutation3(word)
    res3.sort()
    print(res)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
