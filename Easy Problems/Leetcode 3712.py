class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        s = 0
        for i in nums:
            if dic[i] % k == 0:
                s += i
        return s