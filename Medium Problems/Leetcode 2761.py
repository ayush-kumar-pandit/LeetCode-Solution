class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def countPrimes(n: int):
            
            prime = [True] * n
            prime[0] = prime[1] = False

            for i in range(2, int(n**0.5) + 1):
                if prime[i]:
                    for j in range(i * i, n, i):
                        prime[j] = False

            res = {}
            for i in range(len(prime)):
                if prime[i]:
                    res[i] = True
            return res
        
        if n < 2:
            return []
        d = countPrimes(n)
        res = []
        for i in d:
            if n - i in d and d[n - i] == True:
                res.append([i,n - i])
                d[i] = False
                
        return res