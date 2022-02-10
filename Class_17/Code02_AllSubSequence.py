"""
打印一个字符串的全部子序列
字符串的每一位都是可以选或者不选
"""
from typing import List, Set


def all_subsequence(word: str) -> List:
    chars = list(word)
    res = []
    process(chars, 0, '', res)
    return res


def process(chars: List, index: int, path: str, res: List) -> None:
    """
    @param chars: 字符序列
    @param index: 当前选择的位置
    @param path: 前面选择构造的字符串
    @param res:
    @return:
    """
    if index == len(chars):
        res.append(path)
        return
    # 没有拼接当前位置字符
    process(chars, index + 1, path, res)
    # 拼接了当前位置字符
    process(chars, index + 1, path + chars[index], res)


def all_subsequence_no_repeat(word: str) -> List:
    chars = list(word)
    res_set = set()
    process_no_repeat(chars, 0, '', res_set)
    return list(res_set)


def process_no_repeat(chars: List, index: int, path: str, res: Set) -> None:
    if index == len(chars):
        res.add(path)
        return
    process_no_repeat(chars, index + 1, path, res)
    process_no_repeat(chars, index + 1, path + chars[index], res)


def main():
    words = 'abccc'
    res = all_subsequence(words)
    res2 = all_subsequence_no_repeat(words)
    print(res)
    print('=' * 10)
    print(res2)


if __name__ == '__main__':
    main()
