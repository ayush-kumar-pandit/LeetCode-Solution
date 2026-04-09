class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for i in range(len(paths)):
            dic[paths[i][0]] = paths[i][1]
        for i in paths:
            if i[1] not in dic.keys():
                return i[1]
            

            