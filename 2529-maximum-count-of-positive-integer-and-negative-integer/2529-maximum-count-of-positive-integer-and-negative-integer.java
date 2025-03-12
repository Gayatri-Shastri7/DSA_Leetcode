class Solution {
    public int maximumCount(int[] nums) {
        int n = nums.length;
        int st = 0, end = n - 1, pos, neg, mid;

        while(st <= end){
            mid = st + (end - st) / 2;

            if(nums[mid] > 0){
                end = mid - 1;
            }else{
                st = mid + 1;
            }
        }

        pos = n - st;

        st = 0;
        end = n - 1;

        while(st <= end){
            mid = st + (end - st) / 2;

            if(nums[mid] < 0){
                st = mid + 1;
            }else{
                end = mid - 1;
            }
        }

        neg = end + 1;

        return Math.max(pos, neg);
    }
}