class Solution {
    public int[] applyOperations(int[] nums) {
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                nums[i-1] = nums[i-1]*2;
                nums[i] = 0;
            }
        }

        int[] result = new int[nums.length];
        int index = 0; 
        for (int num : nums) {
            if (num != 0) {
                result[index++] = num;
            }
        }
        return result;
    }
}