"""
请同学们自行搜索或者想象一个象棋的棋盘，
然后把整个棋盘放入第一象限，棋盘的最左下角是(0,0)位置
那么整个棋盘就是横坐标上9条线、纵坐标上10条线的区域
给你三个 参数 x，y，k
返回“马”从(0,0)位置出发，必须走k步
最后落在(x,y)上的方法数有多少种?
"""
import time
from typing import List


class Solution:
    def jump(self, x: int, y: int, k: int):
        return self.process(x, y, 0, 0, k)

    def process(self, x: int, y: int, pos_x: int, pos_y: int, rest_step: int):
        """
        @param x:
        @param y:
        @param pos_x: 当前x坐标位置
        @param pos_y: 当前y坐标位置
        @param rest_step: 剩余步数
        @return:
        """
        # 象棋 x轴：0 - 8, y轴：0 - 9
        if pos_x < 0 or pos_x > 8 or pos_y < 0 or pos_y > 9:
            return 0
        if rest_step == 0:
            if x == pos_x and y == pos_y:
                return 1
            return 0
        ways = 0
        ways += self.process(x, y, pos_x + 1, pos_y + 2, rest_step - 1)
        ways += self.process(x, y, pos_x + 2, pos_y + 1, rest_step - 1)
        ways += self.process(x, y, pos_x + 1, pos_y - 2, rest_step - 1)
        ways += self.process(x, y, pos_x + 2, pos_y - 1, rest_step - 1)
        ways += self.process(x, y, pos_x - 1, pos_y + 2, rest_step - 1)
        ways += self.process(x, y, pos_x - 2, pos_y + 1, rest_step - 1)
        ways += self.process(x, y, pos_x - 1, pos_y - 2, rest_step - 1)
        ways += self.process(x, y, pos_x - 2, pos_y - 1, rest_step - 1)
        return ways


class Solution2:
    def jump(self, x: int, y: int, k: int):
        X = 9
        Y = 10
        Z = k + 1
        dp = [[[0] * Z for _ in range(Y)] for _ in range(X)]
        dp[x][y][0] = 1
        for z in range(1, Z):
            for x in range(0, X):
                for y in range(0, Y):
                    dp[x][y][z] = self.pick(dp, x + 1, y + 2, z - 1) + self.pick(dp, x + 2, y + 1, z - 1) + \
                                  self.pick(dp, x + 1, y - 2, z - 1) + self.pick(dp, x + 2, y - 1, z - 1) + \
                                  self.pick(dp, x - 1, y + 2, z - 1) + self.pick(dp, x - 2, y + 1, z - 1) + \
                                  self.pick(dp, x - 1, y - 2, z - 1) + self.pick(dp, x - 2, y - 1, z - 1)
        return dp[0][0][k]

    def pick(self, dp: List[List[List[int]]], x: int, y: int, z: int):
        if x < 0 or x > 8 or y < 0 or y > 9:
            return 0
        return dp[x][y][z]


def main():
    x = 4
    y = 1
    k = 9

    t1 = time.time()
    solution = Solution()
    res = solution.jump(x, y, k)
    t2 = time.time()
    print(f'{t2 - t1}s', res)

    solution2 = Solution2()
    res2 = solution2.jump(x, y, k)
    t3 = time.time()
    print(f'{t3 - t2}s', res2)


if __name__ == '__main__':
    main()
