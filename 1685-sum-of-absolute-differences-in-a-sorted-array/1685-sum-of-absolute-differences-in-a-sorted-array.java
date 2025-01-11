class Solution {
public int[] getSumAbsoluteDifferences(int[] nums) {
    int sum=0;
    int prefix=0;
    int res[]=new int[nums.length];
    for(int a:nums)
    {
       sum+=a; 
    }
    for(int i=0;i<nums.length;i++)
    {
        prefix+=nums[i];
        res[i]=((i+1)*nums[i]-prefix)+((sum-prefix)-((nums.length-1-i)*nums[i]));
    }
    return res;
}
}