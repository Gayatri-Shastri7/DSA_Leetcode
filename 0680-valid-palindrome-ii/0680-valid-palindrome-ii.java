
        /*
        s = abbac
        true = reverse == original
             = 1 letter+ 

        abbac == cabba
        i        j
        compare both:
        while(cnt<=1)
        if(i!=j)
         j++
        cnt++
        if(i==j){
            i++,j++
        }
        return true;
        }
        return false;
        */

class Solution {
    public boolean validPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        int count = 0;

        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                // Increment count for the mismatch
                count++;

                // If more than one mismatch, return false
                if (count > 1) {
                    return false;
                }

                // Try skipping either the left or the right character
                // To avoid recursion, handle it iteratively
                return isSubPalindrome(s, i + 1, j) || isSubPalindrome(s, i, j - 1);
            }

            // Move pointers inward
            i++;
            j--;
        }

        return true; // No mismatch found, or at most one mismatch
    }

    private boolean isSubPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
