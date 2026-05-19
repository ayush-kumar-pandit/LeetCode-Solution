class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums2[0] > nums1[-1] or nums1[0] > nums2[-1]:
            return -1
        s = set(nums1)
        for i in nums2:
            if i in s:
                return i
        return -1