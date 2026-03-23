class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        sum = 0
        for i in nums:
            if dic[i] == 1:
                sum += i
        return sum