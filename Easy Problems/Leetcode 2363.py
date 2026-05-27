class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        my_dict = {}
        for item in items1:
            my_dict[item[0]] = my_dict.get(item[0], 0) + item[1]
        for item in items2:
            my_dict[item[0]] = my_dict.get(item[0], 0) + item[1]
        res = []
        for item in sorted(my_dict):
            res.append([item,my_dict[item]])
        
        return res