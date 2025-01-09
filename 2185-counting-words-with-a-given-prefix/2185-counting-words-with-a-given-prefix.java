class Solution {
    public int prefixCount(String[] words, String pref) {
        /* 
        words = ["pay","attention","practice","attend"]
        pref = "at"
        output = 2
        
        1. regex.
        2. Loop in the array.
           - Check if at is pref is present in words.
        */
        int cnt =0;
        for(String word: words){
            if(word.startsWith(pref)){
                cnt++;
            }
        }
        return cnt;
    }
}