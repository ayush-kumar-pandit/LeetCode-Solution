class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        res = 0

        for g in nums:
            g.sort(reverse = True)

        for i in range(len(nums[0])):
            ls = []
            for g in nums:
                ls.append(g[i])
            res += max(ls)
        return res 
