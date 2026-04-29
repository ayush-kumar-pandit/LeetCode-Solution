class Solution:
    def countEven(self, num: int) -> int:
        def count(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s % 2 == 0
        res = 0
        for i in range(1,num + 1):
            if count(i):
                res += 1
        return res