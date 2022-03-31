class Solution {
public:
bool isvalid(vector<int> arr, int n, int k, int max)
    {
        int student=1;
        int sum=0;
        
    for(int i=0;i<n;i++)
    {
        sum+=arr[i];
        
        if(sum>max)
        {
            student++;
            sum=arr[i];
        }
        
        
        if(student>k)
            return false;
    }
    
    return true;
    
}
int splitArray(vector<int>& nums, int m) {
    
    int n=nums.size();
    
    // finding max and sum of array
    
    int start=nums[0];
    int end=nums[0];
    
    for(int i=1;i<n;i++)
    {
        if(nums[i]>start)
            start=nums[i];
        
        end+=nums[i];
    }
    
    
    // applying binary search
    int res=-1;
    
    while(start<=end)
    {
        int mid=start+ (end-start)/2;
        
        if(isvalid(nums, n, m, mid)==true)
        {
            res=mid;
            end=mid-1;
        }
        
        else
            start=mid+1;
    }
    
    return res;
}
};

