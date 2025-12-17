class Solution {
public:
    string intToRoman(int num) {
        string result;
        while (num) {
            if (num >= 1000) {
                    result.append("M");
                    num -= 1000;                
            }
            else if (num >= 500) {
                if (num + 100 >= 1000) {
                    result += "C";
                    num += 100;
                    continue;
                }
                    result.append("D");
                    num -= 500;
                
            }
            else if (num >= 100) {
                
                if (num + 100 >= 500) {
                    result += "C";
                    num += 100;
                    continue;
                }
                result.append("C");
                num -= 100;
            } 
            else if (num >= 50) {
                    if (num + 10 >= 100) {
                    result += "X";
                    num += 10;
                    continue;
                }
                    result.append("L");
                    num -= 50;
                
            } 
            else if (num >= 10) {
                    if (num + 10 >= 50) {
                    result += "X";
                    num += 10;
                    continue;
                }
                    result.append("X");
                    num -= 10;
            
            } 
            else if (num >= 5) {
                    if (num + 1 >= 10) {
                    result += "I";
                    num += 1;
                    continue;
                }
                    result.append("V");
                    num -= 5;
                
            } 
            else if (num >= 1) {
                    if (num + 1 >= 5) {
                    result += "I";
                    num += 1;
                    continue;
                }

                    result.append("I");
                    num -= 1;
            }
        }
        return result;
    }
};