class Solution {
public:
    long long removeZeros(long long n) {
        stack<int> st;

        while(n){
            int temp = n % 10;
            if(temp != 0){
                st.push(temp);
            }
            n /= 10;
        }
        long long x = 0;
        while(!st.empty()){
            x = x * 10 + st.top();
            st.pop();
        }
        return x;
    }
};