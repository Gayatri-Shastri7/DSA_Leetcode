class Solution {
    int MOD=1_000_000_007;
    public int countGoodStrings(int low, int high, int zero, int one) {
        int[] dp = new int[high + 1];
        Arrays.fill(dp, -1);
        return help(0, low, high, zero, one, dp);
    }
    private int help(int len, int low, int high, int zero, int one, int[] dp) {
        if (len > high)
            return 0;
        if (dp[len] != -1) {
            return dp[len];
        }
        int count = (len >= low && len <= high) ? 1 : 0;
        count = (count+help(len + zero, low, high, zero, one,dp))%MOD;
        count = (count+help(len + one, low, high, zero, one,dp))%MOD;
        dp[len] = count;
        return count;
    }
}