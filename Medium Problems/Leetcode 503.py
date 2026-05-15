class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [-1] * size
        st = []
        for i in range(size * 2 - 1, -1, -1):
            while st and nums[i % size] >= nums[st[-1]]:
                x = st.pop()
            res[i % size] = -1 if not st else nums[st[-1]]
            st.append(i % size)    
        return res