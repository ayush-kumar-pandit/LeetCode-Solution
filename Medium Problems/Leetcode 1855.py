class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            l = i
            h = len(nums2) - 1
            while l <= h:
                mid = l + (h - l) // 2
                if nums2[mid] < nums1[i]:
                    h = mid - 1
                else:
                    l = mid + 1
            res = max(res, h - i)

        return res