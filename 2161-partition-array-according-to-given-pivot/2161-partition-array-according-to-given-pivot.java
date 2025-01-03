class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] result = new int [nums.length] ;
        int i = 0, j = nums.length-1, p = i, q = j ;
        
        while (i < nums.length && j >= 0) {
            if (nums[i] < pivot) result[p++] = nums[i] ;
            if (nums[j] > pivot) result[q--] = nums[j] ;
            i++ ;
            j-- ;
        }
        
        while (p <= q) result[p++] = pivot ;
        return result ;
    }
}