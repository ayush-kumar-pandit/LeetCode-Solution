class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == INT_MAX and divisor == -1)  
            return INT_MIN + 1;

        if(dividend == INT_MIN and divisor == -1)
            return INT_MAX;


        return dividend/divisor;
    }
};