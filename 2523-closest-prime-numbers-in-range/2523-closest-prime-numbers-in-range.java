class Solution {
    public int[] closestPrimes(int left, int right) {
        int n1 = -1, n2 = -1, min1 = -1, min2 = -1, min = Integer.MAX_VALUE;
        for(int i = left;i <= right;i++){
            if(isPrime(i)){
                if(n1 == -1) n1 = i;
                else{
                    if(n2 == -1) n2 = i;
                    else{
                        n1 = n2;
                        n2 = i;
                    }
                    if(n2 - n1 < min){
                        min1 = n1;
                        min2 = n2;
                        min = n2 - n1;
                        if(min == 1 || min == 2) break;
                    }
                }
            }
        }
        return new int[]{min1, min2};
    }
    private boolean isPrime(int n){
        if (n < 2){
            return false;
        }
        for(int i = 2; i * i <= n; i++){
            if (n % i == 0) return false;
        }return true;
    }
}