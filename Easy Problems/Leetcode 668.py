class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new = [x for x in range(1,n+1)]
        s = set(nums)
        res = []
        for i in new:
            if i not in s:
                res.append(i)
        return res
        