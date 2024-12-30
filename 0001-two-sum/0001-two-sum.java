class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();
      for(int i=0;i<nums.length;i++){
                int j = target - nums[i];

            if (numToIndex.containsKey(j)) {
                return new int[] {numToIndex.get(j), i};
            }
            numToIndex.put(nums[i], i);
        }
        return new int[] {};
      }
        
    }
