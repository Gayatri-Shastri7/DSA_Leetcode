class Solution {
    public String reverseVowels(String s) {
        char[] result = s.toCharArray();
        String vowels = "aeiouAEIOU";
        int left=0; int right = result.length -1;
            while (left < right) {

            while (left < right && vowels.indexOf(result[left]) == -1) {
                left++;
            }
            while (left < right && vowels.indexOf(result[right]) == -1) {
                right--;
            }
            char temp = result[left];
            result[left] = result[right];
            result[right] = temp;

            left++;
            right--;
        }
        return new String(result);
        
    }
}