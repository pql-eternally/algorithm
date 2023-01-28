"""
假设有排成一行的N个位置记为1~N，N一定大于或等于2
开始时机器人在其中的M位置上(M一定是1~N中的一个)
如果机器人来到1位置，那么下一步只能往右来到2位置；
如果机器人来到N位置，那么下一步只能往左来到N-1位置；
如果机器人来到中间位置，那么下一步可以往左走或者往右走；
规定机器人必须走K步，最终能来到P位置(P也是1~N中的一个)的方法有多少种
给定四个参数 N、M、K、P，返回方法数
"""
from typing import List


def robot_walk(total_pos: int, cur_pos: int, target_pos: int, step: int):
    """
    @param total_pos: 总共的位置数，1-n
    @param cur_pos: 当前机器人所在的位置
    @param target_pos: 目标位置
    @param step: 机器人走的步数
    """
    if step == 0:
        return 1 if cur_pos == target_pos else 0
    if cur_pos == 1:
        return robot_walk(total_pos, 2, target_pos, step - 1)
    if cur_pos == total_pos:
        return robot_walk(total_pos, total_pos - 1, target_pos, step - 1)
    left = robot_walk(total_pos, cur_pos - 1, target_pos, step - 1)
    right = robot_walk(total_pos, cur_pos + 1, target_pos, step - 1)
    return left + right


def process2(total_pos: int, cur_pos: int, target_pos: int, step: int, res_cache: List):
    res = res_cache[cur_pos][step]
    if res != -1:
        return res
    # 缓冲结果值
    if step == 0:
        res = 1 if cur_pos == target_pos else 0
    elif cur_pos == 1:
        res = process2(total_pos, 2, target_pos, step - 1, res_cache)
    elif cur_pos == total_pos:
        res = process2(total_pos, cur_pos - 1, target_pos, step - 1, res_cache)
    else:
        left = process2(total_pos, cur_pos - 1, target_pos, step - 1, res_cache)
        right = process2(total_pos, cur_pos + 1, target_pos, step - 1, res_cache)
        res = left + right
    res_cache[cur_pos][step] = res
    return res


def robot_walk2(total_pos: int, cur_pos: int, target_pos: int, step: int):
    """
    通过分析发现有大量重复结果，所以增加递归记忆法
    cur_pos: 1 --> n
    target_pos: 1 --> n
    准备一个二维数组缓存结果
    """
    res_cache = [[-1] * (step + 1) for _ in range(total_pos + 1)]
    return process2(total_pos, cur_pos, target_pos, step, res_cache)


def robot_walk_dp(total_pos: int, cur_pos: int, target_pos: int, step: int):
    """
    动态规划
    """
    row = total_pos + 1
    col = step + 1
    dp = [[0] * col for _ in range(row)]
    # step = 0
    for row_index in range(row):
        if row_index == target_pos:
            dp[row_index][0] = 1
    # col: 1 -> step
    for col_index in range(1, col):
        for row_index in range(1, row):
            if row_index == 1:
                dp[row_index][col_index] = dp[row_index + 1][col_index - 1]
            elif row_index == total_pos:
                dp[row_index][col_index] = dp[row_index - 1][col_index - 1]
            else:
                dp[row_index][col_index] = dp[row_index - 1][col_index - 1] + dp[row_index + 1][col_index - 1]
    return dp[cur_pos][step]


def main():
    n = 6
    cur = 2
    pos = 4
    step = 6
    res1 = robot_walk(n, cur, pos, step)
    res2 = robot_walk2(n, cur, pos, step)
    res3 = robot_walk_dp(n, cur, pos, step)
    print(res1)
    print(res2)
    print(res3)
    assert res1 == res2 == res3


if __name__ == '__main__':
    main()
