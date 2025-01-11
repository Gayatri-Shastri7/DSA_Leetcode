class Solution {
    public int bestClosingTime(String customers) {
        /* 
        Y - 1
        N - 0
        Input: customers = "YYNY"
        0 <= j <= n 
        So if customers.length() = 4 +1 =5

        0 - 1+1+0+1 =3
        1 - 0 +1+0+1 = 2
        2 - 00+0+1 =1
        3 - 000+ 1 =1
        4 - 0000+1 = 1
        So 2 is optimal 

        Logic : 
                   YYNY
        prefix_n =[0 0 0 0+1 1+0 1 ] = [0 0 0 1 1] -> N put penalty from begining
        postfix_y =[3 3 2 1+0 1 0]   = [3 2 1 1 0] -> Put y penality from end
        aDD prefix_n, postfix_y =      [3 2 1 1 1] -> 2? 
        */
        int n = customers.length();
        int[] prefix_n = new int[n+1];
        int[] postfix_y = new int[n+1];

        for (int i = 0; i < n; i++) {
            prefix_n[i + 1] = prefix_n[i] + (customers.charAt(i) == 'N' ? 1 : 0); 
        }

        for (int i = n - 1; i >= 0; i--) {
            postfix_y[i] = postfix_y[i + 1] + (customers.charAt(i) == 'Y' ? 1 : 0);
        }
        
        int min_penalty = Integer.MAX_VALUE;
        int best_time =0;
        for(int j=0; j<=n; j++){
            int total_penalty = prefix_n[j]+postfix_y[j];
            if(total_penalty<min_penalty){
                min_penalty= total_penalty;
                best_time=j;
            }

        }
        return best_time;

    }
}