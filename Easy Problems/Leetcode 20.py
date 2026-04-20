class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch in '{[(':
                st.append(ch)
            elif len(st) == 0 or (ch == ')' and st[-1] != '(') or (ch == '}' and st[-1] != '{') or (ch == ']' and st[-1] != '['):
                return False
            else:
                st.pop()
        return not len(st)