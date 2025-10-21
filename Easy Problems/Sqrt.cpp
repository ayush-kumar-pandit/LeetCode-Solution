class Solution {
public:
    int mySqrt(int x) {
        if(x == 0 or x == 1)
            return x;
        int low = 0;
        int high = x;

        while(high >= low){
            long mid = low + (high - low)/2;
            
            if((mid * mid == x) or ((mid * mid < x) and ((mid + 1) * (mid + 1) > x))){
                return mid;
            }
            else if (mid * mid > x)
                high = mid - 1;
            else if (mid * mid < x)
                low = mid + 1;
        }
        return 0;
    }
};

           