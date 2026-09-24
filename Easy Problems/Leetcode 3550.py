class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(x: int) -> int:
            if x < 10:
                return x
            num = 0
            while x:
                num = num + x % 10
                x //= 10
            return num
        
        for i in range(len(nums)):
            if i == digitSum(nums[i]):
                return i
        return -1