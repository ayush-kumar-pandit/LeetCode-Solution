class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = abs(nums[0])
        for i in nums:
            res = min(res,abs(i))
        if res not in nums:
            res = res * -1
        return res