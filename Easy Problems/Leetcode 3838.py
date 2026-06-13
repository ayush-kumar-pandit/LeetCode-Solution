class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        table = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        j = 0
        for i in range(len(alphabet) - 1, -1, -1):
            table[j] = alphabet[i]
            j += 1
        
        res = ""
        for word in words:
            score = 0
            for letter in word:
                score += weights[ord(letter) - 97]
            res += table[score % 26]
        
        return res