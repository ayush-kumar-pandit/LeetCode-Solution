class Solution {
public:
    int smallestNumber(int n) {
        int i = 0;
        while( 2 << i <= n ){
            i++;
        }
        return (2 << i) - 1;
    }
};