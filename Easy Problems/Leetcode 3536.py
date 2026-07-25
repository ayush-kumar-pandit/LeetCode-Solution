class Solution:
    def maxProduct(self, n: int) -> int:
        ls = []
        while n:
            ls.append(n % 10)
            n //= 10
        ls.sort()
        return ls[-1] * ls[-2]