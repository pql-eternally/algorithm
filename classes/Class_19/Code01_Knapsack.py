"""
给定两个长度都为N的数组weights和values，weights[i]和values[i]分别代表 i号物品的重量和价值
给定一个正数bag，表示一个载重bag的袋子，装的物品不能超过这个重量
返回能装下的最大价值
"""
from typing import List


def get_bag_max_value1(weights: List[int], values: List[int], rest_bag: int):
    return process1(weights, values, 0, rest_bag)


def process1(weights: List[int], values: List[int], i: int, rest_bag: int):
    """
    求最大的背包价值
    @param weights: 重量
    @param values: 价值
    @param i: 当前决策的位置，前面都已经决策过了，只需要考虑从i到N位置
    @param rest_bag: 背包剩余的重量
    @return:
    """
    if rest_bag < 0:
        return -1
    if i == len(weights):
        return 0
    # 没有选择i号货物
    p1 = process1(weights, values, i + 1, rest_bag)
    # 选择i号货物
    p2 = process1(weights, values, i + 1, rest_bag - weights[i])
    if p2 != - 1:
        p2 += values[i]
    return max(p1, p2)


def get_bag_max_value2(weights: List[int], values: List[int], bag: int):
    dp = [[-1] * (bag + 1) for _ in range(len(weights) + 1)]
    res = process2(weights, values, 0, bag, dp)
    for _ in dp:
        print(_)
    print('==' * 10)
    return res


def process2(weights: List[int], values: List[int], i: int, rest_bag: int, dp: List[List[int]]):
    """
    缓存记忆
    FIXME：有bug
    """
    if dp[i][rest_bag] != -1:
        return dp[i][rest_bag]
    if rest_bag < 0:
        res = -1
    elif i == len(weights):
        res = 0
    else:
        # 没有选择i号货物
        p1 = process2(weights, values, i + 1, rest_bag, dp)
        # 选择i号货物
        p2 = process2(weights, values, i + 1, rest_bag - weights[i], dp)
        if p2 != - 1:
            p2 += values[i]
        res = max(p1, p2)
    dp[i][rest_bag] = res
    return res


def get_bag_max_value3(weights: List[int], values: List[int], bag: int):
    row = len(weights) + 1
    col = bag + 1
    dp = [[0] * col for _ in range(row)]
    # 行从倒数
    for j in range(0, col):
        for i in range(len(weights) - 1, -1, -1):
            p1 = dp[i + 1][j]
            p2 = 0
            if j >= weights[i]:
                p2 = dp[i + 1][j - weights[i]] + values[i]
            dp[i][j] = max(p1, p2)
    for _ in dp:
        print(_)
    return dp[0][bag]


def main():
    weights = [5, 3, 4, 3, 2, 1]
    values = [3, 6, 5, 9, 2, 1]
    bag = 3
    res1 = get_bag_max_value1(weights, values, bag)
    res2 = get_bag_max_value2(weights, values, bag)
    res3 = get_bag_max_value3(weights, values, bag)
    print(res1)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
