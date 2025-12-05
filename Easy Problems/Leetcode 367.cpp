class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1 or num == 4)    return true;
        int high = num / 2;
        int low = 0;

        while(low <= high){
            long mid = low + (high - low) / 2;
            if(mid * mid == num)    return true;

            else if(mid * mid > num)   high = mid - 1;

            else if(mid * mid < num)   low = mid + 1; 
        }
        return false;
    }
};