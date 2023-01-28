"""
用1*2的瓷砖，把N*2的区域填满，返回铺瓷砖的方法数
"""
import numpy as np


class Solution:
    def count(self, n: int) -> int:
        if n < 1:
            return 0
        if n in [1, 2, 3]:
            return n
        # 1*2瓷砖竖着
        p1 = self.count(n - 1)
        # 1*2瓷砖横着
        p2 = self.count(n - 3)
        return p1 + p2


class Solution2:
    def count(self, n: int) -> int:
        if n < 1:
            return 0
        if n in [1, 2, 3]:
            return n
        res = 3
        pre = 2
        prepre = 1
        for i in range(4, n + 1):
            temp = res
            res = prepre + res
            pre, prepre = temp, pre
        return res


class Solution3:
    def count(self, n: int) -> int:
        if n < 1:
            return 0
        if n in [1, 2, 3]:
            return n
        t = [
            [1, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ]
        res = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        p = n - 3
        while p != 0:
            if p & 1 != 0:
                res = np.array(res).dot(np.array(t))
            t = np.array(t).dot(np.array(t))
            p >>= 1
        return int(3 * res[0][0] + 2 * res[1][0] + res[2][0])


def main():
    n = 40
    s1 = Solution()
    res1 = s1.count(n)
    print(res1)

    s2 = Solution()
    res2 = s2.count(n)
    print(res2)

    s3 = Solution()
    res3 = s3.count(n)
    print(res3)


if __name__ == '__main__':
    main()
