class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2:
            return False
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums:
            if dic[i] % 2:
                return False
            
        return True