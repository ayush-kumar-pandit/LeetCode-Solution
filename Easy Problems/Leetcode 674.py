class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        ans = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                x = i + 2 - start
                if x >= ans:
                    ans = x
            else:
                start = i + 1
        return ans
 


