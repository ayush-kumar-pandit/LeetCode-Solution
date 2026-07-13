class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for i in nums:
            x = (x * 2 + i) % 5
            if x:
                res.append(False)
            else:
                res.append(True)
        return res