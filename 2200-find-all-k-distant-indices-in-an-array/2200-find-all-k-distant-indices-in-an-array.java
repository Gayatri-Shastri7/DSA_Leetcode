class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
      List<Integer> result = new ArrayList<>();
      int sp=0; int ep =0;
      for(int i=0,j=0;i<nums.length;i++){
        if(nums[i] == key){
                for (j = Math.max(i - k, j); j <= Math.min(nums.length - 1, i + k); j++) 
            result.add(j);
        
      }
    }
        return result;

}}