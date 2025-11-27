class Solution {
public:
    int arrangeCoins(int n) {
        int left = 0,right = n;
        while(left <= right){
            long mid = left + (right - left)/2;
            long coin = mid * (mid + 1) / 2;
            if(coin == n)
                return mid;
            else if(n < coin)
                right = mid - 1;
            else 
                left = mid + 1;
        }
    return right;
    }
};