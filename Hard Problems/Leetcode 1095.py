# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length() - 1
        l = 0
        r = n

        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid - 1
        maxx = l

        l = 0
        r = maxx
        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1

        l = maxx
        r = n
        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1