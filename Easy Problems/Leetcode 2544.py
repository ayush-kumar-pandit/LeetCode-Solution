class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = []
        while n:
            res.append(n % 10)
            n //= 10
        res.reverse()
        for i in range(1,len(res), 2):
            res[i] = res[i] * -1
        return sum(res)