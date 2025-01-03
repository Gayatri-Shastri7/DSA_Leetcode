/* 
merged: a p b q c r
word1:  a   b   c
word2:    p   q   r

word1:  ["a",   "b" ,  "c"]
          i
word2:  ["p",   "q" ,  "r"]
          j
          merged.append(i,j)
          i++,j++
          return  String (merged)
*/

class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        char[] merged = new char[n+m];
        int i=0,j=0,k=0;
        
        while(i<n || j<m){
            if(i<n){

                merged[k++] = word1.charAt(i++);
            }
            if(j<m){

                merged[k++] = word2.charAt(j++);
            }
        }
        return new String(merged);

    }
}