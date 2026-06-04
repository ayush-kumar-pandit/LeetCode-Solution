class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1, num2 + 1):
            st = str(i)
            for j in range(1,len(st) - 1):
                if (st[j] > st[j - 1] and st[j] > st[j + 1]) or (st[j] < st[j - 1] and st[j] < st[j + 1]):
                    res += 1
        return res