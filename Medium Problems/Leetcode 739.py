class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sz = len(temperatures)
        res = [0] * sz
        st = []
        for i in range(sz):
            while st and temperatures[i] > temperatures[st[-1]]:
                x = st.pop()
                res[x] = i - x
            st.append(i)
        return res