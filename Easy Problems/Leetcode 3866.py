class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums:
            if dic[i] == 1 and i % 2 == 0:
                return i
        return -1