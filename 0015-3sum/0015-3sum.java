import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
        3 ptr approach
        i, j -> inital , k->at the end for sorted array. 
        nums = [-1,0,1,2,-1,-4]
               [-4,-1,-1,0,1,2]
                i.  j.       k 
                i++ -> only when k<j
                else 
                i+j+k =0 
            1.  -4-1+2 = -3 < 0 -> j++
            2.  -4-1+2 = -3 < 0 -> j++
            3.  -4+0+2 = -2 < 0 -> j++
            4.  -4+0+1 = -1 < 0 -> j++
            5. j==k , so break, i++,j++
             [-4,-1,-1,0,1,2]
                  i  j     k 
            6. -1-1+2 = 0 -> yes (Got 1 pair) , k--,j++
            7. -1+0+1 =0 -> yes (Got 1 pair) k==j, break;
             [-4,-1,-1,0,1,2]
                     i j   k  -> nums[i]==nums[i+1], i++,j++ 
             [-4,-1,-1,0,1,2]
                       i j k  
            9. 0+2+2 =4 >0 
        */
      
        List<List<Integer>> result = new ArrayList<>();
        
        // Sort the array to use two-pointer approach
        Arrays.sort(nums);
        
        // Iterate through the array
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate elements for `i`
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int j = i + 1; // Left pointer
            int k = nums.length - 1; // Right pointer
            
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                
                if (sum == 0) {
                    // Found a triplet
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    
                    // Move j and k to the next unique elements
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;
                    
                    // Move pointers inward
                    j++;
                    k--;
                } else if (sum < 0) {
                    // Increase the sum by moving the left pointer to the right
                    j++;
                } else {
                    // Decrease the sum by moving the right pointer to the left
                    k--;
                }
            }
        }
        
        return result;
    }
}
