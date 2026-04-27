class Solution:
    def findMin(self, nums: List[int]) -> int:
        s1 = []
        d = {}
        for i in nums:
            if i not in d:
                s1.append(i)
                d[i] = 1

        if len(s1) == 1:
            return nums[0]
        l = 0
        r = len(s1) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if s1[mid] < s1[mid - 1]:
                return s1[mid]
            elif s1[mid] > s1[l] and s1[l] > s1[r]:
                l = mid + 1

            else:
                r = mid - 1
        
        return s1[l + 1]