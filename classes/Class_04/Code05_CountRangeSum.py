"""
区间和的个数

给你一个整数数组 nums 以及两个整数 lower 和 upper。
求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

示例 1：
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。

示例 2：
输入：nums = [0], lower = 0, upper = 0
输出：1
"""


class Solution:
    def count_range_sum(self, nums: list, lower: int, upper: int) -> int:
        """
        1、此问题可以使用前缀和来解决
        2、要求区间和的个数可以转换为求包含某个位置i所有区间和个数的和，例如：包含位置3则有：[0, 3]、[1, 3]、[2, 3]、[3, 3]
        3、我们可以从前缀和中拿到当前位置i前面所有数字的和，例如为s
        4、要求包含当前位置i区间和位于[lower, upper]的个数，相当于找位于[s-upper, s-lower]区间和个数
        5、归并排序在merge过程中求右侧
        """
        sums = self.prefix_sum(nums)
        return self.process(sums, 0, len(sums) - 1, lower, upper)

    def prefix_sum(self, nums: list):
        """
        整数数组的前缀和
        S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)
        可以等价于求：sums[j] - sums[i - 1]
        """
        sums = []
        sums.insert(0, nums[0])
        for i in range(1, len(nums)):
            sums.append(sums[-1] + nums[i])
        return sums

    def process(self, sums: list, left: int, right: int, lower: int, upper: int) -> int:
        # 判断当前位置只有自己一个数的情况是否满足区间和，因为归并的时候都是大于一个数的时候
        if left == right:
            return 1 if (sums[left] >= lower) and (sums[left] <= upper) else 0

        mid = left + ((right - left) >> 1)
        count = self.process(sums, left, mid, lower, upper) + \
                self.process(sums, mid + 1, right, lower, upper) + \
                self.merge(sums, left, mid, right, lower, upper)
        return count

    def merge(self, sums: list, left: int, mid: int, right: int, lower: int, upper: int) -> int:
        res = 0
        # 需要两个下标记录满足区间和
        window_l = window_r = left
        # 统计右侧
        for i in range(mid + 1, right + 1):
            cur_min = sums[i] - upper
            cur_max = sums[i] - lower
            # 求满足下限索引位置
            while window_l <= mid and sums[window_l] < cur_min:
                window_l += 1
            # 求满足上限索引位置
            while window_r <= mid and sums[window_r] <= cur_max:
                window_r += 1
            res += window_r - window_l

        # 合并
        help_arr = []
        p1 = left
        p2 = mid + 1
        while p1 <= mid and p2 <= right:
            if sums[p1] < sums[p2]:
                help_arr.append(sums[p1])
                p1 += 1
            else:
                help_arr.append(sums[p2])
                p2 += 1
        help_arr.extend(sums[p1: mid + 1])
        help_arr.extend(sums[p2: right + 1])
        sums[left: right + 1] = help_arr
        return res


def main():
    s = Solution()
    arr = [-2, 5, -1]
    res = s.count_range_sum(arr, -2, 2)
    print(res)


if __name__ == '__main__':
    main()
