class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        long result = 0;
        long[] positions = new long[nums.length];
        long[] prefixSum = new long[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            positions[i] = nums[i] + (s.charAt(i) == 'R' ? d : -d);
        }
        Arrays.sort(positions);
        for (int i = 1; i <= nums.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + positions[i - 1];
        }
        for (int i = 0; i < nums.length; i++) {
            result = (result + positions[i] * i - prefixSum[i]) % (long) (Math.pow(10, 9) + 7);
        }
        return (int) result;
    }
}