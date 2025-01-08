class Solution {
    public int[] leftRightDifference(int[] nums) {
        /*
        nums = [10,4,8,3]. 
        answer =[15]
                i=0: rs = sum(4,8,3).  ls= 0 ans=abs(15-0) update in array 
                i=1: rs = sum(8,3)
                i=2: 
                i=3: 

        2. 
        cALCULATE TOAL SUM. 
        Then subtract 
        */
        int n = nums.length;
        int[] answer = new int[n];
        
        int rightSum = 0;
        for (int num : nums) {
            rightSum += num;
        }
        
        int leftSum = 0;
        for (int i = 0; i < n; i++) {
            rightSum -= nums[i];
            answer[i] = Math.abs(rightSum - leftSum); 
            leftSum += nums[i]; 
        }
        
        return answer;
    }
}
