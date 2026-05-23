class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0
        for i in nums:
            while i:
                if i % 10 == digit:
                    res += 1
                i //= 10
        return res