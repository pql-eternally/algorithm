"""
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
认为值相同的货币没有任何不同，
返回组成aim的方法数
例如：arr = {1,2,1,1,2,1,2}，aim = 4
方法：1+1+1+1、1+1+2、2+2
一共就3种方法，所以返回3
"""
import time
from typing import List


class Solution:
    def get_ways(self, arr: List[int], aim: int):
        # 统计面值及数量数组
        currency_map = {}
        for money in arr:
            count = currency_map.get(money, 0)
            count += 1
            currency_map[money] = count
        moneys, counts = list(currency_map.keys()), list(currency_map.values())
        return self.process(moneys, counts, 0, aim)

    def process(self, moneys: List[int], counts: List[int], index: int, rest: int):
        """
        @param moneys: 货币种类数组
        @param counts: 每种货币数量
        @param index: 考虑从 index ... N
        @param rest: 剩余要组成的数
        @return:
        """
        N = len(moneys)
        if index == N:
            return 1 if rest == 0 else 0
        money = moneys[index]
        count = 0
        ways = 0
        while count <= counts[index] and money * count <= rest:
            ways += self.process(moneys, counts, index + 1, rest - money * count)
            count += 1
        return ways


class Solution2:
    def get_ways(self, arr: List[int], aim: int):
        """
        dp
        index: 0 - N
        rest: 0 - aim
        准备二维列表 [N + 1][aim + 1]
        """
        # 统计面值及数量数组
        currency_map = {}
        for money in arr:
            count = currency_map.get(money, 0)
            count += 1
            currency_map[money] = count
        moneys, counts = list(currency_map.keys()), list(currency_map.values())
        N = len(moneys)
        dp = [[0] * (aim + 1) for _ in range(N + 1)]
        dp[N][0] = 1
        for index in range(N - 1, - 1, -1):
            for rest in range(aim + 1):
                money = moneys[index]
                count = 0
                ways = 0
                while count <= counts[index] and money * count <= rest:
                    ways += dp[index + 1][rest - money * count]
                    count += 1
                dp[index][rest] = ways
        return dp[0][aim]


class Solution3:
    def get_ways(self, arr: List[int], aim: int):
        """
        dp
        index: 0 - N
        rest: 0 - aim
        准备二维列表 [N + 1][aim + 1]
        """
        # 统计面值及数量数组
        currency_map = {}
        for money in arr:
            count = currency_map.get(money, 0)
            count += 1
            currency_map[money] = count
        moneys, counts = list(currency_map.keys()), list(currency_map.values())
        N = len(moneys)
        dp = [[0] * (aim + 1) for _ in range(N + 1)]
        dp[N][0] = 1
        for index in range(N - 1, - 1, -1):
            for rest in range(aim + 1):
                money = moneys[index]
                dp[index][rest] = dp[index + 1][rest]
                if rest - money >= 0:
                    dp[index][rest] += dp[index][rest - money]
                if rest >= counts[index] * money + money:
                    dp[index][rest] -= dp[index + 1][rest - counts[index] * money - money]
        return dp[0][aim]


def main():
    arr = [1, 2, 1, 1, 2, 1, 2]
    aim = 4

    t1 = time.time()
    solution = Solution()
    res1 = solution.get_ways(arr, aim)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.get_ways(arr, aim)
    t3 = time.time()
    print(t3 - t2, res2)

    solution3 = Solution3()
    res3 = solution3.get_ways(arr, aim)
    t4 = time.time()
    print(t4 - t3, res3)


if __name__ == '__main__':
    main()
