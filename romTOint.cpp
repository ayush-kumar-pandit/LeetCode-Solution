class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        char prev = '_';
        for (int i = s.size(); i >= 0; i--) {
            if ((s[i] == 'I' && prev == 'V') || (s[i] == 'I' && prev == 'X') ||
                (s[i] == 'X' && prev == 'L') || (s[i] == 'X' && prev == 'C') ||
                (s[i] == 'C' && prev == 'D') || (s[i] == 'C' && prev == 'M')) {
                switch (s[i]) {
                case 'I':
                    num -= 1;
                    break;

                case 'X':
                    num -= 10;
                    break;
               
                case 'C':
                    num -= 100;
                    break;
                
                }
            } else {
                switch (s[i]) {
                case 'I':
                    num += 1;
                    break;
                case 'V':
                    num += 5;
                    break;
                case 'X':
                    num += 10;
                    break;
                case 'L':
                    num += 50;
                    break;
                case 'C':
                    num += 100;
                    break;
                case 'D':
                    num += 500;
                    break;
                case 'M':
                    num += 1000;
                    break;
                }
            }
            prev = s[i];
        }
        return num;
    }
};