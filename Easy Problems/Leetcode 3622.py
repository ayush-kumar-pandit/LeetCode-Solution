class Solution:
    def checkDivisibility(self, n: int) -> bool:
        copy = n
        s = 0
        p = 1
        while copy:
            s += copy % 10
            p *= copy % 10
            copy //= 10
        return n % (s + p) == 0