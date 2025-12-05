class Solution {
public:
    vector<int> decimalRepresentation(int n) {
        long long div = 1;
        stack<int> st;
        
        while(n){
            div *= 10;
            int temp = n % div;
            if(temp)
                st.push(temp);
            n -= temp;
        }

        vector<int> V;
        while(!st.empty()){
            V.push_back(st.top());
            st.pop();
        }

        return V;
    }
};