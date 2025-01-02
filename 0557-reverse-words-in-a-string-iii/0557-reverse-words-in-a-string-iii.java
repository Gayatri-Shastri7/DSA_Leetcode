class Solution {
    public String reverseWords(String s) {
        /* 
        split()
       words= ["Let's", "take", "LeetCode" ,contest"]
          loop in using for till its end of array
          i=0 -> Let's
                 l   r 
                 while(l<r){
                  swap(l,r)
                 }
        */
        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            char[] word = words[i].toCharArray();
            int left = 0, right = word.length - 1;
                while (left < right) {
                char temp = word[left];
                word[left] = word[right];
                word[right] = temp;
                left++;
                right--;
            }
            words[i] = new String(word);
    }
    return String.join(" ", words);
}
}