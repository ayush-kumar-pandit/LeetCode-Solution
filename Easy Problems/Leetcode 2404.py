class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        my_dict = {}
        count = 0
        for i in nums:
            if not i & 1:
                count += 1
                if i not in my_dict:
                    my_dict[i] = 1
                else:
                    my_dict[i] += 1
        if not count:
            return -1
        nums.sort()
        max_freq = max(my_dict.values())
        for i in nums:
            if i in my_dict:
                if my_dict[i] == max_freq:
                    return i