class Solution {
public:
    int mirrorDistance(int n) {
        int x = 0;
        int temp = n;
        while(temp){
            x = x * 10 + temp % 10; 
            temp /= 10;
        }
        if(x > n) return x - n;
        else return n - x;
    }
};      