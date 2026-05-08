class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = 0
        temp = n

        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10

        left = min(n, rev)
        right = max(n, rev)

        prime = [True] * (right + 1)

        if right >= 0:
            prime[0] = False
        if right >= 1:
            prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, right + 1, i):
                    prime[j] = False

        ans = 0
        for i in range(left, right + 1):
            if prime[i]:
                ans += i

        return ans