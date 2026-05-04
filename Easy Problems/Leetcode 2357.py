class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i not in res and i != 0:
                res.append(i)
        return len(res)