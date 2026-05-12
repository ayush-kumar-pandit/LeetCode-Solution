class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1[:] + nums2[:]
        temp.sort()
        sz = len(temp)
        if sz & 1:
            return temp[sz // 2]
        else:
            return (temp[sz // 2] + temp[(sz // 2) - 1]) / 2