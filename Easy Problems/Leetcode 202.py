class Solution:
    def isHappy(self, n: int) -> bool:
        ls = []
        while n != 1:
            x = 0
            while n:
                x += (n % 10) ** 2
                n //= 10
            if x in ls:
                return False
            ls.append(x)
            n = x
        return True