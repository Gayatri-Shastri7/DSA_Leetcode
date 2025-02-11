/* 
 1. Stack 
 2. Convert String to char array, push it in stack 
 3. Iterate over it, check if stack.get(2) = part.charAt(0) 
    - stack.get(3) = part.charAt(1)
    - stack.get(4) = part.charAt(2)
 4. If the above condition is true -> pop()
 5. Return it as the string from the stack using SB
*/
class Solution {
    public static String removeOccurrences(String s, String part) {
        Stack<Character> stack = new Stack<>();
        int partLength = part.length();

        for (char c : s.toCharArray()) {
            stack.push(c);
            if (stack.size() >= partLength) {
                boolean match = true;
                for (int i = 0; i < partLength; i++) {
                    if (stack.get(stack.size() - partLength + i) != part.charAt(i)) {
                        match = false;
                        break;
                    }
                }
                
                if (match) {
                    for (int i = 0; i < partLength; i++) {
                        stack.pop();
                    }
                }
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        
        return sb.toString();
    }
}