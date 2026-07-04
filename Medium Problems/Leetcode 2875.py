class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in 'aeiou' or ch in 'AEIOU':
                vowels.append(ch)
        vowels.sort()
        ls = list(s)
        j = 0 
        n = len(ls)
        for i in range(n):
            if ls[i] in 'aeiou' or ls[i] in 'AEIOU':
                ls[i] = vowels[j]
                j += 1
        return ''.join(ls)