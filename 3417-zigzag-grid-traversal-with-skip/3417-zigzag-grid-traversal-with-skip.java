class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        List<Integer> result = new ArrayList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        boolean flag = true; 

        for (int i = 0; i < rows; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < cols; j++) {
                    if (flag) {
                        result.add(grid[i][j]);
                    }
                    flag = !flag; 
                }
            } else {
                for (int j = cols - 1; j >= 0; j--) {
                    if (flag) {
                        result.add(grid[i][j]);
                    }
                    flag = !flag; 
                }
            }
        }

        return result;
    }
}
