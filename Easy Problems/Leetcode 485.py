class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i:
                count += 1
            else:
                res = max(res,count)
                count = 0
        return max(count,res)
