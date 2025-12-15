class Solution {
public:
    int maximum69Number (int num) {
        if(num == 9999 or num == 9996 or num == 9969 or num == 9699 or num == 6999)   return 9999;

        int x = num; 
        bool flag = true;
        
        stack<int> st;
        while(x){
            st.push(x % 10);
            x /= 10;
        }

        while(!st.empty()){
            int y = st.top();
            if(y == 6 and flag == true){
                y = 9;
                flag = false;
            }
            x = x * 10 + y;
            st.pop();

        }
        return x;

    }
};