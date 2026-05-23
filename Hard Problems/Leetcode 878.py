class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        lcm = (a * b) // gcd(a, b)
        low = 0
        high = n * min(a,b)
        while low < high:
            mid = low + (high - low) // 2
            x = mid // a + mid // b - mid // lcm
            if x >= n:
                high = mid
            else:
                low = mid + 1
        return low % MOD