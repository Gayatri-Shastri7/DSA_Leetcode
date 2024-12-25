class Solution {
    public int[] sortArrayByParityII(int[] nums) {
    for (int i = 0, j = 1; i < nums.length; i += 2) {
        if (nums[i] % 2 != 0) { // If the number at an even index is odd
            while (nums[j] % 2 != 0) { // Find the next even number at an odd index
                j += 2;
            }
            // Swap the odd number at an even index with the even number at an odd index
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    return nums;
    }
}