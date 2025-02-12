/*
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

i != j , sum of digits of the number nums[i] = sum of digits of the number nums[j]

Loop thru all pairs of numbers in the array
If same sum of digit, add both and get max sum

Tc - o(N^2)


*/

class Solution {
    public int maximumSum(int[] nums) {
        int maxSum = -1;

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (digitSum(nums[i]) == digitSum(nums[j])) {
                    maxSum = Math.max(maxSum, nums[i] + nums[j]);
                }
            }
        }

        return maxSum;
    }

    private int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;  
            num /= 10;  
        }
        return sum;
    }
}
