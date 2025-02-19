class Solution {
    public String getHappyString(int n, int k) {
        int total = 3 * (1 << (n - 1));
        if (k > total) return "";
        
        StringBuilder result = new StringBuilder(n);
        int group = 1 << (n - 1);
        int startA = 1, startB = startA + group, startC = startB + group;
        
        if (k < startB) {
            result.append('a');
            k -= startA;
        } else if (k < startC) {
            result.append('b');
            k -= startB;
        } else {
            result.append('c');
            k -= startC;
        }
        
        for (int i = 1; i < n; i++) {
            int mid = 1 << (n - i - 1);
            char prev = result.charAt(i - 1);
            
            if (k < mid) {
                result.append(prev == 'a' ? 'b' : (prev == 'b' ? 'a' : 'a'));
            } else {
                result.append(prev == 'a' ? 'c' : (prev == 'b' ? 'c' : 'b'));
                k -= mid;
            }
        }
        
        return result.toString();
    }
}