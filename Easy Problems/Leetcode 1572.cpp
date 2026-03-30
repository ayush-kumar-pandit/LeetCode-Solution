class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int x = mat.size() - 1;
        int ans = 0;
        for(int i = 0, j = 0; i <= x; i++,j++){
            if(mat.size() % 2 and i == x / 2){
                continue;
            }
            ans += mat[i][j];
                
        }
        for(int i = 0, j = x; i <= x; i++,j--){
            ans += mat[i][j];
        }
        return ans;
    }
};