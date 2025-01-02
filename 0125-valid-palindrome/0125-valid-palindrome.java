class Solution {
    public boolean isPalindrome(String s) {
        /*
            s = "A man, a plan, a canal: Panama"
            1. Remove all extra characters and make it lower case ->amanaplanacanalpanama 
            2.amanaplanacanalpanama 
            3. word = ['a','m','a','n',.....'a']
                        l                    r
            4. while(l<r){
                if(charAt(l) != charAt(r));
                return False

                else{
                    l++;
                    r--
                }
            }
            return true
        */
        
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false; // Not a palindrome
            }
            left++;
            right--;
        }
        
        return true; 
        
    }
}