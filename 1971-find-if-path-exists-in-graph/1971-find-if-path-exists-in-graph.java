import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        // Step 1: Build the adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u); // Since it's an undirected graph
        }

        // Step 2: Create a visited array to track visited nodes
        boolean[] visited = new boolean[n];

        // Step 3: Call DFS
        return dfs(graph, source, destination, visited);
    }

    private boolean dfs(List<List<Integer>> graph, int node, int destination, boolean[] visited) {
        // Base case: If we reached the destination
        if (node == destination) return true;
        
        // Mark the current node as visited
        visited[node] = true;

        // Traverse all neighbors
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(graph, neighbor, destination, visited)) {
                    return true; // If a path is found, return true
                }
            }
        }

        return false; // No path found
    }
}
