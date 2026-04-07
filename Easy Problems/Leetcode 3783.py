class Solution:
    def mirrorDistance(self, n: int) -> int:
        copy = n
        rev = 0
        while copy > 0:
            rev = rev * 10 + copy % 10
            copy //= 10
        return abs( n - rev)