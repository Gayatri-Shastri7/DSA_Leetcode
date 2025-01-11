class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*

        if no 0
        nums = [1,2,3,4]
        nums[0]-1 -> 2*3*4 = 24
        nums[1]-2 -> 1*3*4 = 12
        nums[2]-3 -> 1*2*4 = 8 
        nums[3]-4 -> 1*2*3 = 6
        
        Output:[24,12,8,6] 

        Here, instead of multipying each and every time 

        If 1 zero, then  then in nums[zeroth index]  - multiplied value 

        If more then 1 0 then output all 0    
        1. Multipy all the numbers and divide by i - brute force
        2. Prefix and Postfix array  -optimal 
        */       
        int n = nums.length;
        int result[] = new int[nums.length];
        int prefix[] = new int[nums.length];
        int postfix[] = new int[nums.length];

        prefix[0] = 1;
        postfix[n-1] = 1;

        for(int i=1;i<n;i++){
            prefix[i] = prefix[i-1]*nums[i-1];
        }
        for(int i=n-2;i>=0;i--){
            postfix[i] = postfix[i+1]* nums[i+1];
        }

        for(int i=0;i<n;i++){
            result[i] =postfix[i]*prefix[i];
        }

        return result;

    }
}