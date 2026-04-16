class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ls = []
        for i,v in enumerate(nums):
            if v == target:
                ls.append(i)
        return ls