class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        res = float('inf')
        for i in range(start, len(nums)):
            if nums[i] == target:
                res = min(res, abs(i - start))
        for i in range(start, -1, -1):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res
        