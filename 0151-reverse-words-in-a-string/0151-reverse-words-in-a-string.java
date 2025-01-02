class Solution {
    public String reverseWords(String s) {
        /*
         Input: s = "the sky is blue"
         split()
         ["the", "sky","is","blue"]
           l.                 r
           swap (l,r)
           l++
           r--
           till (l<r)

        */
      
        String[] words = s.trim().split("\\s+");
        int left = 0; int right = words.length-1;
        while(left<right){
            String temp = words[right];
            words[right] = words[left];
            words[left] = temp;
            left++;
            right--;
        }
        return String.join(" ",words);
      








    }
}
