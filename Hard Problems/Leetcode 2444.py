class Solution:
    def countSubarrays(self, nums, minK, maxK):
        lastMin = -1
        lastMax = -1
        lastBad = -1
        
        res = 0
        
        for i, num in enumerate(nums):
           
            if num < minK or num > maxK:
                lastBad = i
            
            if num == minK:
                lastMin = i
            
            if num == maxK:
                lastMax = i
            
            res += max(0, min(lastMin, lastMax) - lastBad)
        
        return res