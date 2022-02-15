"""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        当前字符串正序和反序的最大公共子序列
        """
        L = len(s)
        dp = [[0] * L for _ in range(L)]
        text1 = s
        text2 = s[::-1]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        # 填第0行
        for j in range(1, L):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        # 填第0列
        for i in range(1, L):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        # 填中间行列
        for i in range(1, L):
            for j in range(1, L):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[L - 1][L - 1]


def main():
    s = 'bbbab'
    solution = Solution()
    res = solution.longestPalindromeSubseq(s)
    print(res)


if __name__ == '__main__':
    main()
