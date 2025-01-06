 class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int first = 0;
        int totalones = 0;
        int[] ans = new int[n];
        //loop calculated for the first box only
        for(int i=0;i<n;i++){
            if(boxes.charAt(i)=='1'){
                first+=i;
                totalones++;
            }
        }
        ans[0] = first;
        //loop calculated for the remaining boxes
        int leftones =  (boxes.charAt(0)=='0') ? 0 : 1;
        for(int i=1;i<n;i++){
           int rightones = totalones-leftones;
           ans[i] = ans[i-1]-rightones+leftones;
           if(boxes.charAt(i)=='1') leftones++;
        }
        return ans;
    }

}