class Solution:
    hash_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    sort_nums = sorted(hash_map.keys(), reverse=True)

    def most_small_near_num(self, num: int) -> int:
        """
        找到比num小的最大的数
        """
        for i in self.sort_nums:
            if i <= num:
                return i
        raise ValueError('num is too small')

    def intToRoman(self, num: int) -> str:
        if num in self.hash_map:
            return self.hash_map[num]
        near_num = self.most_small_near_num(num)
        return self.hash_map[near_num] + self.intToRoman(num - near_num)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(0))
    print(solution.intToRoman(3))
    print(solution.intToRoman(4))
    print(solution.intToRoman(8))
    print(solution.intToRoman(9))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))
    print(solution.intToRoman(2000))
