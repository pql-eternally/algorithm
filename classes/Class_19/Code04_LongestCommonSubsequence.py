"""
给定两个字符串str1和str2，
返回这两个字符串的最长公共子序列长度
比如 ： str1 = “a12b3c456d”,str2 = “1ef23ghi4j56k”
最长公共子序列是“123456”，所以返回长度6


https://leetcode.com/problems/longest-common-subsequence/
"""
import time
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 从右往左尝试
        L1 = len(text1)
        L2 = len(text2)
        return self.process(list(text1), list(text2), L1 - 1, L2 - 1)

    def process(self, arr1: List[str], arr2: List[str], i: int, j: int):
        """
        @param arr1: 字符串1的字符串数组
        @param arr2: 字符串2的字符串数组
        @param i: 只考虑字符串1从0到i位置
        @param j: 只考虑字符串2从0到j位置
        @return: 返回最长公共子序列
        """
        if i == 0 and j == 0:
            return 1 if arr1[0] == arr2[0] else 0
        elif i == 0:
            if arr1[0] == arr2[j]:
                return 1
            else:
                return self.process(arr1, arr2, 0, j - 1)
        elif j == 0:
            if arr1[i] == arr2[0]:
                return 1
            else:
                return self.process(arr1, arr2, i - 1, 0)
        else:
            if arr1[i] == arr2[j]:
                return 1 + self.process(arr1, arr2, i - 1, j - 1)
            else:
                p1 = self.process(arr1, arr2, i - 1, j)
                p2 = self.process(arr1, arr2, i, j - 1)
                return max(p1, p2)


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1 = len(text1)
        L2 = len(text2)
        dp = [[-1] * (L2 + 1) for _ in range(L1 + 1)]
        return self.process(list(text1), list(text2), L1 - 1, L2 - 1, dp)

    def process(self, arr1: List[str], arr2: List[str], i: int, j: int, dp: List[List[int]]):
        """
        @param arr1: 字符串1的字符串数组
        @param arr2: 字符串2的字符串数组
        @param i: 只考虑字符串1从0到i位置
        @param j: 只考虑字符串2从0到j位置
        @param dp: 记忆化缓存
        @return: 返回最长公共子序列
        """
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0 and j == 0:
            res = 1 if arr1[0] == arr2[0] else 0
        elif i == 0:
            if arr1[0] == arr2[j]:
                res = 1
            else:
                res = self.process(arr1, arr2, 0, j - 1, dp)
        elif j == 0:
            if arr1[i] == arr2[0]:
                res = 1
            else:
                res = self.process(arr1, arr2, i - 1, 0, dp)
        else:
            if arr1[i] == arr2[j]:
                res = 1 + self.process(arr1, arr2, i - 1, j - 1, dp)
            else:
                p1 = self.process(arr1, arr2, i - 1, j, dp)
                p2 = self.process(arr1, arr2, i, j - 1, dp)
                res = max(p1, p2)
        dp[i][j] = res
        return res


class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1 = len(text1)
        L2 = len(text2)
        dp = [[0] * L2 for _ in range(L1)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        # 填第0行
        for j in range(1, L2):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        # 填第0列
        for i in range(1, L1):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        # 填中间行列
        for i in range(1, L1):
            for j in range(1, L2):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[L1 - 1][L2 - 1]


def main():
    text1 = "ylqpejqbalahwr"
    text2 = "yrkzavgdmdgtqpg"
    start_at = time.time()
    s = Solution()
    res1 = s.longestCommonSubsequence(text1, text2)
    end_at = time.time()
    print(f'run 1 {end_at - start_at}ms', res1)

    s2 = Solution2()
    res2 = s2.longestCommonSubsequence(text1, text2)
    end_at2 = time.time()
    print(f'run 2 {end_at2 - end_at}ms', res2)

    s3 = Solution3()
    res3 = s3.longestCommonSubsequence(text1, text2)
    end_at3 = time.time()
    print(f'run 3 {end_at3 - end_at2}ms', res3)
    assert res1 == res2 == res3


if __name__ == '__main__':
    main()
