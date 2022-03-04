class Solution {
public:
    void totalWays(vector<int>&candidates,int target,int curr, vector<vector<int>>&res, vector<int>&aux)
    {
        if(curr==candidates.size()){
            if(target==0){
                res.push_back(aux);
            }
            return ;
        }
        if(candidates[curr]<=target){
            aux.push_back(candidates[curr]);
            totalWays(candidates, target-candidates[curr],curr,res,aux);
            aux.pop_back();
        }
        totalWays(candidates, target,curr+1,res,aux);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> aux;
        totalWays(candidates,target,0,res,aux);
        return res;
    }
};