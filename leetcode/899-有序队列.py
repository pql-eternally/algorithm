"""
给定一个字符串 s 和一个整数 k。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。
返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串。

链接：https://leetcode.cn/problems/orderly-queue
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        length = len(s)
        if length == 0:
            return s
        if k >= length:
            return ''.join(sorted(s))

        chars = list(s)
        while True:
            max_char = max(chars[:k])
            # target_char = chars[k]
            # if max_char < target_char:
            #     break
            chars.remove(max_char)
            chars.append(max_char)
            print(''.join(chars))
        return ''.join(chars)


if __name__ == '__main__':
    s = "baaca"
    k = 3
    solution = Solution()
    res = solution.orderlyQueue(s, k)
    print(res)
