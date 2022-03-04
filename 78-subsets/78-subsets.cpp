class Solution {
    private:
    void ss(int idx, vector<int>& nums, vector<int> &ds, vector<vector<int>> &ans)
    { 
        ans.push_back(ds);
    for(int i= idx; i<nums.size();i++)
    {
        if(i!=idx && nums[i]== nums[i-1]) continue;
        ds.push_back(nums[i]);
        ss(i+1,nums,ds,ans);
        ds.pop_back();
    }
}
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> ds;
        sort(nums.begin(),nums.end());
        ss(0,nums,ds,ans);
        return ans;
    }
};