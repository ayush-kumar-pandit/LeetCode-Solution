class Solution {
public:
    string reversePrefix(string word, char ch) {
        int ind = -1;
        stack<char> st;
        for(int i = 0; i < word.size(); i++){
            st.push(word[i]);
            if(word[i] == ch){
                ind = i;
                break;
            }
        }
        if(ind == -1) return word;

        string temp = "";
        while(!st.empty()){
            temp = temp + st.top();
            st.pop();
        }
        for(int i = ind + 1; i < word.size();i++){
            temp = temp + word[i];
        }
        return temp;
    }
};