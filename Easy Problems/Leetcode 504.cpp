class Solution {
public:
    string convertToBase7(int num) {
        string ans = "";
        if(num == 0) return "0";
        stack<string> st;
        if(num < 0){
            ans = ans + "-";
            num *= -1;
        }
        while(num){
            st.push(to_string(num % 7));
            num /= 7;
        }
        while(!st.empty()){
            ans = ans + st.top();
            st.pop();
        }
        return ans;
    }
};