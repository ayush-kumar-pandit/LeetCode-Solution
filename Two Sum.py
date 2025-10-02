class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
            
        for i in range(len(nums)):
            x = target - nums[i]

            if x in my_dict and my_dict[x] != i:
                return [i,my_dict[x]]