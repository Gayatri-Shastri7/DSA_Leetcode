class Solution:
	def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
		graph = defaultdict(list)
		for i,j in edges:
			graph[i].append(j)
			graph[j].append(i)
		parent=[-1 for _ in range(len(amount)+1)]
		time = [-1 for _ in range(len(amount)+1)]
		def dfs(node,par,cnt):
			parent[node]=par
			time[node]=cnt
			for nei in graph[node]:
				if nei!=par:
					dfs(nei,node,cnt+1)
		dfs(0,-1,0)
		curr = bob
		t=0
		while curr!=0:
			if t<time[curr]:
				amount[curr]=0
			elif t==time[curr]:
				amount[curr]//=2
			curr = parent[curr]
			t+=1
		best = -sys.maxsize
		def dfs2(node,par,curr):
			down =0
			for v in graph[node]:
				if v!=par:
					dfs2(v,node,curr+amount[v])
					down+=1
			if down==0:
				nonlocal best
				best = max(best,curr)
		dfs2(0,-1,amount[0])
		return best