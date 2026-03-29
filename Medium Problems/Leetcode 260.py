class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        ls = []
        for i in nums:
            if dic[i] == 1:
                ls.append(i)
            
        return ls
            