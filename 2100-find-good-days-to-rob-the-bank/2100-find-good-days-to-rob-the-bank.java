class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        /* 
        Input: security = [5,3,3,3,5,6,2], time = 2 -> value =3 
        Output: [2,3]
                    [5,3,3,3,5,6,2]
                     i
                     1. 0 
                     2. 3 (i) < 5 -> 1 
                     3. i++ -> 3 = 3 -> 1+1
                     4.i++ -> 3 = 3 -> 2+1
                     5.i++ -> 5 >3 -> reset to 0
                     6.i++ -> 6 > 5 -> reset to 0
                     7.i++ -> 2 < 6 -> 0+1
        prefix_gr = [0 1 2 3 0 0 1]

                    [5,3,3,3,5,6,2]
                     i
                     1. 0
                     2. 2<6 -> 0
                     3. i-- -> 6>5 ->  1
                     4. i-- -> 5> 3 -> 2
                     5. i-- -> 3 =3 -> 3
                     6.  i-- -> 3=3 -> 4
                     7. i-- -> 3< 5 -> 0

        postfix_gr= [3 2 1 0 0 1 0]

        prefix_gr = [0 1 2 3 0 0 1]
        postfix_gr= [0 4 3 2 1 0 0] 

        */
        int n = security.length;
        List<Integer> goodDays = new ArrayList<>();

        if (time == 0) {
            for (int i = 0; i < n; i++) {
                goodDays.add(i);
            }
            return goodDays;
        }
        int[] nonIncreasing = new int[n];
        int[] nonDecreasing = new int[n];

        for (int i = 1; i < n; i++) {
            if (security[i] <= security[i - 1]) {
                nonIncreasing[i] = nonIncreasing[i - 1] + 1;
            }
        }

        for (int i = n - 2; i >= 0; i--) {
            if (security[i] <= security[i + 1]) {
                nonDecreasing[i] = nonDecreasing[i + 1] + 1;
            }
        }

        for (int i = time; i < n - time; i++) {
            if (nonIncreasing[i] >= time && nonDecreasing[i] >= time) {
                goodDays.add(i);
            }
        }

        return goodDays;

    }
}