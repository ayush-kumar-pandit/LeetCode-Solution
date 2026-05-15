class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [i for i in range(1,len(nums) + 1)]
        s = set()
        res = []
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                res.append(i)
        
        for i in arr:
            if i not in s:
                res.append(i)
                break
        return res
        