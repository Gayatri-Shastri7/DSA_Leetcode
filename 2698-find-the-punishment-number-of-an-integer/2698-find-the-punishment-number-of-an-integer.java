class Solution {
    public int punishmentNumber(int n) {
        List<Integer> arrlist = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int squared = i * i;
            if (isValidPartition(squared, i)) { 
                arrlist.add(squared);
            }
        }        
        return arrlist.stream().mapToInt(Integer::intValue).sum();
    }
    
    private static boolean isValidPartition(int num, int target) {
        return checkPartition(num, target, 0);
    }

    private static boolean checkPartition(int num, int target, int currentSum) {
        if (num == 0) {
            return currentSum == target;
        }

        int temp = 0, power = 1;
        while (num > 0) {
            int digit = num % 10;
            temp = digit * power + temp;
            power *= 10;
            if (checkPartition(num / 10, target, currentSum + temp)) {
                return true;
            }
            num /= 10;
        }

        return false;
    }
}
