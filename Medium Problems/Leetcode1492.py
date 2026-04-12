class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ls = []
        for i in range(1,n + 1):
            if n % i == 0:
                ls.append(i)
        if len(ls) < k:
            return -1
        return ls[k - 1]