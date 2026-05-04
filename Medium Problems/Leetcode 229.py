class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        thres = len(nums) // 3 + 1

        for i in set(nums):
            if my_dict[i] >= thres:
                res.append(i)

        return res