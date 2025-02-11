/* 
Different approaches :
    - BFS or DFS 
    - I choose DFS - Iterate all nodes.
    DFS: 
        - Iterative 
        - Recursive 
        - Convert it into Adj List (Iterative)
        - Convert it into Adj List (Recursive)
*/

class Solution {
    public void dfs(int[][] isConnected, boolean[] visited, int i) {
        visited[i] = true;
        for (int j = 0; j < isConnected.length; j++) {
            if (isConnected[i][j] == 1 && !visited[j]) {
                dfs(isConnected, visited, j);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int cnt_provinces = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i);
                cnt_provinces++;
            }
        }
        return cnt_provinces;
    }
}
