/* 
beans = [4,1,6,5]  
Remove atleast 1, making 1 bag =0, other should be same values.

sort()
1,4,5,6 -> use hashmap to preserve indices
index=  1 0 3 2 
remove the first one in sorted -> 0 4 5 6
remove 4,5  
*/

public class Solution {
    public long minimumRemoval(int[] beans) {
        Arrays.sort(beans);
        int n = beans.length;
        long totalBeans = 0;
        for (int bean : beans) {
            totalBeans += bean;
        }        
        long minRemoval = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long beansToKeep = (long) beans[i] * (n - i);
            long currentRemoval = totalBeans - beansToKeep;
            minRemoval = Math.min(minRemoval, currentRemoval);
        }
        
        return minRemoval;
    }
}
