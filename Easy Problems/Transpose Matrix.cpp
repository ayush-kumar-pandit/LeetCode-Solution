class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int h = matrix.size();
        int w = matrix[0].size();
        vector<vector<int>> ans(w,vector<int>(h));
        for(int i = 0; i < w; i++){
            for(int j = 0; j < h; j++){
                ans[i][j] = matrix[j][i];
            }
        }
        return ans;
        }
};