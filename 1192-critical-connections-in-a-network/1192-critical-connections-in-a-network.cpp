#include <bits/stdc++.h>
using namespace std;

class TarjanArticulation {
	public:
		TarjanArticulation(const int N) {
			dfsLow.assign(N, 0);
			dfsNum.assign(N, 0);
			dfsParent.assign(N, 0);
		}

		vector<vector<int>> edges, bridges;
		vector<int> articulationPoints;

		void findBridgesAndArticulationPoints(const int u) {
			dfsLow[u] = dfsNum[u] = id++;
			for (int i = 0; i < int(edges[u].size()); i++) {
				if (!dfsNum[edges[u][i]]) {
					dfsParent[edges[u][i]] = u;
					if (u == dfsRoot)
						rootChildren++;
					findBridgesAndArticulationPoints(edges[u][i]);
					if (dfsLow[edges[u][i]] >= dfsNum[u])
						articulationPoints.push_back(u);
					if (dfsLow[edges[u][i]] > dfsNum[u]) {
						vector<int> edge = {u, edges[u][i]};
						bridges.push_back(edge);
					}
					dfsLow[u] = min(dfsLow[u], dfsLow[edges[u][i]]);
				}
				else if (edges[u][i] != dfsParent[u])
					dfsLow[u] = min(dfsLow[u], dfsLow[edges[u][i]]);
			}
		}

    private:
        vector<int> dfsLow, dfsNum, dfsParent;
        int id = 1;
        int dfsRoot, rootChildren;
};

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        TarjanArticulation tarjan(n);
        tarjan.edges.assign(n, vector<int>());
        for (auto edge : connections)
            tarjan.edges[edge[0]].push_back(edge[1]), tarjan.edges[edge[1]].push_back(edge[0]);
        tarjan.findBridgesAndArticulationPoints(0);
        return tarjan.bridges;
    }
};