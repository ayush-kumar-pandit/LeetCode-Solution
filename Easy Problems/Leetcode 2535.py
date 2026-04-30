class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        y = 0
        for i in nums:
            while i:
                y += i % 10
                i //= 10
        return abs(sum(nums) - y)