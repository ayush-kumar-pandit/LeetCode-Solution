class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        s = set(nums)
        res = []
        for i in range(mn,mx):
            if i not in s:
                res.append(i)
        return res