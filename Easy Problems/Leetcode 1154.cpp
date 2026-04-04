class Solution {
public:
    int dayOfYear(string date) {
        
        int months[] = {0,31,59,90,120,151,181,212,243,273,304,334};
        int m = 0;
        m = date[5] - '0';
        m = m * 10 + date[6] - '0';

        int d = 0;
        d = date[8] - '0';
        d = d * 10 + date[9] - '0';
        
        if(m == 1)   return d;
        
        int year = date[0] - '0';
        year = year * 10 + date[1] - '0';
        year = year * 10 + date[2] - '0';
        year = year * 10 + date[3] - '0';
        if((year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) and m > 2)    return d + months[m - 1] + 1;
        return d + months[m - 1];
    }
};