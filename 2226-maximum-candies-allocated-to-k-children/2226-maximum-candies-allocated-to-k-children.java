class Solution {
    private static final int MAX = 10_000_001;

    public int maximumCandies(int[] candies, long k) {
        return binSearch(candies, k, 1, MAX) - 1;
    }
    
    private boolean check(int[] candies, long k, int value) {
        long sum = 0;
        for (int candy : candies) {
            sum += (long) candy / value;
        }
        return sum >= k;
    }
    
    private int binSearch(int[] candies, long k, int left, int right) {
        if (left >= right) return right;
        
        int mid = left + (right - left) / 2;
        
        return check(candies, k, mid) 
            ? binSearch(candies, k, mid + 1, right) 
            : binSearch(candies, k, left, mid);
    }
}