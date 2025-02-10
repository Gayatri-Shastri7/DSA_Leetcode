class Solution {
    public String clearDigits(String s) {
        String res = "";

        /*
        Initialize Stack
        
        Stack<Character> str = new Stack<Character>();
        Push the string given in stack
        */

        Stack<Character> str = new Stack<Character>();
        for(char ch : s.toCharArray()){
        if(Character.isDigit(ch)){
            if(!str.isEmpty() && !Character.isDigit(str.peek()))
                str.pop();
        }
         else{
            str.push(ch);
        }
        }
       
    

    StringBuilder sb = new StringBuilder();
    for(char ch : str){
        sb.append(ch);
    }
    return sb.toString();
}
}