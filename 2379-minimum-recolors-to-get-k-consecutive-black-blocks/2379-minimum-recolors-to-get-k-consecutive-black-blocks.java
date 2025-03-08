class Solution {
    public int minimumRecolors(String blocks, int k) {
        int i = 0, j = 0;
        int whiteCount = 0;
        int recolors = Integer.MAX_VALUE;
        
        while (j < blocks.length()) {
            if (j - i + 1 < k) {
                if (blocks.charAt(j) == 'W')
                    whiteCount++;
            } else if (j - i + 1 == k) {
                if (blocks.charAt(j) == 'W')
                    whiteCount++;
                recolors = Math.min(recolors, whiteCount);
                if (blocks.charAt(i) == 'W')
                    whiteCount--;
                i++;
            }
            j++;
        }
        return recolors;
    }
}