"""
加油站的良好出发点问题

在一条环路上有 n个加油站，其中第 i个加油站有汽油gas[i]升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

链接：https://leetcode-cn.com/problems/gas-station
"""
from typing import List
from collections import deque


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1、0-n号加油站，汽油和距离差值
        N = len(gas)
        gas_cost = []
        for i in range(N):
            gas_cost.append(gas[i] - cost[i])
        gas_cost.extend(gas_cost)
        # 2、前缀和
        for i in range(1, 2 * N):
            gas_cost[i] += gas_cost[i - 1]
        # 3、构造小值窗口
        min_window = deque()
        for i in range(N):
            while min_window and gas_cost[min_window[-1]] >= gas_cost[i]:
                min_window.pop()
            min_window.append(i)
        # 4、滑动窗口查看当前位置是否满足
        ans = [False] * N
        i = 0
        for j in range(N, 2 * N):
            offset = gas_cost[i - 1] if i > 0 else 0
            if gas_cost[min_window[0]] - offset >= 0:
                ans[i] = True
            if min_window and min_window[0] == i:
                min_window.popleft()
            while min_window and gas_cost[min_window[-1]] >= gas_cost[j]:
                min_window.pop()
            min_window.append(j)
            i += 1
        # 5、查找True
        for i in range(N):
            if ans[i]:
                return i
        return -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1、0-n号加油站，汽油和距离差值
        N = len(gas)
        gas_cost = []
        for i in range(N):
            gas_cost.append(gas[i] - cost[i])
        gas_cost.extend(gas_cost)
        # 2、前缀和
        for i in range(1, 2 * N):
            gas_cost[i] += gas_cost[i - 1]
        # 3、构造小值窗口
        min_window = deque()
        for i in range(N):
            while min_window and gas_cost[min_window[-1]] >= gas_cost[i]:
                min_window.pop()
            min_window.append(i)
        # 4、滑动窗口查看当前位置是否满足
        i = 0
        for j in range(N, 2 * N):
            offset = gas_cost[i - 1] if i > 0 else 0
            if gas_cost[min_window[0]] - offset >= 0:
                return i
            if min_window and min_window[0] == i:
                min_window.popleft()
            while min_window and gas_cost[min_window[-1]] >= gas_cost[j]:
                min_window.pop()
            min_window.append(j)
            i += 1
        return -1


class Solution3:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas_cost = []
        for i in range(N):
            gas_cost.append(gas[i] - cost[i])
        gas_cost.extend(gas_cost)

        for left in range(N):
            cur_gas = 0
            right = left
            while right - left < N:
                cur_gas += gas_cost[right]
                if cur_gas < 0:
                    break
                right += 1
            else:
                return left
        return -1


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    res = s.canCompleteCircuit(gas, cost)
    print(res)
    s2 = Solution2()
    res2 = s2.canCompleteCircuit(gas, cost)
    print(res2)
    s3 = Solution3()
    res3 = s3.canCompleteCircuit(gas, cost)
    print(res3)


if __name__ == '__main__':
    main()
