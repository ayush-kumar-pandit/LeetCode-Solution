class Solution:
    def maxDistinct(self, s: str) -> int:
        my_dict = {}
        for x in s:
            if x not in my_dict:
                my_dict[x] = 1
        return len(my_dict)