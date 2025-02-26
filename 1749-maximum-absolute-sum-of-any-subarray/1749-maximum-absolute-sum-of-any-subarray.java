class Solution {
    public int maxAbsoluteSum(int[] nums) {
        long ans = 0;
        int maxSum = 0, minSum = 0, sum1 = 0, sum2 = 0;

        for (int i : nums) {
            sum1 = Math.max(0, sum1 + i);
            sum2 = Math.min(0, sum2 + i);
            
            maxSum = Math.max(maxSum, sum1);
            minSum = Math.min(minSum, sum2);
        }

        ans = Math.max(maxSum, Math.abs(minSum));
        return (int) ans;
    }
}
