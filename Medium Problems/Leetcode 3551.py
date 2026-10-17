class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def getSum(x):
            n = 0
            while x:
                n += x % 10
                x //= 10
            return n 
        
        N = len(nums)
        indexed = [(getSum(c), nums[i],i) for i,c in enumerate(nums)]
        target_order = sorted(indexed)
        pos = [t[2] for t in target_order]
        visited = [False] * N
        swaps = 0
        for i in range(N):
            if not visited[i]:
                cycle_len = 0
                j = i
                while not visited[j]: 
                    visited[j] = True
                    j = pos[j]
                    cycle_len += 1
                swaps += cycle_len - 1
        return swaps
