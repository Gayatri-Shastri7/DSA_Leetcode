class Solution {
    private int countSequences(int[] frequency) {
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (frequency[i] == 0)
                continue;
            count++;
            frequency[i]--;
            count += countSequences(frequency);
            frequency[i]++;
        }
        return count;
    }

    public int numTilePossibilities(String tiles) {
        int[] frequency = new int[26];
        for (char c : tiles.toCharArray()) {
            int index = c - 'A';
            frequency[index]++;
        }
        return countSequences(frequency);
    }
}