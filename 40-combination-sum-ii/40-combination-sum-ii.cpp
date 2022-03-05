class Solution {
public:
    void totalWays(vector<int>&candidates,int target,int curr, vector<vector<int>>&res, vector<int>&aux)
    {
        //if(curr==candidates.size()){
            if(target==0){
                res.push_back(aux);
            //}
            return ;
        }
        for(int i = curr; i<candidates.size(); i++)
        {
            if(i>curr && candidates[i]==candidates[i-1]) continue;
        
        if(candidates[curr]<=target){
            aux.push_back(candidates[i]);
            totalWays(candidates, target-candidates[i],i+1,res,aux);
            aux.pop_back();
        }
       // totalWays(candidates, target,curr+1,res,aux);
    }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>>res;
        sort(candidates.begin(),candidates.end());
        vector<int> aux;
        totalWays(candidates,target,0,res,aux);
        return res;
    }
};