class Solution {
    public String findDifferentBinaryString(String[] nums) {
        /*
        nums =["01","10"]
        1. Cnt len(nums[0])
        If nums ! in combinationn, print any one.
        */
        int n = nums.length;
        StringBuilder sb = new StringBuilder();        
        for (int i = 0; i < n; i++) {
            sb.append(nums[i].charAt(i) == '0' ? '1' : '0');
        }
        return sb.toString();
    }
}