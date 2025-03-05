class Solution {
    public long coloredCells(int n) {
        /* 
        n=1 -> 1
        n=2 -> 5
        n=3 -> 8 
        */
        
    return (long)n*(2*(n-1))+1;
    }
}