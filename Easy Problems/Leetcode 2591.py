class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children  
        
        res = min(money // 7, children)

        money -= res * 7
        children -= res

        if children == 0 and money > 0:
            res -= 1

        if children == 1 and money == 3:
            res -= 1

        return res
