class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 2 not in nums or 1 not in nums:
            return -1
        n1 = -1
        n2 = -1
        ans = float(inf)
        for i in range(len(nums)):
            if nums[i] == 1:
                n1 = i
                if n2 != -1:
                    ans = min(ans,abs(n1 - n2))
            elif nums[i] == 2:
                n2 = i
                if n1 != -1:
                    ans = min(ans,abs(n1 - n2))
        return ans