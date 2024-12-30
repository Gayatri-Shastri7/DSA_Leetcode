class Solution {
    public int threeSumClosest(int[] nums, int target) {
     /*
       [-1,2,1,-4] 
        i  j    k 
        1. -1+2-4 = -3 < -1 , k--
        2. -1+2+1 = 2 > -1

        [-4,-1,1,2] 
          i j    k 
        hashset - (-4,-1,-2)
        1. -4-1+2 = -3 < 1, j++
        2. -4+1+2 = -1 < 1, j++ -> j==k, break 
        3. i++ , j++ 
        [-4,-1,1,2] 
             i j k 
        4. -1+1+2 = 2 < 1 -> j++ 
        5. j==k, break -> i++,j++ , if (j==k), end ->while
    */ 
            Arrays.sort(nums);
        
        // Variable to track the closest sum
        int closestSum = Integer.MAX_VALUE / 2; // Use a large value to avoid overflow
        
        // Outer loop for the first pointer
        for (int i = 0; i < nums.length - 2; i++) {
            int j = i + 1; // Left pointer
            int k = nums.length - 1; // Right pointer
            
            // Two-pointer approach
            while (j < k) {
                int currentSum = nums[i] + nums[j] + nums[k];
                
                // Update closest sum if current is closer to the target
                if (Math.abs(target - currentSum) < Math.abs(target - closestSum)) {
                    closestSum = currentSum;
                }
                
                // Adjust pointers based on the comparison with the target
                if (currentSum < target) {
                    j++; // Increase the sum by moving left pointer to the right
                } else if (currentSum > target) {
                    k--; // Decrease the sum by moving right pointer to the left
                } else {
                    // If currentSum == target, it's the closest possible
                    return currentSum;
                }
            }
        }
        
        return closestSum;

    }
}