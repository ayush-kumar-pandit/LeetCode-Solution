class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        p,q = 0,k-1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p,q = p + 1, q - 1
        
        p,q = k,len(nums)-1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p,q = p + 1, q - 1