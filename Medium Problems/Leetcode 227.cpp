class Solution {
public:
    int evalRPN(string postfix) {
        stack<int> st;
        stringstream ss(postfix);
        string token;

        while (ss >> token) {
            if (isdigit(token[0]) || (token.size() > 1 && token[0] == '-')) {
                st.push(stoi(token));
            } else {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();

                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else if (token == "/") st.push(a / b);
            }
        }
        return st.top();
    }

    bool precedence(char out, char st_top) {
        if (st_top == '*' || st_top == '/') return false;
        if (out == '*' || out == '/') return true;
        if (st_top == '+' || st_top == '-') return false;
        return true;
    }

    int calculate(string s) {
        stack<char> st;
        string postfix = "";
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];

            if (ch == ' ') continue;

            if (ch == '(') {
                st.push(ch);
            } 
            else if (ch == ')') {
                while (!st.empty() && st.top() != '(') {
                    postfix += st.top();
                    postfix += ' ';
                    st.pop();
                }
                if (!st.empty()) st.pop();
            } 
            else if (isdigit(ch)) {
                while (i < s.length() && isdigit(s[i])) {
                    postfix += s[i];
                    i++;
                }
                postfix += ' '; 
                i--;
            } 
            else {
                while (!st.empty() && st.top() != '(' && !precedence(ch, st.top())) {
                    postfix += st.top();
                    postfix += ' ';
                    st.pop();
                }
                st.push(ch);
            }
        }

        while (!st.empty()) {
            postfix += st.top();
            postfix += ' ';
            st.pop();
        }

        return evalRPN(postfix);
    }
};