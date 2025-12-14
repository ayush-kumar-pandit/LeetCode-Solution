class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int num = 0;
        int temp = x;
        while(temp){
            num = num + temp % 10;
            temp /= 10;
        }
        if(x % num == 0)    return num;
        return -1;
    }
};