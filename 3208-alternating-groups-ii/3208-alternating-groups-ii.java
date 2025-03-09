class Solution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        int concatinatedSize = colors.length + k - 1 ;
        int []concatinatedArray = new int[concatinatedSize];

        System.arraycopy(colors,0,concatinatedArray,0,colors.length);
        System.arraycopy(colors,0,concatinatedArray,colors.length,k-1);

        int count = 0 ;
        int left = 0 ;

        for(int right = 0 ; right < concatinatedArray.length ; right++ ){
            if(right > 0  && concatinatedArray[right] == concatinatedArray[right-1])
                left = right;
            if(right - left + 1 >= k )
                count++;
        }

        return count; 
    }
}