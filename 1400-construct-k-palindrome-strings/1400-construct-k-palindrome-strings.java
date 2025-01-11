class Solution {
    public boolean canConstruct(String s, int k) {
        /* 
        Input: s = "annabelle", k = 2
        Output: true      
        */
        if(s.length() < k) return false;

        HashMap<Character, Integer> cc = new HashMap<>();
        for(char c : s.toCharArray()){
            cc.put(c,cc.getOrDefault(c,0)+1);
        }

        int oc=0;
        for(int f : cc.values()){
            if(f %2 !=0) oc++;
        }
        return oc <=k;
    }
}