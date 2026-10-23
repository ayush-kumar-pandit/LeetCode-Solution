class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = None
        for i, v in enumerate(nums):
            if i != v: 
                if res is None:
                    res = v
                else:
                    res &= v
        return 0 if res is None else res
        