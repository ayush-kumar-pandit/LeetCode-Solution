class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = set()
        for i in nums:
            if i in s:
                res.append(i)
            else:
                s.add(i)
        return res