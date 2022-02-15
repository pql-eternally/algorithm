"""
给定一个字符串str，给定一个字符串类型的数组arr，出现的字符都是小写英文
arr每一个字符串，代表一张贴纸，你可以把单个字符剪开使用，目的是拼出str来
返回需要至少多少张贴纸可以完成这个任务
例子：str= "babac"，arr = {"ba","c","abcd"}
ba + ba + c  3  abcd + abcd 2  abcd+ba 2
所以返回2

https://leetcode-cn.com/problems/stickers-to-spell-word/
# TODO: 代码待优化，leetcode超时未通过
"""
import sys

from typing import List, Dict


class Solution:
    MAX_INT = sys.maxsize

    def minStickers(self, stickers: List[str], target: str) -> int:
        res = self.process(stickers, target)
        if res == self.MAX_INT:
            return -1
        return res

    def process(self, stickers: List[str], target: str) -> int:
        # 字符串已经拼接完了，不需要贴纸了
        if not target:
            return 0
        res = self.MAX_INT
        for sticker in stickers:
            # 使用完贴纸后剩余的字符
            rest = self.minus(target, sticker)
            if len(target) != len(rest):
                res = min(res, self.process(stickers, rest))
        if res != self.MAX_INT:
            res += 1
        return res

    def minus(self, target: str, sticker: str):
        """
        当前字符串减去给定的字符串中存在的字符，返回剩余的字符组成的字符串
        """
        for c in sticker:
            if c in target:
                target = target.replace(c, '', 1)
        return target


class Solution2:
    MAX_INT = sys.maxsize

    def minStickers(self, stickers: List[str], target: str) -> int:
        # 构造词频数组
        sticker_counts = []
        for sticker in stickers:
            counts = [0] * 26
            for c in sticker:
                counts[ord(c) - ord('a')] += 1
            sticker_counts.append(counts)
        res = self.process(sticker_counts, target)
        if res == self.MAX_INT:
            return -1
        return res

    def process(self, sticker_counts: List[List[int]], target: str) -> int:
        # 字符串已经拼接完了，不需要贴纸了
        if not target:
            return 0
        res = self.MAX_INT
        for sticker_count in sticker_counts:
            if sticker_count[ord(target[0]) - ord('a')] > 0:
                # 计算剩余字符串
                rest = self.minus(target, sticker_count)
                res = min(res, self.process(sticker_counts, rest))
        if res != self.MAX_INT:
            res += 1
        return res

    def minus(self, target: str, sticker_count: List[int]):
        words = set()
        for c in target:
            if c in words:
                continue
            count = sticker_count[ord(c) - ord('a')]
            target = target.replace(c, '', count)
            words.add(c)
        return target


class Solution3:
    MAX_INT = sys.maxsize

    def minStickers(self, stickers: List[str], target: str) -> int:
        # 构造词频数组
        sticker_counts = []
        for sticker in stickers:
            counts = [0] * 26
            for c in sticker:
                counts[ord(c) - ord('a')] += 1
            sticker_counts.append(counts)
        dp = {}
        # 目标字符串排序
        targets = list(target)
        targets.sort()
        target = ''.join(targets)
        res = self.process(sticker_counts, target, dp)
        if res == self.MAX_INT:
            return -1
        return res

    def process(self, sticker_counts: List[List[int]], target: str, dp: Dict) -> int:
        if target in dp:
            return dp[target]
        if not target:
            return 0
        res = self.MAX_INT
        for sticker_count in sticker_counts:
            if sticker_count[ord(target[0]) - ord('a')] > 0:
                # 计算剩余字符串
                rest = self.minus(target, sticker_count)
                res = min(res, self.process(sticker_counts, rest, dp))
        if res != self.MAX_INT:
            res += 1
        return res

    def minus(self, target: str, sticker_count: List[int]):
        words = set()
        for c in target:
            if c in words:
                continue
            count = sticker_count[ord(c) - ord('a')]
            target = target.replace(c, '', count)
            words.add(c)
        return target


def main():
    stickers = ["with", "example", "science"]
    target = "thehat"
    s = Solution()
    res = s.minStickers(stickers, target)
    s2 = Solution2()
    res2 = s2.minStickers(stickers, target)
    s3 = Solution3()
    res3 = s3.minStickers(stickers, target)
    print(res)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
