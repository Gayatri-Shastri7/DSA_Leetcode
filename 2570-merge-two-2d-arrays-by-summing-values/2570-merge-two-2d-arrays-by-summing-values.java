class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        /*
         Steps:
         1. Use two pointers, i and j, to iterate through nums1 and nums2.
         2. Compare the IDs at nums1[i][0] and nums2[j][0]:
            - If IDs are equal, sum their values and add the pair to the result.
            - If nums1[i][0] < nums2[j][0], add the current pair from nums1 to the result.
            - If nums1[i][0] > nums2[j][0], add the current pair from nums2 to the result.
         3. Continue until one of the arrays is fully processed.
         4. Add any remaining elements from nums1 or nums2 to the result.
         5. Convert the result list to a 2D array and return it.
        */
        
        int i = 0, j = 0;
        List<int[]> result = new ArrayList<>();
        
        // Two pointers to merge the arrays
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i][0] == nums2[j][0]) {
                // IDs are equal, sum the values
                result.add(new int[]{nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                // ID in nums1 is smaller
                result.add(new int[]{nums1[i][0], nums1[i][1]});
                i++;
            } else {
                // ID in nums2 is smaller
                result.add(new int[]{nums2[j][0], nums2[j][1]});
                j++;
            }
        }
        
        // Add remaining elements from nums1
        while (i < nums1.length) {
            result.add(new int[]{nums1[i][0], nums1[i][1]});
            i++;
        }
        
        // Add remaining elements from nums2
        while (j < nums2.length) {
            result.add(new int[]{nums2[j][0], nums2[j][1]});
            j++;
        }
        
        // Convert the result list to a 2D array
        return result.toArray(new int[result.size()][]);
    }
}
