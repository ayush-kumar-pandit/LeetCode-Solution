class Solution {
public:
    int countDigits(int num) {
        if(num < 10)    return 1;
        int count = 0;
        int copy = num;
        while(copy){
            if(num % (copy % 10) == 0)  count++;
            copy /= 10;
        } 
        return count;
    }
};