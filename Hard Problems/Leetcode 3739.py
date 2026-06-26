class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n
        
        cnt = [0] * (2 * n + 1)
        
        cnt[offset] = 1
        
        balance = 0
        ans = 0
        
        less_than_count = 0
        
        for num in nums:
            if num == target:
                less_than_count += cnt[offset + balance]
                balance += 1
            else:
                balance -= 1
                less_than_count -= cnt[offset + balance]
            
            ans += less_than_count
            
            cnt[offset + balance] += 1
            
        return ans