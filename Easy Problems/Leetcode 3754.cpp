class Solution {
public:
    long long sumAndMultiply(int n) {
        stack<int> st;
        int sum = 0;

        while(n){
            int temp = n % 10;
            if(temp != 0){
                sum += temp;
                st.push(temp);
            }
            n /= 10;
        }
        long long x = 0;
        while(!st.empty()){
            x = x * 10 + st.top();
            st.pop();
        }
        return x * sum;
    }
};