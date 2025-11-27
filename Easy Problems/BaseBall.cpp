class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        for(string ch: operations){
            if(ch == "+"){
                int x = st.top();
                st.pop();
                int y = st.top();
                st.push(x);
                st.push(x + y);
            }
            else if(ch == "C") st.pop();
            
            else if(ch == "D"){
                int x = st.top();
                st.push(x * 2);
            }
            else st.push(stoi(ch));
        }
        int sum = 0;
        while(!st.empty()){
            sum = sum + st.top();
            st.pop();
        }
        return sum;
    }
};