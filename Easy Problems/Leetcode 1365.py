class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = sorted(nums)
        res = []
        for i in nums:
            for j in range(len(ls)):
                if i == ls[j]:
                    res.append(j)
                    break
        return res

        