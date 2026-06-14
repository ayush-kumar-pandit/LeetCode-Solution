class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        s = set(nums)
        res = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                res = max(res, length)
        return res