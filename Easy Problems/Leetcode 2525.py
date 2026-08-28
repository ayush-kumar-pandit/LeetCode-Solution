class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume=length*width*height
        Bulky=False
        Heavy=False
        if length >=10**4 or width >=10**4 or height >=10**4:
            Bulky=True
        elif volume >= 10**9:
            Bulky=True
        if mass >= 100:
            Heavy=True
        if (Bulky) and (Heavy):
            return "Both"
        elif not (Bulky) and not (Heavy):
            return "Neither"
        elif (Bulky) and not (Heavy):
            return "Bulky"
        elif not (Bulky) and (Heavy):
            return "Heavy"