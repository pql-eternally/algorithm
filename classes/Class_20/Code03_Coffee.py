"""
给定一个数组arr，arr[i]代表第i号咖啡机泡一杯咖啡的时间
给定一个正数N，表示N个人等着咖啡机泡咖啡，每台咖啡机只能轮流泡咖啡（串行）
只有一台咖啡机，一次只能洗一个杯子，时间耗费a，洗完才能洗下一杯
每个咖啡杯也可以自己挥发干净，时间耗费b，咖啡杯可以并行挥发
假设所有人拿到咖啡之后立刻喝干净，
返回从开始等到所有咖啡机变干净的最短时间
三个参数：int[] arr、int N，int a、int b
"""
import time
from typing import List


class Solution:
    def coffee(self, arr: List[int], N: int, a: int, b: int):
        """
        @param arr: arr[i]代表第i号咖啡机泡一杯咖啡的时间
        @param N: N个人等着咖啡机泡咖啡
        @param a: 咖啡机，一次只能洗一个杯子，时间耗费a
        @param b: 咖啡杯也可以自己挥发干净，时间耗费b
        @return:
        """
        # N个人全部喝完咖啡的最优时间

    def process(self):
        pass


def main():
    x = 4
    y = 1
    k = 9

    t1 = time.time()
    solution = Solution()
    res1 = 1
    t2 = time.time()
    print(f'{t2 - t1}s', res1)

    t3 = time.time()
    res2 = 2
    print(f'{t3 - t2}s', res2)


if __name__ == '__main__':
    main()
