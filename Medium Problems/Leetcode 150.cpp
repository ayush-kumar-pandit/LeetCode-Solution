class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int a,b;
        for(string ch: tokens){
            if(ch == "+"){
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();

                st.push(a+b);
            }
            else if(ch == "-"){
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();

                st.push(a-b);
            }
            else if(ch == "*"){
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();

                st.push(a*b);
            }
            else if(ch == "/"){
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();

                st.push(a/b);
            }
            else{
                st.push(stoi(ch));
            }
        }
        return st.top();
    }
};