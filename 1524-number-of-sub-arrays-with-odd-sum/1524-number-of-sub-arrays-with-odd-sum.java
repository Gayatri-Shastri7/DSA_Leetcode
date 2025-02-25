class Solution {
    public int numOfSubarrays(int[] arr) {
        long ans = 0;
        int sum = 0, even = 1, odd = 0;

        for (int i : arr) {
            sum += i;
            if (sum % 2 == 0) {
                ans += odd;
                even++;
            } else {
                ans += even;
                odd++;
            }
        }
        return (int) (ans % (1e9 + 7));

    }
}